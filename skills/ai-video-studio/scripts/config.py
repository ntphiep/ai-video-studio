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


def _doc_key(ten_env: str, ten_file: str, huong_dan: str, bat_buoc: bool = True):
    """Đọc một API key từ env, hoặc từ file trong thư mục home.

    Không bao giờ nhúng cứng key vào code. Trả về None nếu không bắt buộc mà
    cũng không tìm thấy, để script gọi tự quyết định bỏ qua hay báo lỗi.
    """
    key = os.environ.get(ten_env)
    if key:
        return key.strip()
    keyfile = Path.home() / ten_file
    if keyfile.exists():
        return keyfile.read_text().strip()
    if bat_buoc:
        sys.exit(f"❌ Thiếu {ten_env}. {huong_dan}")
    return None


def get_api_key() -> str:
    """Lấy Gemini API key từ env hoặc file local, không từ code."""
    return _doc_key(
        "GEMINI_API_KEY",
        ".gemini_key",
        "Đặt env: $env:GEMINI_API_KEY='...' hoặc tạo file ~/.gemini_key",
    )


def get_pexels_key(bat_buoc: bool = True):
    """Key Pexels cho ảnh và video stock. Lấy miễn phí ở pexels.com/api/."""
    return _doc_key(
        "PEXELS_API_KEY",
        ".pexels_key",
        "Đăng ký miễn phí ở https://www.pexels.com/api/ rồi đặt env "
        "$env:PEXELS_API_KEY='...' hoặc tạo file ~/.pexels_key",
        bat_buoc,
    )


def get_cloudflare(bat_buoc: bool = True):
    """Trả về (account_id, api_token) cho Workers AI, hoặc (None, None)."""
    acc = _doc_key(
        "CLOUDFLARE_ACCOUNT_ID",
        ".cloudflare_account",
        "Lấy Account ID ở dash.cloudflare.com rồi đặt env "
        "$env:CLOUDFLARE_ACCOUNT_ID='...' hoặc tạo file ~/.cloudflare_account",
        bat_buoc,
    )
    tok = _doc_key(
        "CLOUDFLARE_API_TOKEN",
        ".cloudflare_token",
        "Tạo API token có quyền Workers AI ở dash.cloudflare.com rồi đặt env "
        "$env:CLOUDFLARE_API_TOKEN='...' hoặc tạo file ~/.cloudflare_token",
        bat_buoc,
    )
    return acc, tok


# Cloudflare Workers AI. Bậc miễn phí 10.000 Neuron mỗi ngày, reset 00:00 UTC,
# không cần thẻ tín dụng. Nguồn:
# https://developers.cloudflare.com/workers-ai/platform/pricing/ đọc 09/09/2026.
CF_BASE = "https://api.cloudflare.com/client/v4/accounts/{acc}/ai/run/"
CF_IMAGE_MODEL = "@cf/black-forest-labs/flux-1-schnell"
CF_STEPS_MAX = 8  # doc ghi mặc định 4, tối đa 8

# Pexels. Rate limit công bố: 200 request mỗi giờ, 20.000 mỗi tháng.
# Nguồn: https://www.pexels.com/api/documentation/ đọc 09/09/2026.
PEXELS_PHOTO = "https://api.pexels.com/v1/search"
PEXELS_VIDEO = "https://api.pexels.com/v1/videos/search"
PEXELS_RATE = "200 request/giờ, 20.000/tháng"

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
