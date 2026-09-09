#!/usr/bin/env python3
"""Chấm video đã render bằng SỐ ĐO KHÁCH QUAN, không bằng cảm tính.

Vì sao viết cái này thay vì bê `/review-video` của remotion-superpowers về:
đọc mã nguồn repo đó ngày 09/09/2026 thì thấy nó là 145 dòng văn xuôi, không có
dòng code thực thi nào, không có bộ đếm vòng, không có ngưỡng dừng, và con số
"Overall Score 1-10" trong mẫu báo cáo không được định nghĩa ở bất kỳ đâu. Nó
còn cần TwelveLabs, một API trả phí. Nói cách khác, model tự nghĩ ra điểm.

Script này đi hướng ngược lại: chỉ báo những gì `ffmpeg` và `ffprobe` đo được,
kèm con số thật, để người đọc tự phán. Không có điểm tổng, vì một con số gộp
che mất thứ đang thật sự sai.

Không gọi API, không tốn credit, không cần tài khoản nào.

    python review_video.py video.mp4
    python review_video.py video.mp4 --nen-tang tiktok
    python review_video.py video.mp4 --json
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

# Ngưỡng và nguồn của từng ngưỡng. Cái nào chưa tìm được trang chính thức thì
# ghi rõ, đừng để người đọc tưởng mọi con số đều có căn cứ như nhau.
NGUONG = {
    "lufs_muc_tieu": -14.0,
    "lufs_sai_so": 2.0,
    "lufs_nguon": "[chưa xác minh] Mức -14 LUFS được nhắc rộng rãi trong giới "
                  "làm video là mốc chuẩn hoá của YouTube, nhưng tôi chưa tìm "
                  "được trang hỗ trợ chính thức nào của Google công bố con số "
                  "này. Coi là mốc tham khảo, không phải quy định.",
    "dung_hinh_giay": 2.0,
    "dung_hinh_ty_le_canh_bao": 30.0,
    "dung_hinh_nguon": "Ngưỡng tự đặt dựa trên số đo trong chính skill này: một "
                       "bản dựng bị chê giống slide có tỉ lệ khung đứng yên 77,3%, "
                       "bản sửa xong còn 17,0%. Lấy 30% làm mốc cảnh báo.",
    "lech_tieng_hinh_giay": 0.5,
    "den_giay": 0.5,
}

NEN_TANG = {
    "youtube":  {"ty_le": (16, 9), "fps_toi_thieu": 24, "chieu_cao_toi_thieu": 720},
    "shorts":   {"ty_le": (9, 16), "fps_toi_thieu": 24, "chieu_cao_toi_thieu": 1080},
    "tiktok":   {"ty_le": (9, 16), "fps_toi_thieu": 24, "chieu_cao_toi_thieu": 1080},
    "reels":    {"ty_le": (9, 16), "fps_toi_thieu": 24, "chieu_cao_toi_thieu": 1080},
}


def _chay(lenh: list[str]) -> str:
    """Chạy lệnh, trả toàn bộ stdout cộng stderr. ffmpeg in số đo ra stderr."""
    p = subprocess.run(lenh, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return (p.stdout or "") + (p.stderr or "")


def doc_luong(f: Path) -> dict:
    ra = _chay([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_streams", "-show_format", str(f),
    ])
    try:
        d = json.loads(ra)
    except json.JSONDecodeError:
        sys.exit(f"❌ ffprobe không đọc được file: {ra[:300]}")
    hinh = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), None)
    tieng = next((s for s in d.get("streams", []) if s.get("codec_type") == "audio"), None)
    return {"hinh": hinh, "tieng": tieng, "format": d.get("format", {})}


def _fps(s: dict) -> float:
    raw = s.get("r_frame_rate") or "0/1"
    try:
        a, b = raw.split("/")
        return float(a) / float(b) if float(b) else 0.0
    except (ValueError, ZeroDivisionError):
        return 0.0


def do_mot_luot(f: Path) -> dict:
    """Một lần chạy ffmpeg, lấy cùng lúc độ ồn, khung đen và đoạn đứng hình."""
    ra = _chay([
        "ffmpeg", "-hide_banner", "-nostats", "-i", str(f),
        "-vf", f"blackdetect=d={NGUONG['den_giay']}:pic_th=0.98,"
               f"freezedetect=n=0.003:d={NGUONG['dung_hinh_giay']}",
        "-af", "ebur128=peak=true",
        "-f", "null", "-",
    ])

    lufs = None
    m = re.search(r"Integrated loudness:\s*\n\s*I:\s*(-?[\d.]+)\s*LUFS", ra)
    if m:
        lufs = float(m.group(1))
    lra = None
    m = re.search(r"LRA:\s*(-?[\d.]+)\s*LU", ra)
    if m:
        lra = float(m.group(1))

    # Chú ý: dùng lớp ký tự POSIX. Viết \d trong grep -E là hỏng thầm lặng,
    # đã mắc một lần rồi.
    dung = [float(x) for x in re.findall(r"freeze_duration:\s*([0-9.]+)", ra)]
    den = [float(x) for x in re.findall(r"black_duration:\s*([0-9.]+)", ra)]
    return {"lufs": lufs, "lra": lra, "dung_hinh": dung, "den": den}


def cham(f: Path, nen_tang: str | None) -> list[dict]:
    l = doc_luong(f)
    if not l["hinh"]:
        sys.exit("❌ File không có luồng hình.")
    d = do_mot_luot(f)

    hinh, tieng = l["hinh"], l["tieng"]
    dai = float(l["format"].get("duration") or hinh.get("duration") or 0)
    kq: list[dict] = []

    def them(ten, muc, so_do, ghi_chu=""):
        kq.append({"ten": ten, "muc": muc, "so_do": so_do, "ghi_chu": ghi_chu})

    # 1. Độ ồn
    if d["lufs"] is None:
        them("Độ ồn", "KHONG DO DUOC", "-", "Không có tiếng, hoặc ffmpeg không trả ebur128")
    else:
        lech = d["lufs"] - NGUONG["lufs_muc_tieu"]
        muc = "DAT" if abs(lech) <= NGUONG["lufs_sai_so"] else "LUU Y"
        huong = "to hơn" if lech > 0 else "nhỏ hơn"
        them("Độ ồn", muc, f"{d['lufs']:.1f} LUFS",
             f"lệch {abs(lech):.1f} LU so với mốc {NGUONG['lufs_muc_tieu']}, tức {huong}")

    # 2. Đứng hình. Đây là thước đo "trông có giống slide không".
    tong_dung = sum(d["dung_hinh"])
    ty_le = 100 * tong_dung / dai if dai else 0
    muc = "LUU Y" if ty_le >= NGUONG["dung_hinh_ty_le_canh_bao"] else "DAT"
    them("Đứng hình", muc, f"{ty_le:.1f}% thời lượng",
         f"{len(d['dung_hinh'])} đoạn dài từ {NGUONG['dung_hinh_giay']}s, "
         f"tổng {tong_dung:.1f}s trên {dai:.0f}s"
         + (f", đoạn dài nhất {max(d['dung_hinh']):.1f}s" if d["dung_hinh"] else ""))

    # 3. Khung đen
    them("Khung đen", "LUU Y" if d["den"] else "DAT",
         f"{len(d['den'])} đoạn",
         f"tổng {sum(d['den']):.1f}s" if d["den"] else "không có đoạn đen nào")

    # 4. Lệch hình và tiếng
    if tieng:
        dh = float(hinh.get("duration") or 0)
        dt = float(tieng.get("duration") or 0)
        lech = abs(dh - dt)
        them("Lệch hình tiếng", "LUU Y" if lech > NGUONG["lech_tieng_hinh_giay"] else "DAT",
             f"{lech * 1000:.0f} ms", f"hình {dh:.2f}s, tiếng {dt:.2f}s")
    else:
        them("Tiếng", "LUU Y", "không có", "Video không có luồng âm thanh")

    # 5. Thông số kỹ thuật
    w, h = hinh.get("width", 0), hinh.get("height", 0)
    fps = _fps(hinh)
    them("Kỹ thuật", "DAT", f"{w}x{h}, {fps:.0f}fps, {hinh.get('codec_name')}",
         f"{dai:.1f}s, {Path(f).stat().st_size / 1048576:.1f} MB")

    # 6. Khớp nền tảng, chỉ kiểm khi người dùng nói rõ định đăng đâu
    if nen_tang:
        spec = NEN_TANG[nen_tang]
        loi = []
        if h and w:
            mong_muon = spec["ty_le"][0] / spec["ty_le"][1]
            that = w / h
            if abs(that - mong_muon) > 0.02:
                loi.append(f"tỉ lệ {w}:{h} không phải {spec['ty_le'][0]}:{spec['ty_le'][1]}")
        if h < spec["chieu_cao_toi_thieu"]:
            loi.append(f"chiều cao {h} dưới mức nên có {spec['chieu_cao_toi_thieu']}")
        if fps and fps < spec["fps_toi_thieu"]:
            loi.append(f"{fps:.0f}fps dưới mức nên có {spec['fps_toi_thieu']}")
        them(f"Hợp {nen_tang}", "LUU Y" if loi else "DAT",
             "không khớp" if loi else "khớp", "; ".join(loi))
    return kq


def main() -> int:
    p = argparse.ArgumentParser(description="Cham video bang so do khach quan, khong goi API")
    p.add_argument("video", help="duong dan file video")
    p.add_argument("--nen-tang", choices=sorted(NEN_TANG), default=None,
                   help="kiem them cho dung chuan nen tang dinh dang")
    p.add_argument("--json", action="store_true", help="in JSON de script khac doc")
    d = p.parse_args()

    for lenh in ("ffmpeg", "ffprobe"):
        if not shutil.which(lenh):
            sys.exit(f"❌ Thiếu {lenh}. Chạy doctor.py để biết cách cài.")

    f = Path(d.video)
    if not f.exists():
        sys.exit(f"❌ Không thấy file: {f}")

    kq = cham(f, d.nen_tang)

    if d.json:
        print(json.dumps({"file": str(f), "ket_qua": kq}, ensure_ascii=False, indent=2))
        return 0

    print(f"\nChấm {f.name}\n")
    for r in kq:
        dau = {"DAT": "  ok  ", "LUU Y": " lưu ý", "KHONG DO DUOC": "  ?   "}.get(r["muc"], "      ")
        print(f"[{dau}] {r['ten']:18} {r['so_do']}")
        if r["ghi_chu"]:
            print(f"           {r['ghi_chu']}")

    luu_y = [r for r in kq if r["muc"] == "LUU Y"]
    print(f"\n{len(kq) - len(luu_y)} mục ổn, {len(luu_y)} mục cần xem lại.")
    print("\nKhông có điểm tổng, vì gộp thành một con số sẽ che mất thứ đang sai.")
    print(f"Về mốc độ ồn: {NGUONG['lufs_nguon']}")
    # Thoát 0 kể cả khi có lưu ý: đây là báo cáo cho người đọc, không phải cổng
    # chặn CI. Muốn dùng làm cổng chặn thì đọc --json rồi tự quyết.
    return 0


if __name__ == "__main__":
    sys.exit(main())
