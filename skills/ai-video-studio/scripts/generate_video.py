"""Tạo video từng shot bằng Veo 3.1 hoặc Gemini Omni qua Gemini API.

Cách dùng:
  python generate_video.py "prompt mo ta hanh dong" \
      --model fast --aspect 16:9 --out clip_01.mp4

Endpoint ĐÚNG cho Veo (đã verify): POST /v1beta/models/<model>:predictLongRunning
  - KHÔNG dùng :generateVideos hay :predictLongRunningGenerateVideos (404)
  - KHÔNG dùng numberOfVideos (model từ chối)
Schema: {"instances":[{"prompt":"..."}],"parameters":{"aspectRatio":"..."}}
Luồng: tạo operation (trả "name") -> poll GET /v1beta/<name> cho tới done.

Endpoint cho Omni (đọc doc chính thức 08/09/2026, xem
references/api-guide.md mục 2): POST /v1beta/interactions, KHÔNG còn dùng
:generateContent làm đường chủ động nữa vì generateContent không có
response_format nên không có cách chính thức đặt aspect_ratio/resolution.
"""
import argparse
import base64
import json
import mimetypes
import sys
import time
import urllib.request
import urllib.error

from config import get_api_key, BASE_URL, VEOS, OMNI

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
# Ép UTF-8 cho stdout/stderr để script chạy được mà không cần set biến môi trường.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


# alias thân thiện -> model id; nhận cả model id đầy đủ
MODELS = {
    **VEOS,
    "omni": OMNI,
    "quality": VEOS["standard"],
}


def is_veo_model(model):
    """True nếu model là một trong ba Veo 3.1, False nếu là Omni (hoặc model
    Gemini khác gọi qua đường generateContent thời cũ)."""
    return model in VEOS.values()


def _post(url, payload, key):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            body = json.load(e)
        except Exception:
            body = {"message": e.read().decode(errors="replace")}
        return e.code, body


def _encode_image(path):
    """Đọc file ảnh local, trả về object inlineData theo đúng shape đã verify
    qua doc Veo (ai.google.dev/gemini-api/docs/veo, đọc qua WebFetch
    08/09/2026): {"inlineData": {"mimeType": "...", "data": "<base64>"}}."""
    mime = mimetypes.guess_type(path)[0] or "image/png"
    with open(path, "rb") as f:
        data = base64.b64encode(f.read()).decode("ascii")
    return {"inlineData": {"mimeType": mime, "data": data}}


def build_reference_images(paths):
    """paths: list đường dẫn ảnh local, tối đa 3 (ràng buộc của Veo).

    Shape mỗi phần tử {"image": {...inlineData...}, "referenceType": "asset"}
    đọc qua WebFetch doc Veo 08/09/2026, bằng chứng trung bình. Giá trị
    referenceType khác ngoài "asset" [chưa xác minh].
    """
    if len(paths) > 3:
        raise SystemExit(
            f"referenceImages tối đa 3 ảnh (bạn truyền {len(paths)})."
        )
    return [
        {"image": _encode_image(p), "referenceType": "asset"} for p in paths
    ]


def validate_veo_constraints(model, duration, resolution, reference_images):
    """Kiểm tra ràng buộc Veo TRƯỚC khi gọi API, tránh chờ lỗi 400 mới biết.

    Nguồn: references/api-guide.md mục 1, bảng RÀNG BUỘC (đọc doc chính thức
    08/09/2026).
    - durationSeconds bắt buộc là 8 khi dùng resolution 1080p/4k hoặc dùng
      referenceImages.
    - "4k" không dùng được trên Veo 3.1 Lite.

    Trả về duration đã chuẩn hoá (tự đặt 8 nếu người dùng không truyền gì mà
    lại dùng một trong các tính năng bắt buộc 8 giây). Nếu người dùng TRUYỀN
    RÕ một duration khác 8 trong khi dùng các tính năng đó thì báo lỗi và
    dừng hẳn, không tự ý sửa theo ý mình.
    """
    forces_8s = []
    if resolution in ("1080p", "4k"):
        forces_8s.append(f"resolution={resolution}")
    if reference_images:
        forces_8s.append("referenceImages")

    if forces_8s and duration is not None and duration != 8:
        raise SystemExit(
            "Sai tham số Veo: dùng " + ", ".join(forces_8s) +
            f" thì --duration bắt buộc là 8 (bạn truyền {duration})."
        )
    if forces_8s and duration is None:
        print(f"Lưu ý: {', '.join(forces_8s)} bắt buộc 8 giây, tự đặt --duration=8.")
        duration = 8

    if resolution == "4k" and model == VEOS["lite"]:
        raise SystemExit("Sai tham số Veo: Veo 3.1 Lite không hỗ trợ resolution 4k.")

    if resolution == "360p":
        raise SystemExit(
            "Sai tham số Veo: 360p chỉ có ở Gemini Omni Flash, ba model Veo không "
            "có mức này. Muốn nháp rẻ thì dùng --model omni --resolution 360p."
        )

    return duration


def create_operation(model, prompt, aspect, key, duration=None, resolution=None,
                      reference_images=None):
    """Tạo operation/interaction tạo video.

    - Veo (veo-3.1-*) dùng :predictLongRunning (đã verify: không phải generateVideos).
    - Gemini Omni dùng POST /v1beta/interactions (xem references/api-guide.md
      mục 2). KHÔNG còn dùng :generateContent làm đường chủ động, vì
      generateContent không có response_format nên trước đây phải nhét tỉ lệ
      khung hình vào giữa câu prompt — đó là lỗi đã sửa ở bản này.
    """
    if not is_veo_model(model):
        # Omni: Interactions API, đồng bộ, không cần poll.
        url = f"{BASE_URL}/interactions?key={key}"
        # Omni không có field thời lượng riêng trong tài liệu đọc được.
        # Cách ĐÃ VERIFY để đặt thời lượng vẫn là viết thẳng vào input.
        # Bằng chứng: câu "Create one 8-second video ..." cho ra file đo được
        # đúng 8.000000 giây (ffprobe). Xem references/format-and-export.md mục 4.
        if duration:
            text = f"Create one {duration}-second video. {prompt}"
        else:
            text = prompt
        response_format = {"type": "video", "aspect_ratio": aspect}
        if resolution:
            response_format["resolution"] = resolution
        payload = {
            "model": model,
            "input": text,
            "response_format": response_format,
            # task mặc định text_to_video vì script này chỉ nhận prompt text,
            # chưa hỗ trợ image_to_video/reference_to_video/edit/extend.
            "generation_config": {"video_config": {"task": "text_to_video"}},
        }
    else:
        # Veo: predictLongRunning
        url = f"{BASE_URL}/models/{model}:predictLongRunning?key={key}"
        params = {"aspectRatio": aspect}
        if duration:
            # Nguồn: ai.google.dev/gemini-api/docs/veo, đọc HTML thô ngày 06/09/2026.
            # Nguyên văn trên trang: durationSeconds : Length of the generated video.
            #   "4" , "6" , "8" . Must be "8" when using extension, reference images
            #   or with 1080p and 4k resolutions
            # Vậy giá trị là CHUỖI, không phải số nguyên. Và Veo KHÔNG nhận 10 giây;
            # chỉ Omni mới có mức 10 giây (đo trên giao diện Flow ngày 06/09/2026).
            if int(duration) not in (4, 6, 8):
                raise SystemExit(
                    f"Veo chỉ nhận durationSeconds 4, 6 hoặc 8 (bạn truyền {duration}). "
                    "Muốn 10 giây thì dùng --model omni."
                )
            params["durationSeconds"] = str(int(duration))
        if resolution:
            params["resolution"] = resolution
        instance = {"prompt": prompt}
        if reference_images:
            instance["referenceImages"] = reference_images
        payload = {
            "instances": [instance],
            "parameters": params,
        }
    return _post(url, payload, key)


LOI_THOANG = (500, 502, 503, 504)
TOI_DA_LOI_LIEN_TIEP = 5


def poll_operation(name, key, timeout=600, interval=8, interval_toi_da=30):
    """Chờ operation sinh video chạy xong, trả (status, body).

    Điều quan trọng nhất ở đây: credit đã bị trừ ngay khi operation được tạo,
    TRƯỚC khi vòng chờ này bắt đầu. Nên một lỗi thoáng giữa chừng mà làm hàm
    thoát sớm là mất trắng clip đã trả tiền. Vì vậy vòng chờ phải sống sót qua
    mất mạng và qua lỗi 5xx, chỉ đầu hàng khi lỗi lặp liên tiếp quá nhiều lần
    hoặc khi gặp lỗi thật sự không cứu được (400, 401, 404).

    Giãn dần khoảng chờ từ `interval` lên `interval_toi_da` để đỡ đập API với
    clip lâu, mà vẫn phản hồi nhanh với clip ngắn.
    """
    url = f"{BASE_URL}/{name}?key={key}"
    start = time.time()
    cho = interval
    lan = 0
    loi_lien_tiep = 0

    while True:
        con_lai = timeout - (time.time() - start)
        if con_lai <= 0:
            return 504, {"error": {"message": (
                f"Chờ quá {timeout}s mà operation chưa done. Clip có thể vẫn "
                f"đang sinh; operation name là {name}, hỏi lại sau bằng chính "
                "name đó thay vì sinh lại từ đầu.")}}

        lan += 1
        status, body = _get(url)

        if status == 200:
            loi_lien_tiep = 0
            if body.get("done"):
                print(f"  xong sau {time.time() - start:.0f}s, hỏi {lan} lần.")
                return 200, body
            print(f"  đang sinh... {time.time() - start:.0f}s (lần hỏi {lan})", flush=True)
        elif status == 0 or status in LOI_THOANG:
            # status 0 nghĩa là lỗi mạng phía mình, chưa chạm tới server.
            loi_lien_tiep += 1
            msg = (body.get("error") or {}).get("message", "")
            print(f"  lỗi thoáng {loi_lien_tiep}/{TOI_DA_LOI_LIEN_TIEP}: {msg[:120]}", flush=True)
            if loi_lien_tiep >= TOI_DA_LOI_LIEN_TIEP:
                return (status or 504), body
        else:
            # 400, 401, 404... thử lại cũng vô ích.
            return status, body

        time.sleep(min(cho, max(con_lai, 0)))
        cho = min(cho * 1.5, interval_toi_da)


def _get(url):
    """GET một URL, luôn trả (status, body), KHÔNG bao giờ ném ngoại lệ.

    Trả status 0 cho lỗi mạng. Người gọi phân biệt được "chưa tới được server"
    với "server trả lỗi", và tự quyết định thử lại hay dừng.
    """
    req = urllib.request.Request(url, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            body = json.load(e)
        except Exception:
            body = {"message": e.read().decode(errors="replace")}
        return e.code, body
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        return 0, {"error": {"message": f"lỗi mạng: {e}"}}
    except json.JSONDecodeError as e:
        return 0, {"error": {"message": f"response không phải JSON: {e}"}}


def _retry_delay(body):
    """Đọc retryDelay trong error.details nếu API có gửi. Trả số giây hoặc None.

    Google trả dạng {"@type": ".../google.rpc.RetryInfo", "retryDelay": "27s"}.
    """
    details = ((body.get("error") or {}).get("details") or [])
    for d in details:
        if not isinstance(d, dict):
            continue
        raw = d.get("retryDelay")
        if isinstance(raw, str) and raw.endswith("s"):
            try:
                return float(raw[:-1])
            except ValueError:
                return None
    return None


def handle_error(status, body):
    """Phân loại HTTP status. Trả 'ok' | 'retry' | 'stop'.

    Bảng lỗi đầy đủ nằm ở references/api-guide.md mục 8, KHÔNG phải SKILL.md.
    Quy tắc 429 theo đúng tài liệu đó: có retryDelay thì chờ rồi gọi lại,
    không có thì mới dừng hẳn.
    """
    if 200 <= status < 300:
        return "ok"
    msg = (body.get("error") or {}).get("message", str(body))
    print(f"[{status}] {msg}")
    if status == 429:
        delay = _retry_delay(body)
        if delay is not None:
            print(f"Bị giới hạn tốc độ, API bảo chờ {delay}s rồi gọi lại.")
            time.sleep(delay)
            return "retry"
        print("HẾT QUOTA và API không kèm retryDelay. Kiểm tra billing tại https://ai.dev/rate-limit. Ngừng.")
        return "stop"
    if status == 400:
        print("Sai payload. Sửa schema (instances[] / bỏ numberOfVideos).")
        return "stop"
    if status in (500, 504):
        print("Lỗi thoáng, retry...")
        return "retry"
    if status == 404:
        print("Sai endpoint/model. Kiểm tra model id + suffix :predictLongRunning / :interactions.")
        return "stop"
    return "stop"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt", help="Prompt mô tả hành động cho 1 shot")
    ap.add_argument("--model", default="fast", choices=list(MODELS.keys()))
    ap.add_argument("--aspect", default="16:9", choices=["16:9", "9:16"])
    ap.add_argument("--duration", type=int, default=None, choices=[4, 6, 8, 10],
                    help="Thời lượng giây. Giao diện Flow cho Omni chọn 4/6/8/10. Doc Veo ghi rõ chỉ nhận chuỗi 4, 6, 8, và bắt buộc là 8 khi dùng extension, reference images, 1080p hoặc 4k.")
    ap.add_argument("--resolution", default=None,
                    choices=["360p", "720p", "1080p", "4k"],
                    help="Độ phân giải. Mặc định API là 720p nếu bỏ trống. "
                         "'360p' CHỈ có ở Omni và là mức nháp rẻ nhất, đúng theo "
                         "Luật vàng số 1 của SKILL.md. Veo không có 360p. "
                         "'4k' không dùng được với --model lite (Veo 3.1 Lite).")
    ap.add_argument("--reference-images", default=None,
                    help="Chỉ áp dụng cho Veo. Đường dẫn ảnh local, cách nhau "
                         "bằng dấu phẩy, tối đa 3 ảnh (Ingredients to Video). "
                         "Bắt buộc --duration 8 khi dùng.")
    ap.add_argument("--out", default="clip.mp4", help="File lưu video")
    ap.add_argument("--max-retry", type=int, default=3)
    args = ap.parse_args()

    key = get_api_key()
    # alias thân thiện -> model id; nhận cả model id đầy đủ
    model = MODELS.get(args.model, args.model)

    reference_images = None
    if args.reference_images:
        if not is_veo_model(model):
            raise SystemExit("--reference-images chỉ dùng được với Veo, không dùng được với --model omni.")
        paths = [p.strip() for p in args.reference_images.split(",") if p.strip()]
        reference_images = build_reference_images(paths)

    duration = args.duration
    if is_veo_model(model):
        duration = validate_veo_constraints(model, duration, args.resolution, reference_images)

    for attempt in range(args.max_retry + 1):
        status, body = create_operation(model, args.prompt, args.aspect, key,
                                        duration=duration, resolution=args.resolution,
                                        reference_images=reference_images)
        action = handle_error(status, body)
        if action == "stop":
            sys.exit(1)
        if action == "retry":
            time.sleep(5 * (attempt + 1))
            continue
        # success. Phân nhánh:
        #   - Veo (predictLongRunning): body có "name" → poll tới khi done.
        #   - Omni (Interactions API): body có "object": "interaction" → đồng bộ, dùng luôn.
        #   - generateContent kiểu cũ (dự phòng, không còn được gọi chủ động ở
        #     đây nhưng giữ nhánh phòng khi model khác trả về dạng này): "candidates".
        if body.get("name"):
            name = body["name"]
            print(f"Operation created: {name}")
            status, final_body = poll_operation(name, key)
            if status != 200:
                handle_error(status, final_body)
                sys.exit(1)
            final = final_body
        elif body.get("object") == "interaction":
            print(f"Omni interactions API trả ngay (đồng bộ), status={body.get('status')}.")
            final = body
        elif body.get("candidates"):
            print("generateContent kiểu cũ trả ngay (đồng bộ).")
            final = body
        else:
            handle_error(status, body)
            sys.exit(1)
        # tìm uri video
        kind, val = extract_uri(final)
        if not val:
            print("Không tìm thấy uri video trong response:", json.dumps(final)[:400])
            sys.exit(1)
        if kind == "base64":
            import base64 as _b64
            with open(args.out, "wb") as f:
                f.write(_b64.b64decode(val))
        else:
            download(val, args.out)
        print(f"Đã tải video -> {args.out}")
        return

    print("Thất bại sau nhiều lần retry.")


def extract_uri(body):
    """Tìm uri/base64 video trong nhiều dạng response.

    - predictLongRunning (Veo): body["response"]["video"]["uri"].
    - Interactions API (Omni, /v1beta/interactions): body["steps"][] có phần
      tử type == "model_output", bên trong content[] có phần tử type ==
      "video" với "data" (base64) hoặc "uri". Nguồn:
      ai.google.dev/gemini-api/docs/omni, đọc qua WebFetch 08/09/2026, bằng
      chứng trung bình (model tóm tắt), CHƯA tự gọi bằng key thật để xác nhận
      response thật trên endpoint này khớp y hệt.
    - generateContent kiểu cũ (candidates[].content.parts[].inlineData): giữ
      lại làm phương án dự phòng, KHÔNG còn được nhánh Omni trong script này
      chủ động gọi tới nữa kể từ khi chuyển sang /v1beta/interactions.
    Trả về (kind, value): kind='uri' | 'base64'.
    """
    # 1) dạng predictLongRunning
    resp = body.get("response", {})
    v = resp.get("video") if isinstance(resp, dict) else None
    if v and isinstance(v, dict):
        u = v.get("uri") or v.get("url")
        if u:
            return "uri", u
    # 2) dạng Interactions API (Omni mới).
    # CỐ Ý không lọc theo step["type"] == "model_output". Chuỗi đó lấy từ doc
    # đọc qua WebFetch chứ chưa ai xác minh bằng key thật, nên nếu response
    # thật dùng tên khác hoặc không có field type thì script sẽ mất tiền sinh
    # video xong vẫn thoát lỗi mà không lấy được file. Quét mọi step rồi tìm
    # phần tử content type == "video" là đủ và không mất mát gì.
    for step in body.get("steps", []):
        if not isinstance(step, dict):
            continue
        for item in step.get("content", []) or []:
            if isinstance(item, dict) and item.get("type") == "video":
                if item.get("uri"):
                    return "uri", item["uri"]
                if item.get("data"):
                    return "base64", item["data"]
    # 3) dạng generateContent kiểu cũ (dự phòng)
    for cand in body.get("candidates", []):
        for part in cand.get("content", {}).get("parts", []):
            d = part.get("inlineData") or part.get("inline_data", {})
            if d.get("data"):
                return "base64", d["data"]
    return None, None


def download(uri, path):
    import shutil
    req = urllib.request.Request(uri, headers={"User-Agent": "skill"})
    with urllib.request.urlopen(req) as resp, open(path, "wb") as out:
        shutil.copyfileobj(resp, out)


if __name__ == "__main__":
    main()
