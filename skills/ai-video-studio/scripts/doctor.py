"""Kiểm tra môi trường trước khi dùng skill ai-video-studio.

Chạy trước tiên trên một máy mới. Nó nói rõ cái gì có, cái gì thiếu, và thiếu thì
cài bằng lệnh nào, thay vì để người dùng gặp lỗi giữa chừng.

Cách dùng:
  python doctor.py
  python doctor.py --json     (xuất JSON cho máy đọc)

Mã thoát: 0 nếu đủ điều kiện chạy đường API, 1 nếu thiếu thứ bắt buộc.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

CAI_DAT = {
    "ffmpeg": {
        "win32": "winget install Gyan.FFmpeg",
        "darwin": "brew install ffmpeg",
        "linux": "sudo apt install ffmpeg",
    },
    "yt-dlp": {
        "win32": "pip install -U yt-dlp",
        "darwin": "brew install yt-dlp",
        "linux": "pip install -U yt-dlp",
    },
    "node": {
        "win32": "winget install OpenJS.NodeJS.LTS",
        "darwin": "brew install node",
        "linux": "sudo apt install nodejs npm",
    },
}


def lenh_cai(ten):
    return CAI_DAT.get(ten, {}).get(sys.platform, f"tự cài {ten}")


def kiem_lenh(ten, bat_buoc, mo_ta, co_version=True):
    duong_dan = shutil.which(ten)
    ket = {"ten": ten, "bat_buoc": bat_buoc, "mo_ta": mo_ta,
           "co": bool(duong_dan), "duong_dan": duong_dan, "version": None}
    if duong_dan and co_version:
        for co in (["--version"], ["-version"], ["version"]):
            try:
                out = subprocess.run([duong_dan] + co, capture_output=True,
                                     text=True, timeout=20)
                dong = (out.stdout or out.stderr).strip().split("\n")[0]
                if dong:
                    ket["version"] = dong[:80]
                    break
            except Exception:
                continue
    if not duong_dan:
        ket["cach_cai"] = lenh_cai(ten)
    return ket


def kiem_key(ten_env, ten_file, mo_ta, cach_lay, bat_buoc=True):
    """Kiểm một API key: có trong env chưa, hay có file ở thư mục home chưa."""
    ket = {"ten": ten_env, "bat_buoc": bat_buoc, "mo_ta": mo_ta,
           "co": False, "duong_dan": None, "version": None}
    if os.environ.get(ten_env):
        ket["co"] = True
        ket["duong_dan"] = f"biến môi trường {ten_env}"
    else:
        f = Path.home() / ten_file
        if f.exists() and f.read_text(encoding="utf-8").strip():
            ket["co"] = True
            ket["duong_dan"] = str(f)
    if not ket["co"]:
        ket["cach_cai"] = cach_lay
    return ket


def kiem_api_key():
    return kiem_key(
        "GEMINI_API_KEY", ".gemini_key",
        "Khoá gọi Gemini API, cần cho đường B",
        "Lấy khoá tại https://aistudio.google.com/apikey rồi đặt "
        "biến môi trường GEMINI_API_KEY, hoặc ghi vào file ~/.gemini_key",
    )


def kiem_goi_python(ten_goi, mo_ta, cach_cai):
    """Kiểm một gói Python tuỳ chọn đã cài chưa, không import thật để khỏi chậm."""
    import importlib.util
    co = importlib.util.find_spec(ten_goi) is not None
    ket = {"ten": ten_goi, "bat_buoc": False, "mo_ta": mo_ta,
           "co": co, "duong_dan": None, "version": None}
    if not co:
        ket["cach_cai"] = cach_cai
    return ket


def kiem_python():
    v = sys.version_info
    du = v >= (3, 9)
    return {"ten": "python", "bat_buoc": True,
            "mo_ta": "Python 3.9 trở lên để chạy các script",
            "co": du, "duong_dan": sys.executable,
            "version": f"{v.major}.{v.minor}.{v.micro}",
            **({} if du else {"cach_cai": "Nâng lên Python 3.9 trở lên"})}


def chay():
    kq = [
        kiem_python(),
        kiem_api_key(),
        kiem_lenh("ffmpeg", True, "Ghép, đổi tỉ lệ, xuất video"),
        kiem_lenh("ffprobe", True, "Đo kích thước và thời lượng, dùng để tự kiểm chứng"),
        kiem_lenh("node", False, "Cần cho đường D, tức Remotion"),
        kiem_lenh("npx", False, "Cần cho đường D, tức Remotion", co_version=False),
        kiem_lenh("yt-dlp", False, "Chỉ cần khi muốn tải video tham khảo về học"),
        kiem_lenh("curl", False, "Tải file từ URL ký tên của Flow"),
        # Ba đường miễn phí dưới đây đều tuỳ chọn. Thiếu chúng thì skill vẫn
        # chạy đủ, chỉ là mọi thứ đều tính vào quota Google.
        kiem_key(
            "PEXELS_API_KEY", ".pexels_key",
            "Tuỳ chọn. Tải ảnh và video stock miễn phí làm B-roll, đỡ tốn credit Veo",
            "Đăng ký miễn phí tại https://www.pexels.com/api/ rồi đặt biến môi "
            "trường PEXELS_API_KEY, hoặc ghi vào file ~/.pexels_key",
            bat_buoc=False,
        ),
        kiem_key(
            "CLOUDFLARE_ACCOUNT_ID", ".cloudflare_account",
            "Tuỳ chọn. Sinh ảnh miễn phí qua Workers AI, 10.000 Neuron mỗi ngày",
            "Lấy Account ID tại https://dash.cloudflare.com rồi đặt biến môi "
            "trường CLOUDFLARE_ACCOUNT_ID, hoặc ghi vào file ~/.cloudflare_account",
            bat_buoc=False,
        ),
        kiem_key(
            "CLOUDFLARE_API_TOKEN", ".cloudflare_token",
            "Tuỳ chọn. Đi kèm CLOUDFLARE_ACCOUNT_ID, token cần quyền Workers AI",
            "Tạo token có quyền Workers AI tại https://dash.cloudflare.com rồi đặt "
            "biến môi trường CLOUDFLARE_API_TOKEN, hoặc ghi vào file ~/.cloudflare_token",
            bat_buoc=False,
        ),
        kiem_goi_python(
            "edge_tts",
            "Tuỳ chọn. Giọng đọc miễn phí có tiếng Việt, dùng cho bản nháp",
            "pip install edge-tts",
        ),
        kiem_goi_python(
            "requests",
            "Cần cho fetch_stock.py và generate_image_cf.py",
            "pip install requests",
        ),
    ]
    return kq


def in_bang(kq):
    print("Kiểm tra môi trường cho skill ai-video-studio")
    print(f"Hệ điều hành: {sys.platform}")
    print()
    rong = max(len(k["ten"]) for k in kq)
    for k in kq:
        dau = "co " if k["co"] else ("THIEU" if k["bat_buoc"] else "thieu")
        nhan = "bắt buộc" if k["bat_buoc"] else "tuỳ chọn"
        print(f"  [{dau:>5}] {k['ten']:<{rong}}  ({nhan})  {k.get('version') or ''}")
        if not k["co"]:
            print(f"          {k['mo_ta']}")
            print(f"          Cài bằng: {k.get('cach_cai', 'tự cài')}")
    print()
    thieu_bb = [k["ten"] for k in kq if k["bat_buoc"] and not k["co"]]
    thieu_tc = [k["ten"] for k in kq if not k["bat_buoc"] and not k["co"]]
    if thieu_bb:
        print(f"THIẾU thứ bắt buộc: {', '.join(thieu_bb)}. Cài xong hãy chạy lại.")
    else:
        print("Đủ điều kiện chạy đường API và đường dựng bằng ffmpeg.")
    if thieu_tc:
        print(f"Thiếu tuỳ chọn: {', '.join(thieu_tc)}. Chỉ ảnh hưởng các đường tương ứng.")
    return 1 if thieu_bb else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="Xuất JSON thay vì bảng chữ")
    args = ap.parse_args()
    kq = chay()
    if args.json:
        thieu = [k["ten"] for k in kq if k["bat_buoc"] and not k["co"]]
        print(json.dumps({"platform": sys.platform, "san_sang": not thieu,
                          "thieu_bat_buoc": thieu, "chi_tiet": kq},
                         ensure_ascii=False, indent=2))
        return 1 if thieu else 0
    return in_bang(kq)


if __name__ == "__main__":
    sys.exit(main())
