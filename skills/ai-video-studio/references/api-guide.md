# API Guide: Gemini (Veo, Omni, Nano Banana, TTS, Lyria)

Tra cứu endpoint, schema, model id và giới hạn để gọi trực tiếp Gemini API. File
này gộp và thay thế trọn ba file cũ đã bị gỡ khỏi skill. Chuyện
đường Google Flow UI (credit, voice UI, Flow Music) nằm ở `flow-core.md` và
`flow-tools.md`, không lặp lại ở đây.

## 0. Cảnh báo đầu tiên: Google chạy song song ba họ API khác cú pháp

Google hiện có **ba họ API khác cú pháp cho cùng một việc**. Nhầm họ là mọi ví
dụ đều sai (sai field, sai case, ra lỗi 400 hoặc 404).

| Họ API | Cách gọi | Case field | Dùng cho |
|---|---|---|---|
| **Interactions API** | `POST {BASE_URL}/interactions` hoặc `client.interactions.create(...)` | snake_case (`response_format`, `generation_config`, `previous_interaction_id`) | **Omni sinh video, đây là hợp đồng CHÍNH THỨC** theo `ai.google.dev/gemini-api/docs/omni` `[doc]`, đọc 08/09/2026. Đọc qua WebFetch (có model tóm tắt ở giữa), mức bằng chứng trung bình cho hình dạng payload/response cụ thể, CHƯA tự gọi bằng key thật để xác nhận response thật trên endpoint này. Nhưng đây là cách DUY NHẤT có tham số `aspect_ratio`, `resolution`, `task` chính thức, nên từ giờ script dùng đường này cho Omni. |
| **Generate Content API (cũ, tài liệu gọi là "Legacy")** | `models/{model}:generateContent` | camelCase (`responseModalities`, `speechConfig`) | Nano Banana, TTS (đã tự gọi bằng key thật và xác nhận endpoint tồn tại, mục 3, 4). Omni theo lối này (`responseModalities: ["VIDEO"]`) từng được tự gọi thật ngày 06/09/2026 và trả `candidates` thật, NHƯNG lối này không có `response_format` nên không có cách chính thức đặt `aspect_ratio`/`resolution` — đó chính là lỗi mà bản trước của skill mắc phải (nhét tỉ lệ khung hình vào giữa câu prompt). Giữ lại trong `extract_uri()` làm phương án đọc dự phòng, script không còn CHỦ ĐỘNG gọi đường này cho Omni nữa. |
| Riêng biệt, không thuộc hai họ trên | `models/{model}:predictLongRunning` | camelCase (`instances`, `parameters`) | Chỉ Veo 3.1, đã verify từ HTML thô trang doc Veo. |

Toàn bộ ví dụ trong file này dùng **Generate Content API** cho Nano Banana và
TTS, **Interactions API** cho Omni, và riêng Veo dùng `predictLongRunning`.

## Base URL

```
https://generativelanguage.googleapis.com/v1beta
```

## 1. Video: Veo 3.1

Endpoint (đã verify từ HTML thô trang `ai.google.dev/gemini-api/docs/veo`,
06/09/2026, và đối chiếu lại `[doc]` ngày 08/09/2026):
```
POST {BASE_URL}/models/{MODEL}:predictLongRunning
```

Truyền API key được CẢ HAI cách đều chạy: header `x-goog-api-key: {GEMINI_API_KEY}`
hoặc tham số trên URL `?key={GEMINI_API_KEY}`. Đánh đổi: đặt key trên URL thì
key lọt vào log của server và vào lịch sử shell, nên header an toàn hơn. Các
script hiện có trong skill (`generate_audio.py`, `generate_image.py`,
`generate_video.py`, `write_script.py`) đều đang dùng dạng `?key=`.

Model id: `veo-3.1-generate-preview` (Standard/"Quality"),
`veo-3.1-fast-generate-preview` (Fast), `veo-3.1-lite-generate-preview` (Lite).
`veo-3.0-generate-001` ghi "Deprecated" trên trang doc và không còn xuất hiện
khi gọi `models.list` bằng key thật (06/09/2026), đừng dùng.
`[doc]` https://ai.google.dev/gemini-api/docs/veo, đọc 08/09/2026, khớp với
lần đọc HTML thô 06/09/2026.

### Bảng tham số đầy đủ

Phần `instances[]` (mỗi phần tử một video muốn sinh):

| Field | Ý nghĩa | Ghi chú |
|---|---|---|
| `prompt` | Chuỗi mô tả cảnh | Bắt buộc |
| `image` | Khung hình đầu (image-to-video) | `{"inlineData": {"mimeType": "...", "data": "<base64>"}}`. `[doc]` https://ai.google.dev/gemini-api/docs/veo, đọc qua WebFetch 08/09/2026, bằng chứng trung bình (model tóm tắt), chưa tự gọi bằng key thật |
| `lastFrame` | Khung hình cuối | Cùng shape `inlineData` như trên. BẮT BUỘC phải có `image` đi kèm |
| `referenceImages` | Ảnh tham chiếu nhân vật/vật thể (Ingredients to Video) | Mảng, tối đa 3 phần tử, mỗi phần tử `{"image": {"inlineData": {...}}, "referenceType": "asset"}`. Giá trị `referenceType` khác ngoài `"asset"` `[chưa xác minh]`, doc tóm tắt chỉ cho thấy một ví dụ |
| `video` | Video do chính Veo sinh ra, dùng để nối dài | Cùng shape `inlineData` với `mimeType` dạng video (vd `video/mp4`) |

Phần `parameters` (áp dụng cho cả video sinh ra):

| Field | Giá trị hợp lệ | Ghi chú |
|---|---|---|
| `aspectRatio` | `"16:9"` (mặc định) hoặc `"9:16"` | Không có 21:9, 4:3 |
| `durationSeconds` | Chuỗi `"4"`, `"6"`, `"8"` | KHÔNG phải số nguyên. Xem bảng ràng buộc bên dưới |
| `resolution` | `"720p"` (mặc định), `"1080p"`, `"4k"` | `"4k"` KHÔNG có trên Veo 3.1 Lite |
| `personGeneration` | `"allow_all"` hoặc `"allow_adult"` | Xem hai ràng buộc riêng bên dưới, không mâu thuẫn nhau mà chồng lên nhau |
| `seed` | Số nguyên | `[doc]` https://ai.google.dev/gemini-api/docs/veo, đọc 08/09/2026, nguyên văn ghi nhận field này "chỉ có ở Veo 3". **MÂU THUẪN CHƯA GIẢI QUYẾT:** lần đọc HTML thô trước đó (06/09/2026, xem mục Tự soát nguồn) đã grep toàn bộ trang và không thấy field này, kết luận khi đó là "không tìm thấy". Ghi cả hai ở đây, KHÔNG tự chọn bên nào đúng cho tới khi có ai đọc lại và đối chiếu trực tiếp |
| `negativePrompt` | — | Vẫn `[chưa xác minh]`, không có trong cả hai lần đọc (06/09 và 08/09) |
| `numberOfVideos` | — | Xuất hiện trong ví dụ chính thức (giá trị `1`) nhưng một lần gọi thật trước đây kèm field này bị từ chối 400. Khuyến nghị: bỏ hẳn field này |

### Bảng ràng buộc

Nguồn: `[doc]` https://ai.google.dev/gemini-api/docs/veo, đọc 08/09/2026.

| Điều kiện | Ràng buộc |
|---|---|
| Dùng `resolution` `"1080p"` hoặc `"4k"` | `durationSeconds` BẮT BUỘC là `"8"` |
| Dùng `referenceImages` | `durationSeconds` BẮT BUỘC là `"8"`, tối đa 3 ảnh |
| Nối dài (dùng field `video`) | `durationSeconds` BẮT BUỘC là `"8"` |
| `"4k"` | KHÔNG dùng được trên `veo-3.1-lite-generate-preview` |
| Nối dài | Chỉ có ở Veo 3.1 (`veo-3.1-generate-preview`) và Veo 3.1 Fast, KHÔNG có ở Lite. Video đầu vào phải là 720p và không quá 141 giây. Kết quả là một video gộp, tối đa 148 giây |
| Vùng EU, Anh (UK), Thuỵ Sĩ (CH), MENA | `personGeneration` chỉ được `"allow_adult"`, bất kể chế độ sinh nào |
| Theo chế độ sinh (nguồn cũ hơn, chưa đối chiếu lại 08/09/2026, `[chưa xác minh lại]`) | text-to-video và extension chỉ nhận `"allow_all"`; image-to-video, interpolation, reference images chỉ nhận `"allow_adult"` |

Thông số kỹ thuật khác, `[doc]` https://ai.google.dev/gemini-api/docs/veo, đọc
08/09/2026: **24 hình mỗi giây**, **mỗi lần gọi trả về đúng 1 video**, video
**lưu trên máy chủ Google 2 ngày** và thời hạn này đặt lại nếu video được dùng
để nối dài. Âm thanh sinh kèm sẵn trong video; nếu bộ lọc an toàn chặn âm
thanh thì lượt đó không bị tính tiền.

Luồng: POST trả `"name"` (operation name). Poll `GET {BASE_URL}/{name}` cho
tới khi `"done": true`, lấy uri video từ `response.video.uri`.

## 2. Video: Gemini Omni Flash (khác Veo, dùng Interactions API)

Model id: `gemini-omni-1.1-flash`. Ra bản chính thức đại trà ngày 27/08/2026
theo `[doc]` https://ai.google.dev/gemini-api/docs/changelog, đọc 08/09/2026.

**Đây KHÔNG dùng `predictLongRunning` (đã verify live: trả 404 "not supported
for predictLongRunning") và KHÔNG còn dùng `generateContent` làm đường chính**
(xem mục 0). Đường chính thức để sinh video bằng Omni là Interactions API:

```
POST {BASE_URL}/interactions
```
SDK: `client.interactions.create(...)`

### Request

`[doc]` https://ai.google.dev/gemini-api/docs/omni, đọc qua WebFetch
08/09/2026, bằng chứng trung bình (model tóm tắt dựng lại từ trang doc, CHƯA
tự gọi bằng key thật đường này).

```json
{
  "model": "gemini-omni-1.1-flash",
  "input": "A futuristic city with neon lights and flying cars, cyberpunk style",
  "response_format": {
    "type": "video",
    "aspect_ratio": "9:16",
    "resolution": "720p"
  },
  "generation_config": {
    "video_config": {"task": "text_to_video"}
  }
}
```

`response_format` (top-level, KHÔNG nằm trong `generation_config`):
- `type`: `"video"`.
- `aspect_ratio`: `"16:9"` (mặc định) hoặc `"9:16"`.
- `resolution`: `"360p"`, `"720p"` (mặc định), `"1080p"`, `"4k"`.
- `delivery`: `"base64"` (mặc định, ngầm định), hoặc `"uri"` khi video lớn hơn
  4MB, trả về uri do Google host thay vì base64.

`generation_config.video_config.task`, năm giá trị hợp lệ, nguyên văn:
`"text_to_video"`, `"image_to_video"`, `"reference_to_video"`, `"edit"`,
`"extend"`.

`input` có thể là một chuỗi (text thuần), hoặc một mảng phần tử kiểu
`{"type": "text", "text": "..."}`, `{"type": "image", "data": "<base64>",
"mime_type": "..."}`, `{"type": "video", "data": "<base64>", "mime_type":
"..."}`, `{"type": "document", "uri": "files/..."}` khi cần trộn nhiều loại
nội dung trong một lượt gọi (ảnh/video tham chiếu, khung hình đầu/cuối).

Sửa nhiều lượt hoặc nối dài: thêm `previous_interaction_id` (giá trị là
`id` trả về từ lượt gọi trước, dạng `"v1_..."`).

**Về thời lượng:** `response_format` KHÔNG có field thời lượng riêng trong tài
liệu đọc được. Cách ĐÃ VERIFY để đặt thời lượng vẫn là viết thẳng vào `input`,
ví dụ `"Create one 8-second video. ..."`, đã đo bằng ffprobe ra đúng 8.000000
giây trên file thật (xem `references/format-and-export.md` mục 4). Mới tự đo
được đúng một giá trị là 8 giây ở cấp API. Bốn mức 4, 6, 8, 10 giây là mức của
**giao diện Flow** (xem mục 1 bảng năng lực trong `flow-core.md`), chưa ai thử
qua API, nên ba mức còn lại vẫn `[chưa xác minh]` ở cấp API.

**ĐÂY LÀ CHỖ ĐÃ SỬA so với bản trước.** Bản trước nhét tỉ lệ khung hình vào
giữa câu prompt tiếng Anh (`"in vertical 9:16 portrait format"`) vì lúc viết
chưa biết có `response_format.aspect_ratio`. Từ bản này, tỉ lệ khung hình và
độ phân giải đi qua đúng `response_format`, KHÔNG còn nhét vào prompt nữa.
Thời lượng vẫn phải nhét vào prompt vì chưa tìm thấy field riêng.

### Response

`[doc]` https://ai.google.dev/gemini-api/docs/omni, đọc qua WebFetch
08/09/2026, bằng chứng trung bình, chưa tự gọi bằng key thật để đối chiếu.

```json
{
  "steps": [
    {"type": "user_input", "content": [{"type": "text", "text": "..."}]},
    {"type": "thought", "content": [{"text": "...", "type": "thought"}]},
    {
      "type": "model_output",
      "content": [
        {"type": "video", "mime_type": "video/mp4", "data": "AAAAIGZ0eXBpc29t..."}
      ]
    }
  ],
  "id": "v1_...",
  "status": "completed",
  "model": "gemini-omni-1.1-flash",
  "object": "interaction"
}
```

Khi `response_format.delivery` là `"uri"`, phần tử video trong
`model_output` có `"uri"` thay vì `"data"`, và tài liệu ghi cần poll
`GET {BASE_URL}/files/{fileId}` tới khi `state` là `"ACTIVE"` trước khi tải —
script hiện tại CHƯA cài phần poll file này (chỉ dùng `delivery` mặc định là
base64), nên nếu sau này bật `--delivery uri` mà tải thất bại thì đây là lý do
đã biết trước, `[chưa xác minh]` cho tới khi ai tự thử.

Đây là phản hồi ĐỒNG BỘ (không có operation name, không cần poll như Veo),
nhận diện bằng `body.get("object") == "interaction"`.

### Giới hạn sửa và nối dài

Nguồn: `[doc]` https://ai.google.dev/gemini-api/docs/omni, đọc 08/09/2026.

- Video tải lên để sửa (`task: "edit"`) hoặc nối dài (`task: "extend"`) phải
  từ 10 giây trở xuống.
- Nối dài chỉ nối được vào CUỐI video. Không chèn vào giữa, không nối vào đầu.
- Tổng thời lượng đầu ra tối đa 40 giây.
- Không nối dài để thêm thoại vào một video tải lên đã có người đang nói.
- Video tham chiếu (`task: "reference_to_video"`) tối đa 3 clip, mỗi clip
  không quá 3 giây, và âm thanh trong video tham chiếu bị bỏ qua.
- Không sửa và không nối dài video TẢI LÊN ở khu vực EEA, Thuỵ Sĩ (CH) và Anh
  (UK). Video do chính model sinh ra thì vẫn sửa/nối dài được ở mọi nơi.

### Thẻ đặc biệt trong prompt

Nguyên văn, dùng bên trong `input` dạng text:
- `<FIRST_FRAME>` khung hình đầu.
- `<LAST_FRAME>` khung hình cuối, phải có `<FIRST_FRAME>` đi kèm.
- `<IMAGE_REF_N>` ảnh tham chiếu, N đếm từ 0.
- `<VIDEO_REF_N>` video tham chiếu, N đếm từ 0.

Cú pháp mốc thời gian, nguyên văn:
```
[0-3s] Scene description
[3-6s] Next scene
```
Cũng hỗ trợ diễn đạt tự nhiên như `"After 3 seconds, a woman enters"` hoặc
`"Every 2s cut to a new frame"`.

Cú pháp khai báo nguồn/tham chiếu, nguyên văn:
```
[# Sources <FIRST_FRAME>@Image1]
[# References <IMAGE_REF_0>@Image2]
```

### Không hỗ trợ

Omni KHÔNG hỗ trợ: **system instruction**, **`temperature`**, **`top_p`**,
**stop sequence**, provisioned throughput, và suy luận bắc cầu qua nhiều
video. Tiếng Anh được hỗ trợ đầy đủ, các ngôn ngữ khác chưa được đánh giá.
`[doc]` https://ai.google.dev/gemini-api/docs/omni, đọc 08/09/2026.

## 3. Ảnh: Nano Banana

Không dùng `:predict` (đã verify live: 404 "not supported for predict" / "is
not found"). Dùng `:generateContent` với `responseModalities: ["IMAGE"]`. Ảnh
trả về base64 trong `candidates[].content.parts[].inline_data[].data`.

```
POST {BASE_URL}/models/{MODEL}:generateContent
```

```json
{
  "contents": [{"parts": [{"text": "..."}]}],
  "generationConfig": {"responseModalities": ["IMAGE"]}
}
```

Model id (từ `models.list` bằng key thật, 06/09/2026): `gemini-3.1-flash-image`
(Nano Banana 2, mặc định), `gemini-3-pro-image` (Nano Banana Pro),
`gemini-3.1-flash-lite-image` (Nano Banana 2 Lite). Cũng tồn tại
`gemini-2.5-flash-image`, `gemini-3-pro-image-preview`,
`gemini-3.1-flash-image-preview`.

## 4. TTS: Gemini Flash TTS

Model id đang dùng: `gemini-3.1-flash-tts-preview`. Cũng tồn tại
`gemini-2.5-flash-preview-tts` và `gemini-2.5-pro-preview-tts` trên key thật.

**Cú pháp legacy** (đã tự gọi và xác nhận hoạt động):
```
POST {BASE_URL}/models/gemini-3.1-flash-tts-preview:generateContent
```
```json
{
  "contents": [{"parts": [{"text": "synthesise speech:\n..."}]}],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Puck"}}}
  }
}
```
Đa giọng (legacy): `multiSpeakerVoiceConfig.speakerVoiceConfigs[]`, mỗi phần tử
`{speaker, voiceConfig}`.

**Cú pháp Interactions API mới, `[chưa xác minh bằng key thật]`.** Theo tài
liệu tổng hợp, họ API mới dùng field snake_case:
```
generation_config.speech_config = [ { "voice": "Kore" } ]
```
Đa giọng mới: `speech_config: [ {"speaker": "Joe", "voice": "Kore"} ]`. Không
được trộn hai cú pháp trong cùng một request.

**`voiceName` không phải mã BCP-47.** Bản cũ từng ghi ví dụ
`"voiceName": "en-US"` gây lỗi, đừng lặp lại. Đã tự gọi thật và xác nhận:
`voiceName` phải là tên nhân vật (`Puck`, `Charon`, `Fenrir`, `Leda`, `Kore`).
Truyền mã locale như `en-US`, `vi`, `vi-VN-*` trả về
**400 "No matching speaker voice found"**.

Danh sách 30 giọng hợp lệ (tên nhân vật, không phải mã ngôn ngữ): Zephyr,
Puck, Charon, Kore, Fenrir, Leda, Orus, Aoede, Callirrhoe, Autonoe, Enceladus,
Iapetus, Umbriel, Algieba, Despina, Erinome, Algenib, Rasalgethi, Laomedeia,
Achernar, Alnilam, Schedar, Gacrux, Pulcherrima, Achird, Zubenelgenubi,
Vindemiatrix, Sadachbia, Sadaltager, Sulafat. Con số này khác với "23 base
voice" từng thấy trong dialog chọn giọng của Flow UI, hai con số thuộc hai
ngữ cảnh khác nhau (API và UI), không được gộp lẫn.

**Định dạng output.** Model trả PCM thô, mime báo
`audio/l16; rate=24000; channels=1` (24kHz, 1 kênh, 16-bit), không phải MP3.
Phải tự thêm header WAV (RIFF) trước khi lưu `.wav`, nếu không ffmpeg/player
không đọc được. `generate_audio.py` đã có sẵn `_wrap_wav()`.

**Rate limit** (đã verify live): quota `generate_content_free_tier_requests`
giới hạn 3, tên model trong thông báo quota là `gemini-3.1-flash-tts` (không
có hậu tố `-preview`, khác model id gọi API). Vượt quota trả 429 kèm
`retryDelay` dạng chuỗi như `"2.7s"`, đã quan sát trực tiếp từ response thật.

## 5. Nhạc: Lyria

```
POST {BASE_URL}/models/{MODEL}:generateContent
```

Model id từ `models.list` bằng key thật (06/09/2026): `lyria-3-clip-preview`
(clip khoảng 30s), `lyria-3-pro-preview` (bài hoàn chỉnh), `lyria-3.5` (model
mới nhất, xác nhận BA chiều: trang flowmusic.app gọi đây là "our latest
frontier music model, Lyria 3.5", `models.list` bằng key thật trả đúng id
này, và `[changelog]` https://ai.google.dev/gemini-api/docs/changelog đọc
08/09/2026 ghi mục ngày 03/09/2026 "Lyria 3.5 vào public preview: sinh trọn
bài hát, giọng hát tự nhiên hơn, kiểm soát cấu trúc và thời lượng tốt hơn").

## 6. Text: viết kịch bản

```
POST {BASE_URL}/models/{MODEL}:generateContent
```

Đã tự gọi và xác nhận: `gemini-3.5-flash` trả HTTP 200, dùng được để viết
kịch bản và chia shot. `gemini-2.5-pro` và `gemini-3.1-flash` trả 404 trên
key này tại thời điểm test, không dùng.

## 7. Bảng model hiện hành (kết quả gọi API thật, `models.list`, 06/09/2026)

Key thật trả tổng 54 model, các nhóm liên quan tới skill này:

| Nhóm | Model id |
|---|---|
| Video | `veo-3.1-fast-generate-preview`, `veo-3.1-generate-preview`, `veo-3.1-lite-generate-preview` |
| Omni | `gemini-omni-1.1-flash`, `gemini-omni-flash-preview` |
| Ảnh | `gemini-2.5-flash-image`, `gemini-3-pro-image`, `gemini-3-pro-image-preview`, `gemini-3.1-flash-image`, `gemini-3.1-flash-image-preview`, `gemini-3.1-flash-lite-image` |
| TTS | `gemini-2.5-flash-preview-tts`, `gemini-2.5-pro-preview-tts`, `gemini-3.1-flash-tts-preview` |
| Nhạc | `lyria-3-clip-preview`, `lyria-3-pro-preview`, `lyria-3.5` |

`veo-2` và `veo-3.0-generate-001` không còn trong danh sách này, khớp
changelog "Veo 2 Deprecation" ngày 02/03/2026.

## 8. Rate limit và lỗi, chỉ ghi phần có căn cứ

| HTTP | Ý nghĩa | Căn cứ | Hành động |
|---|---|---|---|
| 429 kèm `retryDelay` | Chạm rate limit tức thời | Đã quan sát trực tiếp trên TTS (limit 3/phút) | Chờ đúng `retryDelay` rồi gọi lại |
| 429 không kèm `retryDelay` | Hết quota ngày/gói | Suy luận từ hành vi API chuẩn Google, chưa tự gặp trường hợp này | Dừng, kiểm tra billing |
| 400 | Sai payload | Đã tự gặp (voiceName sai, numberOfVideos thừa) | Sửa schema theo mục tương ứng |
| 404 | Sai endpoint/model | Đã tự gặp (nhầm predict/predictLongRunning/generateContent giữa các model) | Kiểm tra đúng endpoint theo mục 1 đến 4 |
| 500/504 | Lỗi thoáng | Quan sát khi dùng TTS | Retry backoff, tối đa 3 lần |

Định dạng và ngữ nghĩa chi tiết của field `retryDelay`/`RetryInfo` nói chung
(ngoài trường hợp TTS đã tự đo) chỉ có nguồn diễn đàn, không phải tài liệu
chính thức, gán `[chưa xác minh]` nếu áp dụng cho model khác. Interactions
API (Omni) CHƯA từng tự gặp lỗi thật nào, hình dạng lỗi của họ API này
`[chưa xác minh]`, giả định tạm là cùng dạng `{"error": {...}}` chuẩn của
Google cho tới khi ai tự gặp lỗi thật.

## 9. Giá

Credit trên Flow UI không thuộc phạm vi file API này, xem bảng chính thức
`support.google.com/flow/answer/16526234` đã chép ở `flow-core.md` mục 2.

Giá theo giây khi gọi thẳng API `[chưa xác minh]`, số lấy qua model tóm tắt
trung gian ở phiên làm việc trước, chưa tự đối chiếu lại trang giá chính thức
Google Cloud/AI Studio, chỉ dùng để ước lượng thô:

| Model | 720p | 1080p | 4K |
|---|---|---|---|
| Veo 3.1 Standard | $0.40/giây | $0.40/giây | $0.60/giây |
| Veo 3.1 Fast | $0.10/giây | $0.12/giây | $0.30/giây |
| Veo 3.1 Lite | $0.05/giây | $0.08/giây | không có |

Lyria 3 Clip khoảng $0.04/bài, Lyria 3 Pro khoảng $0.08/bài. Giá TTS: input
$1.00/1M text token, output $20.00/1M audio token (1 giây âm thanh khoảng 25
audio token). Toàn bộ mục giá `[chưa xác minh lại lần này]`.

## Tự soát nguồn

- Mục 1 (Veo), bảng tham số và bảng ràng buộc: `[doc]`
  https://ai.google.dev/gemini-api/docs/veo. Endpoint, model id, và các field
  `aspectRatio`/`durationSeconds`/`resolution`/`personGeneration`/ràng buộc
  8 giây/vùng EU-UK-CH-MENA/24fps/lưu 2 ngày: đọc trực tiếp HTML thô
  06/09/2026, đối chiếu lại 08/09/2026. Shape chi tiết của
  `image`/`lastFrame`/`referenceImages`/`video` và field `seed`: đọc qua
  WebFetch (model tóm tắt) 08/09/2026, bằng chứng trung bình, CHƯA tự gọi API
  thật với các field này.
- Mục 2 (Omni): endpoint, `response_format`, `generation_config.video_config`,
  `previous_interaction_id`, giới hạn sửa/nối dài, bốn thẻ đặc biệt, cú pháp
  mốc thời gian và cú pháp Sources/References: `[doc]`
  https://ai.google.dev/gemini-api/docs/omni, đọc qua WebFetch ngày
  08/09/2026 bởi hai phiên độc lập cho ra cùng kết quả để lấy đủ shape request/response. Toàn bộ mục này ở
  mức bằng chứng trung bình (qua model tóm tắt, chưa tự gọi bằng key thật
  đúng endpoint `/v1beta/interactions`). Chi tiết đã tự gọi thật trước đây
  (endpoint `generateContent` cho Omni trả 404 ở `predictLongRunning`, có
  `candidates` thật) vẫn giữ nguyên bằng chứng `[live]`, chỉ không còn là
  đường script chủ động gọi nữa.
- Mục 3, 6, và phần legacy syntax cùng rate limit ở mục 4: tự gọi API bằng
  key thật, quan sát trực tiếp mã lỗi (404 sai endpoint, 429/200 đúng endpoint).
- Mục 0 và phần "Interactions API mới" ở mục 4 (TTS): tài liệu tổng hợp qua
  fetch có model tóm tắt, bằng chứng trung bình, chưa tự gọi bằng key thật
  đúng cú pháp `client.interactions.create` cho TTS.
- Mục 7: gọi `models.list` bằng key thật, 06/09/2026, bằng chứng cao nhất.
- Mục 9 (giá): qua model tóm tắt trung gian từ phiên trước, chưa tự đối chiếu
  lại lần này, gán `[chưa xác minh]`.
- Mục 5 (Lyria 3.5): thêm nguồn `[changelog]` chính thức 08/09/2026, cộng với
  hai nguồn cũ (flowmusic.app và `models.list`), nâng lên ba chiều xác nhận.
- Danh sách 30 giọng TTS: tài liệu tổng hợp qua fetch, chỉ Puck, Charon,
  Fenrir, Leda, Kore từng được tự gọi thử và không trả lỗi voiceName.
