#!/usr/bin/env python3
"""Sinh ảnh bằng Cloudflare Workers AI (FLUX.1 schnell), bậc miễn phí.

Vì sao cần: Nano Banana tốn quota Gemini. Với ảnh nháp, ảnh thử bố cục, hay
ảnh nền không đòi nhân vật nhất quán, dùng bậc miễn phí của Cloudflare để dành
quota Gemini cho việc thật sự cần.

Bậc miễn phí: 10.000 Neuron mỗi ngày, reset 00:00 UTC, không cần thẻ tín dụng.
Nguồn: https://developers.cloudflare.com/workers-ai/platform/pricing/ đọc 09/09/2026.

Hợp đồng API đọc trực tiếp từ trang model, ngày 09/09/2026:
https://developers.cloudflare.com/workers-ai/models/flux-1-schnell/
- POST {CF_BASE}@cf/black-forest-labs/flux-1-schnell
- Header `Authorization: Bearer <token>`
- Body: prompt (bắt buộc, tối đa 2048 ký tự), seed (tuỳ chọn), steps (mặc định
  4, tối đa 8)
- Response: trường `image` chứa ảnh **JPEG mã hoá base64**, không phải PNG.

Hạn chế cần biết trước khi dùng: model này KHÔNG nhận ảnh tham khảo, nên không
giữ được nhân vật nhất quán giữa các lần sinh. Cần nhân vật nhất quán thì vẫn
phải dùng Nano Banana hoặc Characters trong Flow.

    python generate_image_cf.py --prompt "a quiet Hanoi alley at dawn" --ra anh.jpg
    python generate_image_cf.py --prompt "..." --so 4 --steps 8 --seed 42
"""

from __future__ import annotations

import argparse
import base64
import binascii
import json
import sys
from pathlib import Path

import requests

import config

TIMEOUT = 180
GIOI_HAN_PROMPT = 2048


def sinh_mot(acc: str, tok: str, prompt: str, steps: int, seed: int | None) -> bytes:
    url = config.CF_BASE.format(acc=acc) + config.CF_IMAGE_MODEL
    than = {"prompt": prompt, "steps": steps}
    if seed is not None:
        than["seed"] = seed

    r = requests.post(
        url,
        headers={"Authorization": f"Bearer {tok}", "Content-Type": "application/json"},
        json=than,
        timeout=TIMEOUT,
    )

    if r.status_code == 401 or r.status_code == 403:
        sys.exit(
            "❌ Cloudflare từ chối xác thực. Kiểm tra CLOUDFLARE_API_TOKEN có "
            "quyền Workers AI, và CLOUDFLARE_ACCOUNT_ID đúng tài khoản."
        )
    if r.status_code == 429:
        sys.exit(
            "❌ Hết quota Neuron trong ngày (bậc miễn phí 10.000 Neuron, reset "
            "00:00 UTC). Đợi sang ngày mới hoặc dùng Nano Banana."
        )
    if not r.ok:
        sys.exit(f"❌ Cloudflare trả {r.status_code}: {r.text[:400]}")

    try:
        d = r.json()
    except json.JSONDecodeError:
        sys.exit(f"❌ Không phải JSON. 300 ký tự đầu: {r.text[:300]}")

    # Cloudflare bọc kết quả trong {"result": {...}, "success": true, ...}
    if isinstance(d, dict) and "result" in d:
        if d.get("success") is False:
            sys.exit(f"❌ Cloudflare báo lỗi: {d.get('errors')}")
        d = d["result"]

    b64 = d.get("image") if isinstance(d, dict) else None
    if not b64:
        sys.exit(f"❌ Response không có trường 'image'. Các khoá: {list(d) if isinstance(d, dict) else type(d)}")

    try:
        return base64.b64decode(b64)
    except (binascii.Error, ValueError) as e:
        sys.exit(f"❌ Giải mã base64 hỏng: {e}")


def main() -> int:
    p = argparse.ArgumentParser(description="Sinh anh bang Cloudflare Workers AI, bac mien phi")
    p.add_argument("--prompt", required=True, help=f"mo ta anh, toi da {GIOI_HAN_PROMPT} ky tu")
    p.add_argument("--ra", default="cf-image.jpg", help="duong dan file ra (.jpg)")
    p.add_argument("--so", type=int, default=1, help="sinh may anh, moi anh mot lan goi")
    p.add_argument("--steps", type=int, default=4, help=f"so buoc, toi da {config.CF_STEPS_MAX}")
    p.add_argument("--seed", type=int, default=None, help="co dinh seed de lap lai duoc")
    d = p.parse_args()

    if len(d.prompt) > GIOI_HAN_PROMPT:
        p.error(f"prompt dai {len(d.prompt)} ky tu, vuot gioi han {GIOI_HAN_PROMPT} cua model")
    if not 1 <= d.steps <= config.CF_STEPS_MAX:
        p.error(f"steps phai trong khoang 1 toi {config.CF_STEPS_MAX}")
    if d.so < 1:
        p.error("--so phai tu 1 tro len")

    acc, tok = config.get_cloudflare()
    goc = Path(d.ra)

    for i in range(d.so):
        # Seed cố định mà sinh nhiều ảnh thì mọi ảnh sẽ giống hệt nhau, nên
        # cộng thêm chỉ số để mỗi ảnh vẫn khác nhau mà vẫn lặp lại được.
        seed = None if d.seed is None else d.seed + i
        anh = sinh_mot(acc, tok, d.prompt, d.steps, seed)
        dich = goc if d.so == 1 else goc.with_name(f"{goc.stem}-{i + 1}{goc.suffix}")
        dich.parent.mkdir(parents=True, exist_ok=True)
        dich.write_bytes(anh)
        # Model trả JPEG bất kể đuôi file người dùng đặt, nên nói rõ ra.
        print(f"✅ {dich}  ({len(anh) / 1024:.0f} KB, định dạng JPEG)")

    if goc.suffix.lower() not in (".jpg", ".jpeg"):
        print(
            f"\n⚠ Bạn đặt đuôi '{goc.suffix}' nhưng model luôn trả JPEG. "
            "Nội dung file là JPEG, chỉ tên gọi là sai."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
