"""Tạo ảnh (keyframe/thumbnail) bằng Nano Banana qua Gemini API.

QUAN TRỌNG (đã verify live): Nano Banana KHÔNG dùng :predict (404 "not supported
for predict"). Nó dùng :generateContent với responseModalities=["IMAGE"], ảnh trả
về base64 trong candidates[].content.parts[].inline_data[].data.

Model id (từ ModelService.ListModels đã verify):
  gemini-3.1-flash-image (Nano Banana 2) — mặc định
  gemini-3-pro-image (Nano Banana Pro)
  gemini-3.1-flash-lite-image (Nano Banana 2 Lite)

Cách dùng:
  python generate_image.py "prompt" --model nano-banana-2 --out-prefix thumb
"""
import argparse
import base64
import json
import sys
import urllib.request
import urllib.error

from config import get_api_key, BASE_URL, IMAGE_MODELS

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
# Ép UTF-8 cho stdout/stderr để script chạy được mà không cần set biến môi trường.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


# alias -> model id
ALIAS = IMAGE_MODELS


def generate(prompt, model, key, count=1):
    url = f"{BASE_URL}/models/{model}:generateContent?key={key}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            # Nano Banana chỉ nhận IMAGE modality; để count>1 thì lặp gọi riêng bởi vì
            # model không có sampleCount đáng tin như :predict.
            "responseModalities": ["IMAGE"],
        },
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt")
    ap.add_argument("--model", default="nano-banana-2", choices=list(ALIAS.keys()))
    ap.add_argument("--out-prefix", default="img", help="Prefix; sẽ thêm _0.png, _1.png...")
    ap.add_argument("--count", type=int, default=1, help="Số ảnh; gọi lặp model từng lần.")
    args = ap.parse_args()

    key = get_api_key()
    model = ALIAS[args.model]

    # gọi lần lượt count lần (mỗi lần 1 ảnh), gom lại
    imgs = []
    for i in range(max(1, args.count)):
        status, body = generate(args.prompt, model, key)
        if status != 200:
            print(f"[{status}] {str(body)[:200]}")
            if status == 429:
                print("HẾT QUOTA (Nano Banana).")
            elif status == 404:
                print("Sai model id / endpoint. Kiểm tra ListModels.")
            sys.exit(1)
        # ảnh base64 trong candidates[].content.parts[].inline_data.data
        found = False
        for cand in body.get("candidates", []):
            for part in cand.get("content", {}).get("parts", []):
                data = part.get("inlineData", part.get("inline_data", {}))
                if isinstance(data, dict) and data.get("data"):
                    imgs.append(data["data"])
                    found = True
        if not found:
            print("Không tìm thấy ảnh trong response:", json.dumps(body)[:300])
            sys.exit(1)

    for i, b64 in enumerate(imgs):
        path = f"{args.out_prefix}_{i}.png"
        with open(path, "wb") as f:
            f.write(base64.b64decode(b64))
        print(f"Đã lưu {path}")
    print(f"Tổng cộng {len(imgs)} ảnh.")


if __name__ == "__main__":
    main()
