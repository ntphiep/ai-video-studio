"""Viết kịch bản + chia shot cho video bằng Gemini, linh hoạt chọn model.

Script gọi lần lượt vài model viết kịch bản, chấm điểm output bằng một hàm
đánh giá đơn giản, chọn bản tốt nhất, rồi xuất JSON spec cho pipeline.

Cách dùng:
  python write_script.py "Làm video giáo dục ngắn về cách dậy sớm" \
      --format shorts --character "mèo vàng VN" --out spec.json
"""
import argparse
import json
import re
import sys
import urllib.request
import urllib.error

from config import get_api_key, BASE_URL

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
# Ép UTF-8 cho stdout/stderr để script chạy được mà không cần set biến môi trường.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


# Danh sách model viết kịch bản, thử lần lượt cho tới khi có bản dùng được.
#
# MỨC BẰNG CHỨNG, đọc kỹ trước khi sửa danh sách này:
#   gemini-3.5-flash        đã tự gọi thử và nhận 200. Đây là lý do nó đứng đầu.
#   gemini-3.7-flash        [chưa xác minh] KHÔNG có trong kết quả GET /v1beta/models
#                           ngày 06/09/2026 trên key thật. Giữ lại làm phương án dự
#                           phòng phòng khi tài khoản khác có, nhưng đừng coi là chắc.
#   gemini-3.1-pro-preview  [chưa xác minh] cũng không có trong danh sách models đó.
# Danh sách model thật đã liệt kê ở references/api-guide.md mục 7.
WRITER_MODELS = [
    "gemini-3.5-flash",
    "gemini-3.7-flash",
    "gemini-3.1-pro-preview",
]

PROMPT_TEMPLATE = """Bạn là biên kịch video AI. Viết kịch bản cho: {topic}

Định dạng: {format} ({format_desc})
Nhân vật chính: {character}
Giọng đọc: {voice}
Nhạc nền: {voice_music}

Yêu cầu:
1. Chia kịch bản thành các shot, mỗi shot 4-8 giây (giới hạn hard của Veo, không quá).
2. Mỗi shot có: scene_prompt (mô tả hành động + camera + nhân vật + thoại, đơn giản rõ ràng),
   dialogue (lời thoại nếu có), duration (giây).
3. Viết scene_prompt bằng {scene_lang} (chất lượng tốt nhất), thoại/narration tiếng Việt.
4. Mỗi shot 1 hành động rõ ràng, không nhồi nhiều chi tiết (dễ blur/biến dạng).
5. Trả về DUY NHẤT JSON hợp lệ (không markdown, không text ngoài) theo cấu trúc:
{{
  "script": "kịch bản tóm tắt",
  "shots": [
    {{"id":1, "duration":6, "scene_prompt":"...", "character":"...", "dialogue":"...", "video_format":"16:9", "keyframe_images":[], "voice_speaker":"male_vietnamese"}}
  ],
  "thumbnail_prompt": "...",
  "voiceover_script": "...",
  "music_style": "..."
}}
Chỉ trả về JSON. Không thêm chú thích.
"""


def _post_generate(model, prompt, key):
    url = f"{BASE_URL}/models/{model}:generateContent?key={key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.7},
    }
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


def extract_text(body):
    try:
        return body["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return ""


def parse_json(text):
    # tách JSON khỏi markdown fence nếu có
    m = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
    if m:
        text = m.group(1)
    # lấy từ { đầu tiên đến } cuối cùng
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        return None
    try:
        return json.loads(text[start:end + 1])
    except json.JSONDecodeError:
        return None


def score_output(spec, num_shots):
    """Đánh giá chất lượng JSON trả về: càng đầy đủ + càng nhiều shot hợp lý càng tốt."""
    s = 0
    if not spec:
        return -1
    shots = spec.get("shots", [])
    s += min(len(shots), num_shots) * 2          # có đủ shot
    s += 3 if spec.get("voiceover_script") else 0
    s += 2 if spec.get("thumbnail_prompt") else 0
    s += 1 if spec.get("music_style") else 0
    valid = all(0 < sh.get("duration", 0) <= 8 and sh.get("scene_prompt") for sh in shots)
    s += 2 if valid else 0
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("topic", help="Chủ đề/kịch bản video")
    ap.add_argument("--format", default="shorts", choices=["shorts", "long"])
    ap.add_argument("--num-shots", type=int, default=6)
    ap.add_argument("--character", default="mèo vàng nước Việt Nam")
    ap.add_argument("--voice", default="nam trầm ấm 25 tuổi, tiếng Việt")
    ap.add_argument("--music", default="upbeat acoustic ấm áp")
    ap.add_argument("--out", default="spec.json")
    ap.add_argument("--lang", default="en", choices=["en", "vi"],
                    help="Ngôn ngữ scene_prompt. Mặc định 'en' (chất lượng tốt nhất).")
    args = ap.parse_args()

    key = get_api_key()
    subj = args.topic
    fmt = "9:16 dọc (Shorts, <=60s)" if args.format == "shorts" else "16:9 ngang (video dài)"

    prompt = PROMPT_TEMPLATE.format(
        topic=subj, format=args.format, format_desc=fmt,
        character=args.character, voice=args.voice, voice_music=args.music,
        scene_lang=("tiếng Anh" if args.lang == "en" else "tiếng Việt"),
    )

    best = None
    best_score = -1
    best_model = None
    for model in WRITER_MODELS:
        print(f"⟳ Thử {model} ...")
        status, body = _post_generate(model, prompt, key)
        if status != 200:
            print(f"  [{status}] {body}")
            continue
        text = extract_text(body)
        spec = parse_json(text)
        sc = score_output(spec, args.num_shots)
        print(f"  score={sc}")
        if sc > best_score:
            best_score = sc
            best = spec
            best_model = model
            if sc >= args.num_shots * 2 + 5:   # đạt chuẩn cao thì dừng sớm
                print(f"  → đạt chuẩn, dừng.")
                break

    if best is None:
        print("Không model nào trả về kịch bản JSON hợp lệ. Thử lại / đổi key.")
        sys.exit(1)

    # thêm model dùng để trace
    best["_writer_model"] = best_model
    best["_writer_score"] = best_score
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(best, f, ensure_ascii=False, indent=2)
    print(f"\n✅ Kịch bản từ {best_model} (score {best_score}) -> {args.out}")
    print(f"  {len(best.get('shots', []))} shot. Đếm lại bằng: "
          f"jq '.shots | length' {args.out}")


if __name__ == "__main__":
    main()
