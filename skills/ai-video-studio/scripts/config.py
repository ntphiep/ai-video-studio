"""Cấu hình chung cho skill ai-video-studio.

API key KHÔNG nhúng cứng ở đây. Đọc từ env GEMINI_API_KEY.
Nếu cần file local, người dùng có thể đặt tại ~/.gemini_key (KHÔNG commit).
"""
import os
import sys
from pathlib import Path

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
# Ép UTF-8 cho stdout/stderr để script chạy được mà không cần set biến môi trường.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


def get_api_key() -> str:
    """Lấy Gemini API key từ env hoặc file local, không từ code."""
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key.strip()
    # Fallback: file local ở home, không nằm trong repo/skill
    keyfile = Path.home() / ".gemini_key"
    if keyfile.exists():
        return keyfile.read_text().strip()
    sys.exit(
        "❌ Thiếu GEMINI_API_KEY. Đặt env: $env:GEMINI_API_KEY='...' "
        "hoặc tạo file ~/.gemini_key"
    )

# Base URL Gemini API (v1beta)
BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

# Model ids (đã verify tồn tại qua models list của key)
VEOS = {
    "lite": "veo-3.1-lite-generate-preview",
    "fast": "veo-3.1-fast-generate-preview",
    "standard": "veo-3.1-generate-preview",  # "3.1 Quality" trong Flow
}
OMNI = "gemini-omni-1.1-flash"
IMAGE_MODELS = {
    "nano-banana-2": "gemini-3.1-flash-image",
    "nano-banana-pro": "gemini-3-pro-image",
    "nano-banana-2-lite": "gemini-3.1-flash-lite-image",
}
TTS = "gemini-3.1-flash-tts-preview"
# Lyria 3.5 là model nhạc mới nhất, xác nhận BA chiều:
# (a) trang flowmusic.app ghi "our latest frontier music model, Lyria 3.5",
# (b) gọi GET /v1beta/models trên key thật trả về đúng id "lyria-3.5"
#     (06/09/2026),
# (c) [changelog] https://ai.google.dev/gemini-api/docs/changelog, đọc
#     08/09/2026, mục ngày 03/09/2026: "Lyria 3.5 vào public preview: sinh
#     trọn bài hát, giọng hát tự nhiên hơn, kiểm soát cấu trúc và thời lượng
#     tốt hơn". Xem references/api-guide.md mục 5 và mục Tự soát nguồn.
MUSIC = {
    "latest": "lyria-3.5",
    "clip": "lyria-3-clip-preview",
    "pro": "lyria-3-pro-preview",
}
WRITER = "gemini-3.5-flash"  # viết kịch bản và chia shot. Đây là model duy nhất
                            # trong nhóm này đã tự gọi thử và nhận 200.

# Chuẩn xuất YouTube
YOUTUBE = {
    "container": "mp4",
    "video_codec": "h264",
    "audio_codec": "aac",
    "audio_sample_rate": 48000,
    "fps": 24,
    "bitrate_1080p": "8M",
    "bitrate_720p": "5M",
}
