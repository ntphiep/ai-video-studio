"""Tạo video từng shot bằng Veo 3.1 hoặc Gemini Omni qua Gemini API.

Cách dùng:
  python generate_video.py "prompt mo ta hanh dong" \
      --model fast --aspect 16:9 --out clip_01.mp4

Endpoint ĐÚNG cho Veo (đã verify): POST /v1beta/models/<model>:predictLongRunning
  - KHÔNG dùng :generateVideos hay :predictLongRunningGenerateVideos (404)
  - KHÔNG dùng numberOfVideos (model từ chối)
Schema: {"instances":[{"prompt":"..."}],"parameters":{"aspectRatio":"..."}}
Luồng: tạo operation (trả "name") -> poll GET /v1beta/<name> cho tới done.
"""
import argparse
import json
import sys
import time
import urllib.request
import urllib.error

from config import get_api_key, BASE_URL, VEOS, OMNI

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
# Ép UTF-8 cho stdout/stderr để script chạy được mà không cần set biến môi trường.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


# alias thân thiện -> model id; nhận cả model id đầy đủ
MODELS = {
    **VEOS,
    "omni": OMNI,
    "quality": VEOS["standard"],
}


def _post(url, payload, key):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            body = json.load(e)
        except Exception:
            body = {"message": e.read().decode(errors="replace")}
        return e.code, body


def create_operation(model, prompt, aspect, key, duration=None):
    """Tạo operation tạo video.

    - Veo (veo-3.1-*) dùng :predictLongRunning (đã verify: không phải generateVideos).
    - Gemini Omni chỉ hỗ trợ :generateContent + responseModalities=["VIDEO"]
      (đã verify live: predictLongRunning → 404). Trả về inline video có thể là
      generateContent đồng bộ; nếu responseModalities VIDEO thì payload khác.
    """
    if model.startswith("gemini-omni") or model.startswith("gemini-3."):
        # Omni: generateContent, không long-running
        url = f"{BASE_URL}/models/{model}:generateContent?key={key}"
        # Omni không có tham số thời lượng riêng trong schema đã verify.
        # Cách ĐÃ VERIFY để đặt thời lượng: viết thẳng vào prompt.
        # Bằng chứng: câu "Create one 8-second video ..." cho ra file đo được
        # đúng 8.000000 giây (ffprobe). Xem references/format-and-export.md mục 4.
        # Omni KHÔNG có tham số aspectRatio lẫn tham số thời lượng trong schema.
        # Cách duy nhất đã kiểm chứng là ghi thẳng yêu cầu vào prompt. Trước đây
        # chỉ làm vậy cho thời lượng, còn --aspect thì bị bỏ qua hoàn toàn nên
        # người dùng chọn 9:16 mà vẫn nhận khung ngang.
        yeu_cau = []
        if duration:
            yeu_cau.append(f"one {duration}-second video")
        else:
            yeu_cau.append("one video")
        if aspect == "9:16":
            yeu_cau.append("in vertical 9:16 portrait format")
        elif aspect == "16:9":
            yeu_cau.append("in horizontal 16:9 landscape format")
        text = f"Create {' '.join(yeu_cau)}. {prompt}"
        payload = {
            "contents": [{"parts": [{"text": text}]}],
            "generationConfig": {"responseModalities": ["VIDEO"]},
        }
    else:
        # Veo: predictLongRunning
        url = f"{BASE_URL}/models/{model}:predictLongRunning?key={key}"
        params = {"aspectRatio": aspect}
        if duration:
            # Nguồn: ai.google.dev/gemini-api/docs/veo, đọc HTML thô ngày 06/09/2026.
            # Nguyên văn trên trang: durationSeconds : Length of the generated video.
            #   "4" , "6" , "8" . Must be "8" when using extension, reference images
            #   or with 1080p and 4k resolutions
            # Vậy giá trị là CHUỖI, không phải số nguyên. Và Veo KHÔNG nhận 10 giây;
            # chỉ Omni mới có mức 10 giây (đo trên giao diện Flow ngày 06/09/2026).
            if int(duration) not in (4, 6, 8):
                raise SystemExit(
                    f"Veo chỉ nhận durationSeconds 4, 6 hoặc 8 (bạn truyền {duration}). "
                    "Muốn 10 giây thì dùng --model omni."
                )
            params["durationSeconds"] = str(int(duration))
        payload = {
            "instances": [{"prompt": prompt}],
            "parameters": params,
        }
    return _post(url, payload, key)


def poll_operation(name, key, timeout=600, interval=8):
    url = f"{BASE_URL}/{name}?key={key}"
    start = time.time()
    while time.time() - start < timeout:
        status, body = _post_no_body(url, key)
        if status != 200:
            return status, body
        if body.get("done"):
            return 200, body
        # body thường có response.video.uri khi xong
        time.sleep(interval)
    return 504, {"error": {"message": "timeout"}}

def _post_no_body(url, key):
    req = urllib.request.Request(url, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            body = json.load(e)
        except Exception:
            body = {"message": e.read().decode(errors="replace")}
        return e.code, body


def _retry_delay(body):
    """Đọc retryDelay trong error.details nếu API có gửi. Trả số giây hoặc None.

    Google trả dạng {"@type": ".../google.rpc.RetryInfo", "retryDelay": "27s"}.
    """
    details = ((body.get("error") or {}).get("details") or [])
    for d in details:
        if not isinstance(d, dict):
            continue
        raw = d.get("retryDelay")
        if isinstance(raw, str) and raw.endswith("s"):
            try:
                return float(raw[:-1])
            except ValueError:
                return None
    return None


def handle_error(status, body):
    """Phân loại HTTP status. Trả 'ok' | 'retry' | 'stop'.

    Bảng lỗi đầy đủ nằm ở references/api-guide.md mục 8, KHÔNG phải SKILL.md.
    Quy tắc 429 theo đúng tài liệu đó: có retryDelay thì chờ rồi gọi lại,
    không có thì mới dừng hẳn.
    """
    if 200 <= status < 300:
        return "ok"
    msg = (body.get("error") or {}).get("message", str(body))
    print(f"[{status}] {msg}")
    if status == 429:
        delay = _retry_delay(body)
        if delay is not None:
            print(f"Bị giới hạn tốc độ, API bảo chờ {delay}s rồi gọi lại.")
            time.sleep(delay)
            return "retry"
        print("HẾT QUOTA và API không kèm retryDelay. Kiểm tra billing tại https://ai.dev/rate-limit. Ngừng.")
        return "stop"
    if status == 400:
        print("Sai payload. Sửa schema (instances[] / bỏ numberOfVideos).")
        return "stop"
    if status in (500, 504):
        print("Lỗi thoáng, retry...")
        return "retry"
    if status == 404:
        print("Sai endpoint/model. Kiểm tra model id + suffix :predictLongRunning.")
        return "stop"
    return "stop"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt", help="Prompt mô tả hành động cho 1 shot")
    ap.add_argument("--model", default="fast", choices=list(MODELS.keys()))
    ap.add_argument("--aspect", default="16:9", choices=["16:9", "9:16"])
    ap.add_argument("--duration", type=int, default=None, choices=[4, 6, 8, 10],
                    help="Thời lượng giây. Giao diện Flow cho Omni chọn 4/6/8/10. Doc Veo ghi rõ chỉ nhận chuỗi 4, 6, 8, và bắt buộc là 8 khi dùng extension, reference images, 1080p hoặc 4k.")
    ap.add_argument("--out", default="clip.mp4", help="File lưu video")
    ap.add_argument("--max-retry", type=int, default=3)
    args = ap.parse_args()

    key = get_api_key()
    # alias thân thiện -> model id; nhận cả model id đầy đủ
    model = MODELS.get(args.model, args.model)

    for attempt in range(args.max_retry + 1):
        status, body = create_operation(model, args.prompt, args.aspect, key,
                                        duration=args.duration)
        action = handle_error(status, body)
        if action == "stop":
            sys.exit(1)
        if action == "retry":
            time.sleep(5 * (attempt + 1))
            continue
        # success. Phân nhánh:
        #   - Veo (predictLongRunning): body có "name" → poll tới khi done.
        #   - Omni (generateContent): body có candidates ngay (đồng bộ) → dùng luôn.
        if body.get("name"):
            name = body["name"]
            print(f"Operation created: {name}")
            status, final_body = poll_operation(name, key)
            if status != 200:
                handle_error(status, final_body)
                sys.exit(1)
            final = final_body
        elif body.get("candidates"):
            print("Omni generateContent trả ngay (đồng bộ).")
            final = body
        else:
            handle_error(status, body)
            sys.exit(1)
        # tìm uri video
        kind, val = extract_uri(final)
        if not val:
            print("Không tìm thấy uri video trong response:", json.dumps(final)[:400])
            sys.exit(1)
        if kind == "base64":
            import base64 as _b64
            with open(args.out, "wb") as f:
                f.write(_b64.b64decode(val))
        else:
            download(val, args.out)
        print(f"Đã tải video -> {args.out}")
        return

    print("Thất bại sau nhiều lần retry.")


def extract_uri(body):
    """Tìm uri video/ảnh trong nhiều dạng response.

    - predictLongRunning (Veo): body["response"]["video"]["uri"]
    - generateContent (Omni): candidates[].content.parts[].inlineData.data
      (base64) — phải lưu dạng khác, nên trả về ("base64", data) hoặc ("uri", u).
    Trả về (kind, value): kind='uri' | 'base64'.
    """
    # 1) dạng predictLongRunning
    resp = body.get("response", {})
    v = resp.get("video") if isinstance(resp, dict) else None
    if v and isinstance(v, dict):
        u = v.get("uri") or v.get("url")
        if u:
            return "uri", u
    # 2) dạng generateContent (inlineData base64)
    for cand in body.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            d = part.get("inlineData") or part.get("inline_data", {})
            if d.get("data"):
                return "base64", d["data"]
    return None, None


def download(uri, path):
    import shutil
    req = urllib.request.Request(uri, headers={"User-Agent": "skill"})
    with urllib.request.urlopen(req) as resp, open(path, "wb") as out:
        shutil.copyfileobj(resp, out)


if __name__ == "__main__":
    main()
