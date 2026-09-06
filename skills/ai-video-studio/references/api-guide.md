# API Guide: Gemini (Veo, Omni, Nano Banana, TTS, Lyria)

Tra cứu endpoint, schema, model id và giới hạn để gọi trực tiếp Gemini API. File
này gộp và thay thế trọn ba file cũ đã bị gỡ khỏi skill. Chuyện
đường Google Flow UI (credit, voice UI, Flow Music) nằm ở `flow-core.md` và
`flow-tools.md`, không lặp lại ở đây.

## 0. Cảnh báo đầu tiên: Google chạy song song hai API khác cú pháp

Google hiện có **hai họ API khác cú pháp cho cùng một việc**. Nhầm họ là mọi ví
dụ đều sai (sai field, sai case, ra lỗi 400).

| Họ API | Cách gọi | Case field | Dùng cho |
|---|---|---|---|
| **Interactions API (mới)** | `client.interactions.create(...)` | snake_case (`voice`, `speech_config`) | Omni, Nano Banana theo tài liệu tổng hợp, mức bằng chứng trung bình, chưa tự gọi bằng key thật theo đúng cú pháp này |
| **Generate Content API (cũ, tài liệu gọi là "Legacy")** | `models/{model}:generateContent` | camelCase (`responseModalities`, `speechConfig`) | Omni, Nano Banana, TTS. Đã tự gọi bằng key thật và xác nhận endpoint tồn tại (mục 2, 3, 4) |
| Riêng biệt, không thuộc hai họ trên | `models/{model}:predictLongRunning` | camelCase (`instances`, `parameters`) | Chỉ Veo 3.1, đã verify từ HTML thô trang doc Veo |

Toàn bộ ví dụ trong file này dùng **Generate Content API** cho Omni, Nano
Banana, TTS (đã tự gọi và xác nhận endpoint tồn tại, 429 do hết quota vẫn tính
là đúng endpoint, khác 404 là sai endpoint) và riêng Veo dùng
`predictLongRunning`. Cú pháp Interactions API được ghi ở mục 4 cho TTS vì tài
liệu tổng hợp nói đây là đường song song, nhưng chưa tự thử bằng key thật.

## Base URL

```
https://generativelanguage.googleapis.com/v1beta
```

## 1. Video: Veo 3.1

Endpoint (đã verify từ HTML thô trang `ai.google.dev/gemini-api/docs/veo`,
06/09/2026):
```
POST {BASE_URL}/models/{MODEL}:predictLongRunning
```

Truyền API key được CẢ HAI cách đều chạy: header `x-goog-api-key: {GEMINI_API_KEY}`
hoặc tham số trên URL `?key={GEMINI_API_KEY}`. Đánh đổi: đặt key trên URL thì
key lọt vào log của server và vào lịch sử shell, nên header an toàn hơn. Các
script hiện có trong skill (`generate_audio.py`, `generate_image.py`,
`generate_video.py`, `write_script.py`) đều đang dùng dạng `?key=`.

Schema:
```json
{
  "instances": [
    {"prompt": "A yellow cat waving on a sunny balcony, golden hour, realistic"}
  ],
  "parameters": {
    "aspectRatio": "16:9",
    "durationSeconds": "8"
  }
}
```

- `durationSeconds` là **CHUỖI** `"4"`, `"6"` hoặc `"8"` (không phải số
  nguyên), nguyên văn tài liệu. Bắt buộc là `"8"` khi dùng video extension,
  reference images, hoặc độ phân giải 1080p/4k.
- `aspectRatio`: chỉ `"16:9"` (mặc định) và `"9:16"`, không có 21:9, 4:3.
- `personGeneration`: text-to-video và extension chỉ nhận `"allow_all"`;
  image-to-video, interpolation, reference images chỉ nhận `"allow_adult"`.
- `resolution`: `"720p"` (mặc định), `"1080p"`, `"4k"` (không có ở Lite);
  extension giới hạn 720p; càng cao độ phân giải càng lâu và càng đắt.
- `numberOfVideos` xuất hiện trong ví dụ chính thức (giá trị `1`), nhưng một
  lần gọi thật trước đây kèm field này bị từ chối 400, chưa rõ do field nào
  khác trong payload cũ. Khuyến nghị: bỏ hẳn field này, để mặc định 1 video.
- `negativePrompt` và `seed` KHÔNG tìm thấy trong tài liệu (đã grep toàn bộ
  HTML thô, không ra). Khẳng định nào về hai tham số này phải gán
  `[chưa xác minh]`.

Model id: `veo-3.1-generate-preview` (Standard/"Quality"),
`veo-3.1-fast-generate-preview` (Fast), `veo-3.1-lite-generate-preview` (Lite).
`veo-3.0-generate-001` ghi "Deprecated" trên trang doc và không còn xuất hiện
khi gọi `models.list` bằng key thật (06/09/2026), đừng dùng.

Luồng: POST trả `"name"` (operation name). Poll `GET {BASE_URL}/{name}` cho
tới khi `"done": true`, lấy uri video từ `response.video.uri`.

## 2. Video: Gemini Omni Flash (khác Veo)

Model id: `gemini-omni-1.1-flash`. Không dùng `predictLongRunning`, đã verify
live: trả 404 "not supported for predictLongRunning". Endpoint đúng là
`generateContent`, trả về đồng bộ (candidates), không cần poll.

```
POST {BASE_URL}/models/gemini-omni-1.1-flash:generateContent
```

```json
{
  "contents": [{"parts": [{"text": "Create one 8-second video. ..."}]}],
  "generationConfig": {"responseModalities": ["VIDEO"]}
}
```

Không có tham số thời lượng riêng trong schema. Cách đặt thời lượng đã verify
là viết thẳng vào prompt, ví dụ `"Create one 8-second video. ..."`, đã đo bằng
ffprobe ra đúng 8.000000 giây trên file thật. Về thời lượng hợp lệ ở cấp API: mới **tự đo được đúng một giá trị là 8 giây**,
cho ra file 8.000000 giây. Bốn mức 4, 6, 8, 10 là mức của **giao diện Flow**,
chưa ai thử qua API, nên `[chưa xác minh]` với ba mức còn lại.

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
mới nhất, xác nhận hai chiều: trang flowmusic.app gọi đây là "our latest
frontier music model, Lyria 3.5", và `models.list` bằng key thật cũng trả
đúng id này).

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
chính thức, gán `[chưa xác minh]` nếu áp dụng cho model khác.

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

- Mục 1 (Veo): đọc trực tiếp HTML thô `ai.google.dev/gemini-api/docs/veo`,
  06/09/2026. Bằng chứng cao nhất, không qua model tóm tắt.
- Mục 2, 3, 6, và phần legacy syntax cùng rate limit ở mục 4: tự gọi API bằng
  key thật, quan sát trực tiếp mã lỗi (404 sai endpoint, 429/200 đúng endpoint).
- Mục 0 và phần "Interactions API mới" ở mục 4: tài liệu tổng hợp qua fetch có
  model tóm tắt, bằng chứng trung bình, chưa tự gọi bằng key thật đúng cú pháp
  `client.interactions.create`, gán `[chưa xác minh]`.
- Mục 7: gọi `models.list` bằng key thật, 06/09/2026, bằng chứng cao nhất.
- Mục 9 (giá): qua model tóm tắt trung gian từ phiên trước, chưa tự đối chiếu
  lại lần này, gán `[chưa xác minh]`.
- Danh sách 30 giọng TTS: tài liệu tổng hợp qua fetch, chỉ Puck, Charon,
  Fenrir, Leda, Kore từng được tự gọi thử và không trả lỗi voiceName.
