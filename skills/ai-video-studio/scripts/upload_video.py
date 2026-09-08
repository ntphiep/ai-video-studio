"""Chuẩn bị metadata cho việc đăng video. KHÔNG tải file lên bất cứ đâu.

Tên file là di sản cũ. Script này CHỈ sinh ra một file JSON gồm tiêu đề, mô tả,
tag và thông tin file, để bước đăng về sau dùng lại. Nó không gọi Google Drive,
không gọi YouTube, không gọi dịch vụ nào khác. Việc đăng thật do người dùng làm.

CÓ MỘT ĐƯỜNG NGẮN HƠN nếu video được làm hoàn toàn trong Google Flow: chuột phải
lên video trong project rồi chọn `Publish to YouTube`, Flow đăng thẳng lên. Đo
trực tiếp trên giao diện ngày 08/09/2026, xem references/flow-core.md mục 1.2.
Chỉ dùng script này khi video được dựng ngoài Flow, ví dụ đường Remotion.

Cách dùng:
  python upload_video.py --title "Video 1" --file final.mp4       --desc "Mô tả" --tags "ai,faceless" --category 22       --meta-out meta.json
"""
import argparse
import sys
import json
import os

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
# Ép UTF-8 cho stdout/stderr để script chạy được mà không cần set biến môi trường.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True, help="Tiêu đề video (tối đa 100 ký tự)")
    ap.add_argument("--file", required=True, help="Đường dẫn file MP4 đã lắp ráp")
    ap.add_argument("--desc", default="")
    ap.add_argument("--tags", default="", help="Tags, phân tách bằng dấu phẩy")
    ap.add_argument("--category", default="22", help="YouTube category id (22=People & Blogs)")
    ap.add_argument("--privacy", default="private", choices=["public", "private", "unlisted"])
    ap.add_argument("--thumbnail", default="", help="Đường dẫn ảnh thumbnail (1280x720)")
    ap.add_argument("--meta-out", default="upload_meta.json")
    args = ap.parse_args()

    # validate file tồn tại
    if not os.path.exists(args.file):
        print(f"❌ File không tồn tại: {args.file}")
        raise SystemExit(1)

    meta = {
        "title": args.title[:100],
        "file": os.path.abspath(args.file),
        "description": args.desc,
        "tags": [t.strip() for t in args.tags.split(",") if t.strip()],
        "categoryId": args.category,
        "privacyStatus": args.privacy,
        "thumbnail": os.path.abspath(args.thumbnail) if args.thumbnail else "",
    }
    with open(args.meta_out, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    print(f"Đã lưu metadata -> {args.meta_out}")
    print(meta)


if __name__ == "__main__":
    main()
