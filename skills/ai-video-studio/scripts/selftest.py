#!/usr/bin/env python3
"""Tự kiểm phần logic dễ vỡ của skill, chạy hoàn toàn offline.

Vì sao cần: những chỗ dễ sai nhất trong skill này đều là chỗ KHÔNG gọi API thật
nên không ai thử, mà khi hỏng thì hỏng đắt. Cụ thể là vòng chờ operation sinh
video: credit đã bị trừ ngay khi operation được tạo, nên một lỗi mạng thoáng qua
mà làm script thoát sớm là mất trắng clip đã trả tiền.

Test ở đây KHÔNG gọi mạng, không tốn credit, chạy trong một giây. Chạy nó sau
mỗi lần sửa `generate_video.py`.

    python selftest.py
    python selftest.py -v     # in chi tiết từng bước

Đây là test logic offline, không thay thế việc gọi API thật một lần để xác minh
schema. Xem evals/evals.json cho phần kiểm chứng có gọi thật.
"""

from __future__ import annotations

import argparse
import io
import sys
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

import generate_video as gv

_LOI: list[str] = []
_DAT = 0


def kiem(ten: str, dieu_kien: bool, chi_tiet: str = "") -> None:
    global _DAT
    if dieu_kien:
        _DAT += 1
        print(f"  ĐẠT   {ten}")
    else:
        _LOI.append(f"{ten} — {chi_tiet}")
        print(f"  HỎNG  {ten}   {chi_tiet}")


def _chay_im(ham, *a, **kw):
    """Chạy hàm, nuốt output, trả (ket_qua, van_ban_da_in)."""
    b = io.StringIO()
    with redirect_stdout(b):
        kq = ham(*a, **kw)
    return kq, b.getvalue()


def test_poll(chi_tiet: bool) -> None:
    print("\nVòng chờ operation sinh video (poll_operation)")
    that = gv._get
    ngu = gv.time.sleep
    gv.time.sleep = lambda s: None  # khỏi chờ thật
    try:
        # 1. Sống sót qua mất mạng rồi lỗi 5xx, cuối cùng vẫn lấy được clip.
        kich_ban = [
            (0, {"error": {"message": "getaddrinfo failed"}}),
            (0, {"error": {"message": "getaddrinfo failed"}}),
            (500, {"error": {"message": "backend hiccup"}}),
            (200, {"done": False}),
            (200, {"done": True, "response": {"video": {"uri": "http://x/v.mp4"}}}),
        ]
        dem = {"i": 0}

        def theo_kich_ban(url):
            k = kich_ban[min(dem["i"], len(kich_ban) - 1)]
            dem["i"] += 1
            return k

        gv._get = theo_kich_ban
        (st, body), _ = _chay_im(gv.poll_operation, "operations/a", "K", timeout=600)
        kiem(
            "sống sót qua 2 lần mất mạng và 1 lỗi 500",
            st == 200 and body.get("done") is True,
            f"nhận status={st}",
        )

        # 2. Lỗi mạng liên tục thì phải đầu hàng, không lặp vô tận.
        gv._get = lambda url: (0, {"error": {"message": "mất mạng mãi"}})
        (st, _b), _ = _chay_im(gv.poll_operation, "operations/a", "K", timeout=600)
        kiem("đầu hàng sau khi lỗi mạng lặp quá ngưỡng", st in (0, 504), f"status={st}")

        # 3. Lỗi 400 là sai payload, thử lại vô ích nên phải dừng ngay.
        d2 = {"n": 0}

        def loi400(url):
            d2["n"] += 1
            return 400, {"error": {"message": "sai payload"}}

        gv._get = loi400
        (st, _b), _ = _chay_im(gv.poll_operation, "operations/a", "K", timeout=600)
        kiem("lỗi 400 dừng ngay sau đúng 1 lần gọi", st == 400 and d2["n"] == 1,
             f"status={st}, gọi {d2['n']} lần")

        # 4. Hết giờ phải trả lại operation name, vì clip đã bị tính tiền rồi.
        gv._get = lambda url: (200, {"done": False})
        (st, body), _ = _chay_im(gv.poll_operation, "operations/xyz", "K", timeout=0.001)
        msg = (body.get("error") or {}).get("message", "")
        kiem("hết giờ vẫn trả operation name để hỏi lại", st == 504 and "operations/xyz" in msg,
             f"status={st}, thông báo: {msg[:60]}")
    finally:
        gv._get = that
        gv.time.sleep = ngu


def test_get_khong_nem() -> None:
    print("\nHàm _get không bao giờ được ném ngoại lệ")
    that = gv.urllib.request.urlopen

    def no_tung(*a, **kw):
        raise gv.urllib.error.URLError("mạng chết")

    gv.urllib.request.urlopen = no_tung
    try:
        st, body = gv._get("https://khong-ton-tai.invalid/x")
        kiem("lỗi mạng trả status 0 thay vì ném", st == 0, f"status={st}")
        kiem("kèm thông báo đọc được", bool((body.get("error") or {}).get("message")))
    except Exception as e:
        kiem("lỗi mạng trả status 0 thay vì ném", False, f"đã ném {type(e).__name__}: {e}")
    finally:
        gv.urllib.request.urlopen = that


def test_retry_delay() -> None:
    print("\nĐọc retryDelay theo chuẩn RetryInfo của Google")
    kiem(
        "đọc được '27s' thành 27.0",
        gv._retry_delay(
            {"error": {"details": [
                {"@type": "type.googleapis.com/google.rpc.RetryInfo", "retryDelay": "27s"}
            ]}}
        ) == 27.0,
    )
    kiem("không có details thì trả None", gv._retry_delay({"error": {}}) is None)
    kiem("giá trị rác thì trả None chứ không nổ",
         gv._retry_delay({"error": {"details": [{"retryDelay": "abc"}]}}) is None)


def main() -> int:
    p = argparse.ArgumentParser(description="Tu kiem logic offline cua skill")
    p.add_argument("-v", "--verbose", action="store_true")
    d = p.parse_args()

    print("Tự kiểm ai-video-studio (offline, không tốn credit)")
    test_poll(d.verbose)
    test_get_khong_nem()
    test_retry_delay()

    print(f"\n{_DAT} đạt, {len(_LOI)} hỏng")
    if _LOI:
        print("\nCác mục hỏng:")
        for l in _LOI:
            print(f"  - {l}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
