#!/usr/bin/env python3
"""Tải ảnh và video stock miễn phí từ Pexels, dùng làm B-roll.

Vì sao cần: mỗi clip sinh bằng Veo đều tốn credit. Rất nhiều cảnh trong một
video không cần nhân vật nhất quán, chỉ cần cảnh minh hoạ chung (thành phố,
bàn phím, biển, người đi bộ). Với những cảnh đó, lấy stock rẻ hơn hẳn và
chất lượng thường cao hơn clip sinh 8 giây.

Giấy phép: Pexels cho dùng thương mại và KHÔNG bắt buộc ghi công. Vẫn nên ghi
tên tác giả nếu tiện, script in sẵn dòng ghi công cho từng file tải về.
Nguồn: https://www.pexels.com/license/

Rate limit công bố: 200 request/giờ và 20.000/tháng.
Nguồn: https://www.pexels.com/api/documentation/ đọc 09/09/2026.

Vì sao chưa có Pixabay: đã thử đọc https://pixabay.com/api/docs/ hai lần bằng hai
cách khác nhau vào 09/09/2026, cả hai đều bị trả HTTP 429. Không đọc được hợp
đồng API thì không viết code theo trí nhớ. Ai mở được trang đó thì bổ sung sau,
cấu trúc script này đã tách sẵn phần tìm kiếm theo từng nguồn.

    python fetch_stock.py --query "hanoi street food" --loai video --so 3
    python fetch_stock.py --query "keyboard closeup" --loai anh --huong landscape
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import requests

import config

TIMEOUT = 60


def _ten_file_an_toan(s: str, toi_da: int = 60) -> str:
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE).strip()
    s = re.sub(r"[\s_]+", "-", s).lower()
    return s[:toi_da] or "stock"


def _goi(url: str, key: str, tham_so: dict) -> dict:
    r = requests.get(url, headers={"Authorization": key}, params=tham_so, timeout=TIMEOUT)
    if r.status_code == 401:
        sys.exit("❌ Pexels từ chối key. Kiểm tra lại PEXELS_API_KEY.")
    if r.status_code == 429:
        con_lai = r.headers.get("X-Ratelimit-Remaining", "?")
        sys.exit(
            f"❌ Chạm rate limit Pexels ({config.PEXELS_RATE}). "
            f"Còn lại theo header: {con_lai}. Đợi rồi chạy lại."
        )
    r.raise_for_status()
    return r.json()


def _tai(url: str, dich: Path) -> int:
    with requests.get(url, stream=True, timeout=TIMEOUT) as r:
        r.raise_for_status()
        dich.parent.mkdir(parents=True, exist_ok=True)
        n = 0
        with open(dich, "wb") as f:
            for khoi in r.iter_content(1 << 16):
                f.write(khoi)
                n += len(khoi)
    return n


def _chon_file_video(video: dict) -> dict | None:
    """Chọn bản mp4 có độ phân giải cao nhất trong danh sách video_files."""
    ung_vien = [
        f for f in video.get("video_files", [])
        if f.get("file_type") == "video/mp4" and f.get("link")
    ]
    if not ung_vien:
        return None
    return max(ung_vien, key=lambda f: (f.get("width") or 0) * (f.get("height") or 0))


def tim_anh(key: str, doi_so) -> list[dict]:
    tham_so = {"query": doi_so.query, "per_page": doi_so.so, "page": doi_so.trang}
    if doi_so.huong:
        tham_so["orientation"] = doi_so.huong
    if doi_so.co:
        tham_so["size"] = doi_so.co
    d = _goi(config.PEXELS_PHOTO, key, tham_so)
    ket = []
    for a in d.get("photos", []):
        ket.append(
            {
                "id": a["id"],
                "tac_gia": a.get("photographer", "?"),
                "trang": a.get("url", ""),
                "link": a["src"]["original"],
                "rong": a.get("width"),
                "cao": a.get("height"),
                "duoi": ".jpg",
            }
        )
    return ket


def tim_video(key: str, doi_so) -> list[dict]:
    tham_so = {"query": doi_so.query, "per_page": doi_so.so, "page": doi_so.trang}
    if doi_so.huong:
        tham_so["orientation"] = doi_so.huong
    if doi_so.co:
        tham_so["size"] = doi_so.co
    d = _goi(config.PEXELS_VIDEO, key, tham_so)
    ket = []
    for v in d.get("videos", []):
        f = _chon_file_video(v)
        if not f:
            continue
        ket.append(
            {
                "id": v["id"],
                "tac_gia": (v.get("user") or {}).get("name", "?"),
                "trang": v.get("url", ""),
                "link": f["link"],
                "rong": f.get("width"),
                "cao": f.get("height"),
                "giay": v.get("duration"),
                "duoi": ".mp4",
            }
        )
    return ket


def main() -> int:
    p = argparse.ArgumentParser(description="Tai anh va video stock mien phi tu Pexels")
    p.add_argument("--query", required=True, help="tu khoa tim kiem, nen viet tieng Anh")
    p.add_argument("--loai", choices=["anh", "video"], default="video")
    p.add_argument("--so", type=int, default=5, help="so ket qua, toi da 80")
    p.add_argument("--trang", type=int, default=1)
    p.add_argument("--huong", choices=["landscape", "portrait", "square"], default=None)
    p.add_argument("--co", choices=["large", "medium", "small"], default=None)
    p.add_argument("--ra", default="stock", help="thu muc luu")
    p.add_argument("--chi-liet-ke", action="store_true", help="chi in ket qua, khong tai")
    d = p.parse_args()

    if d.so > 80:
        p.error("Pexels cho toi da 80 ket qua moi trang (per_page)")

    key = config.get_pexels_key()
    ket = tim_anh(key, d) if d.loai == "anh" else tim_video(key, d)

    if not ket:
        print(f"Không tìm thấy kết quả nào cho: {d.query}")
        return 1

    print(f"Tìm thấy {len(ket)} kết quả cho \"{d.query}\":\n")
    thu_muc = Path(d.ra)
    ghi_cong = []
    for i, m in enumerate(ket, start=1):
        kich_thuoc = f"{m['rong']}x{m['cao']}"
        them = f", {m['giay']}s" if m.get("giay") else ""
        print(f"  {i}. #{m['id']}  {kich_thuoc}{them}  — {m['tac_gia']}")
        if d.chi_liet_ke:
            continue
        ten = f"{_ten_file_an_toan(d.query)}-{m['id']}{m['duoi']}"
        dich = thu_muc / ten
        try:
            n = _tai(m["link"], dich)
        except Exception as e:
            print(f"     tải hỏng: {e}")
            continue
        print(f"     đã lưu {dich}  ({n / 1048576:.2f} MB)")
        ghi_cong.append(f"{ten}: ảnh/video của {m['tac_gia']} trên Pexels — {m['trang']}")

    if ghi_cong:
        f = thu_muc / "GHI-CONG.txt"
        f.write_text(
            "Pexels không bắt buộc ghi công, nhưng nên ghi nếu tiện.\n\n"
            + "\n".join(ghi_cong)
            + "\n",
            encoding="utf-8",
        )
        print(f"\nĐã ghi danh sách tác giả vào {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
