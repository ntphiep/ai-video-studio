#!/usr/bin/env python3
"""Sinh giọng đọc miễn phí bằng edge-tts, có giọng tiếng Việt.

Vì sao cần: Gemini TTS tốn quota. Với bản nháp để canh nhịp, để đo độ dài lời
đọc trước khi dựng hình, hoặc cho video không đòi giọng cao cấp, edge-tts đủ
dùng và không tốn đồng nào.

CẢNH BÁO trước khi dựa vào nó để kiếm tiền: edge-tts KHÔNG phải API chính thức
của Microsoft. Nó là bản dịch ngược dịch vụ Read Aloud của trình duyệt Edge,
nên Microsoft có thể đổi hoặc chặn bất cứ lúc nào mà không báo trước. Dùng cho
bản nháp thì rất tiện; đưa vào quy trình sản xuất chính thì nên coi Gemini TTS
là đường chính và edge-tts là đường dự phòng.

Cài trước khi dùng:  pip install edge-tts

Script cố ý KHÔNG nhúng cứng tên giọng. Tên giọng của Microsoft có đổi theo
thời gian, nên script luôn hỏi danh sách trực tiếp rồi mới chọn.

    python generate_audio_edge.py --liet-ke-giong
    python generate_audio_edge.py --text "Xin chào" --ra loi.mp3
    python generate_audio_edge.py --file kich-ban.txt --giong vi-VN-HoaiMyNeural --toc-do +10%
"""

from __future__ import annotations

import argparse
import asyncio
import sys
from pathlib import Path

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
# Script này không import config nên phải tự ép UTF-8.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# Import mềm: để `--help` vẫn chạy được trên máy chưa cài edge-tts, giống
# mọi script khác trong thư mục này.
try:
    import edge_tts
except ImportError:
    edge_tts = None

NGON_NGU_MAC_DINH = "vi-VN"


def _bat_buoc_co_edge_tts() -> None:
    if edge_tts is None:
        sys.exit(
            "❌ Chưa cài edge-tts. Chạy:  pip install edge-tts\n"
            "   Nếu không muốn cài thêm gói, dùng generate_audio.py (Gemini TTS)."
        )


async def _lay_giong(tien_to: str) -> list[dict]:
    tat_ca = await edge_tts.list_voices()
    return sorted(
        (v for v in tat_ca if v.get("ShortName", "").startswith(tien_to)),
        key=lambda v: v["ShortName"],
    )


async def _doc(text: str, giong: str, toc_do: str, cao_do: str, ra: Path) -> None:
    tt = edge_tts.Communicate(text, giong, rate=toc_do, pitch=cao_do)
    ra.parent.mkdir(parents=True, exist_ok=True)
    await tt.save(str(ra))


def main() -> int:
    p = argparse.ArgumentParser(description="Sinh giong doc mien phi bang edge-tts")
    p.add_argument("--text", help="noi dung can doc")
    p.add_argument("--file", help="doc noi dung tu file .txt thay vi --text")
    p.add_argument("--ra", default="loi-doc.mp3", help="file mp3 dau ra")
    p.add_argument("--giong", default=None, help="ten giong, vd vi-VN-HoaiMyNeural")
    p.add_argument("--ngon-ngu", default=NGON_NGU_MAC_DINH, help="tien to loc giong, vd vi-VN")
    p.add_argument("--toc-do", default="+0%", help="vd +10%% nhanh hon, -10%% cham hon")
    p.add_argument("--cao-do", default="+0Hz", help="vd +5Hz cao hon")
    p.add_argument("--liet-ke-giong", action="store_true", help="in cac giong co san roi thoat")
    d = p.parse_args()

    _bat_buoc_co_edge_tts()

    if d.liet_ke_giong:
        ds = asyncio.run(_lay_giong(d.ngon_ngu))
        if not ds:
            print(f"Không có giọng nào cho '{d.ngon_ngu}'. Thử --ngon-ngu en-US.")
            return 1
        print(f"Giọng có sẵn cho {d.ngon_ngu}:\n")
        for v in ds:
            print(f"  {v['ShortName']:32} {v.get('Gender', '?'):7} {v.get('FriendlyName', '')}")
        return 0

    if not d.text and not d.file:
        p.error("can --text hoac --file")
    if d.text and d.file:
        p.error("chi dung mot trong hai: --text hoac --file")

    if d.file:
        f = Path(d.file)
        if not f.exists():
            sys.exit(f"❌ Không thấy file: {f}")
        noi_dung = f.read_text(encoding="utf-8").strip()
    else:
        noi_dung = d.text.strip()

    if not noi_dung:
        sys.exit("❌ Nội dung rỗng, không có gì để đọc.")

    giong = d.giong
    if not giong:
        ds = asyncio.run(_lay_giong(d.ngon_ngu))
        if not ds:
            sys.exit(
                f"❌ Không có giọng nào cho '{d.ngon_ngu}'. "
                "Chạy --liet-ke-giong để xem danh sách."
            )
        giong = ds[0]["ShortName"]
        print(f"Không chỉ định giọng, tự chọn: {giong}")

    ra = Path(d.ra)
    try:
        asyncio.run(_doc(noi_dung, giong, d.toc_do, d.cao_do, ra))
    except Exception as e:
        sys.exit(
            f"❌ edge-tts hỏng: {e}\n"
            "   Nhớ rằng đây là dịch vụ không chính thức, Microsoft có thể đã đổi. "
            "Dùng generate_audio.py (Gemini TTS) nếu cần đường ổn định."
        )

    if not ra.exists() or ra.stat().st_size == 0:
        sys.exit("❌ Chạy xong nhưng file rỗng. Nhiều khả năng dịch vụ đã từ chối.")

    print(f"✅ {ra}  ({ra.stat().st_size / 1024:.0f} KB, giọng {giong})")
    print(f"   {len(noi_dung.split())} từ. Đo độ dài thật bằng: ffprobe -i {ra}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
