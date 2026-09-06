"""Tạo narration (giọng đọc tiếng Việt) bằng Gemini 3.1 Flash TTS,
và nhạc nền bằng Lyria 3.

QUAN TRỌNG (chi tiết ở references/api-guide.md):
- Chia narration thành chunk ngắn (~1 phút) vì TTS drift chất lượng khi dài.
- BẮT BUỘC retry logic vì model thỉnh thoảng trả 500 ngẫu nhiên.
- voiceName PHẢI là TÊN NHÂN VẬT (Puck/Charon/Fenrir/Leda...).
  KHÔNG dùng mã BCP-47: `vi`, `vi-VN-*`, `en-US` đều trả 400
  "No matching speaker voice found" (đã gọi thật và gặp lỗi).
  Model tự nhận ngôn ngữ từ nội dung văn bản.
- LƯU Ý: script này CHƯA tự chia chunk. Dòng trên chỉ là khuyến nghị cho
  người dùng tự cắt text trước khi gọi. Retry thì đã có sẵn.
- Audio trả về base64 trong response.

Cách dùng (tham số thật là --style, KHÔNG phải --music-style):
  python generate_audio.py --tts "Lời thoại cần đọc" --out voice_01.wav
  python generate_audio.py --music "upbeat acoustic" --style clip --out music.wav

Về đuôi file: TTS trả PCM thô và script tự bọc header WAV, nên phải đặt đuôi
.wav. Đặt .mp3 sẽ ra một file WAV mang tên sai, nhiều trình phát sẽ từ chối.
"""
import argparse
import base64
import json
import sys
import time
import urllib.request
import urllib.error

from config import get_api_key, BASE_URL, TTS, MUSIC

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
# Ép UTF-8 cho stdout/stderr để script chạy được mà không cần set biến môi trường.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass



def _post(url, payload, key):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.load(e)
        except Exception:
            return e.code, {"error": {"message": e.read().decode(errors="replace")}}


# TTS trả raw PCM L16 (audio/l16; rate=24000; channels=1) — KHÔNG phải MP3.
# mime này là LINEAR PCM; đổi tên file .wav mới mở được bằng ffmpeg/player.
_MIME_EXT = {
    "audio/l16": "wav",   # PCM 16-bit, có thể đóng gói .wav (thêm header WAV nếu cần)
    "audio/wav": "wav",
    "audio/mpeg": "mp3",
    "audio/wave": "wav",
}


def tts(text, key, out, speaker="Puck", retries=6):
    # endpoint TTS dùng :generateContent với config audio
    url = f"{BASE_URL}/models/{TTS}:generateContent?key={key}"
    payload = {
        "contents": [{"parts": [{"text": "synthesise speech:\n" + text}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {
                "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": speaker}}
            },
        },
    }
    for attempt in range(retries):
        status, body = _post(url, payload, key)
        if status == 200:
            audio, mime = extract_audio(body)
            if audio:
                data = base64.b64decode(audio)
                # audio/l16 là PCM raw, cần thêm header WAV trước khi ghi
                if (mime and mime.startswith("audio/l16")) or (".wav" in out.lower() and not out.lower().endswith(".mp3")):
                    data = _wrap_wav(data, rate=24000, channels=1)
                with open(out, "wb") as f:
                    f.write(data)
                print(f"Narration -> {out} (mime={mime}, {len(data)} bytes)")
                return True
            print("200 nhưng không có audio part:", json.dumps(body)[:200])
            return False
        print(f"[{status}] {str(body)[:100]}")
        # 429 có retryDelay; 500 thoáng. Chờ tối thiểu để vượt rate limit 3/phút.
        wait = _retry_delay(body) or (20 if status == 429 else 3 * (attempt + 1))
        print(f"  chờ {wait:.0f}s rồi retry...")
        time.sleep(wait)
    print("TTS thất bại sau retries.")
    return False


def _retry_delay(body):
    """Lấy retryDelay (giây, số) từ error.details[].RetryInfo nếu có.

    API trả dạng '2.745184562s' (chuỗi kèm 's') chứ không phải số → parse.
    """
    import re
    try:
        for d in body.get("error", {}).get("details", []):
            if "RetryInfo" in str(d.get("@type", "")):
                raw = d.get("retryDelay")
                if raw is None:
                    return None
                m = re.match(r"([\d.]+)", str(raw))
                return float(m.group(1)) if m else None
    except Exception:
        pass
    return None


def _wrap_wav(pcm_bytes, rate=24000, channels=1, sample_width=2):
    """Đóng gói PCM 16-bit raw thành WAV (RIFF) để ffmpeg/player đọc được."""
    import struct
    byte_rate = rate * channels * sample_width
    block_align = channels * sample_width
    data_len = len(pcm_bytes)
    header = b"RIFF" + struct.pack("<I", 36 + data_len) + b"WAVE" \
        + b"fmt " + struct.pack("<IHHIIHH", 16, 1, channels, rate, byte_rate, block_align, sample_width * 8) \
        + b"data" + struct.pack("<I", data_len)
    return header + pcm_bytes


def extract_audio(body):
    """Trả (base64_data, mimeType hoặc None) của audio đầu tiên.

    ⚠️ API trả key camelCase `inlineData` (Không phải `inline_data`).
    mimeType dạng "audio/l16; rate=24000; channels=1".
    """
    for cand in body.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            d = part.get("inlineData") or part.get("inline_data", {})
            b = d.get("data")
            if b:
                return b, (d.get("mimeType") or d.get("mime_type"))
    return None, None


def music(prompt, key, out, style="clip", retries=3):
    """Sinh nhạc nền. CÓ retry vì cùng API với TTS, cùng rủi ro 500 ngẫu nhiên.

    Trước đây hàm này gọi đúng một lần rồi bỏ cuộc, dù docstring đầu file ghi
    retry là bắt buộc. Nay xử lý giống tts().
    """
    model = MUSIC[style]
    url = f"{BASE_URL}/models/{model}:generateContent?key={key}"
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    status, body = None, None
    for attempt in range(retries):
        status, body = _post(url, payload, key)
        if status == 200:
            break
        print(f"[{status}] lần {attempt + 1}/{retries}: {str(body)[:160]}")
        if status not in (500, 503, 504, 429):
            break
        time.sleep(3 * (attempt + 1))
    if status != 200:
        return False
    audio, mime = extract_audio(body)
    if not audio:
        print("Không có audio:", json.dumps(body)[:200])
        return False
    with open(out, "wb") as f:
        f.write(base64.b64decode(audio))
    print(f"Nhạc nền -> {out}")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tts", help="Văn bản cảm xúc để đọc (narration)")
    ap.add_argument("--music", help="Mô tả phong cách nhạc nền")
    ap.add_argument("--style", default="clip", choices=["clip", "pro", "latest"],
                    help="Model nhạc. latest là lyria-3.5, bản mới nhất.")
    ap.add_argument("--speaker", default="Puck", help="VoiceName (vd Puck/Charon/Fenrir/Leda — tên nhân vật, KHÔNG phải BCP-47). Model tự detect ngôn ngữ từ văn bản.")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    key = get_api_key()
    if args.tts:
        ok = tts(args.tts, key, args.out, args.speaker)
    elif args.music:
        ok = music(args.music, key, args.out, args.style)
    else:
        print("Cần --tts hoặc --music.")
        ok = False
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
