# Tỉ lệ khung hình và chuẩn xuất video (verify 06/09/2026, cập nhật doc chính thức 08/09/2026)

File này gộp và thay thế phần còn dùng được của `format-and-export.md` và
bản export-spec cũ, nay đã gỡ khỏi skill. Mọi con số đều kèm nguồn; phần chưa ai đo lại được gắn
`[chưa xác minh]`, không đoán. Mục 4.1, 7 và 8 cập nhật ngày 08/09/2026 dựa trên các trang
hỗ trợ chính thức của Google, đọc trực tiếp bằng WebFetch.

<!-- MUCLUC:BAT-DAU (sinh bang scripts/gen_toc.py, dung sua tay) -->
**Mục lục** (số dòng để đọc thẳng đúng đoạn, không cần nạp cả file)

- 1. Ba tầng tỉ lệ khung hình — dòng 24
- 2. Video Resizer — bảng đo thật bằng ffprobe — dòng 40
- 3. Ba quy luật bắt buộc phải biết trước khi dùng Resizer — dòng 57
- 3b. Menu tải về: nội dung thật, đo ngày 08/09/2026 `[live]` — dòng 86
- 4. Độ phân giải và thời lượng — chỉ Omni chọn được, ba model Veo thì không — dòng 125
- 5. Lệnh ffmpeg đã chạy thật (không phải chép từ doc) — dòng 183
- 6. Chuẩn xuất theo từng nền tảng — dòng 228
- 7. Định dạng video tải lên Flow — dòng 253
- 8. Watermark — mục quan trọng vì Việt Nam nằm trong vùng bắt buộc — dòng 261
- 9. Đăng thẳng lên YouTube bằng Composio MCP `[live 09/09/2026]` — dòng 300
- Tự soát nguồn — dòng 341

<!-- MUCLUC:KET-THUC -->
## 1. Ba tầng tỉ lệ khung hình

Flow có ba con đường ra tỉ lệ khác nhau, không được gộp làm một:

| Tầng | Nơi chọn | Tỉ lệ có được |
|---|---|---|
| (a) Sinh VIDEO trực tiếp trong Flow | Composer chính, Agent settings mục Video generation default | Đúng 2 lựa chọn: **16:9, 9:16** |
| (b) Sinh ẢNH trực tiếp trong Flow | Composer chính, Agent settings mục Image generation default | Đúng 5 lựa chọn: **16:9, 4:3, 1:1, 3:4, 9:16** |
| (c) Tool Video Resizer (đổi tỉ lệ video đã có) | Tools > Templates > Video Resizer | Đúng 6 mục Output Ratio: **9:16, 16:9, 1:1, 4:5, 21:9, Custom** |

Nguồn (a) và (b): đọc DOM panel Agent settings trực tiếp, đồng thời đã thử ép
4:3 cho video bằng prompt hai lần và bị agent từ chối, khớp với dropdown.
Nguồn (c): đọc DOM tool Video Resizer, số đo Video Resizer ngày 06/09/2026. Video KHÔNG có
đường nào ra 4:3, 3:4, 21:9 hay Custom khi sinh trực tiếp; muốn các tỉ lệ đó
phải sinh 16:9 hoặc 9:16 trước rồi đưa qua Video Resizer.

## 2. Video Resizer — bảng đo thật bằng ffprobe

Nguồn video test: "Fisherman casting net on river", 640x360, 8.0 giây (trừ
dòng có ghi chú khác). Đo ngày 06/09/2026, `ffprobe.exe` 9.0.1 trên file tải
về, mức bằng chứng cao nhất trong tài liệu này.

| Output Ratio | Alignment | Kích thước ffprobe thật | Thời lượng | File |
|---|---|---|---|---|
| 4:5 | FILL | 1280 x 1600 | 8.000s | flow_coffee_explainer_4x5_resized.mp4 |
| 1:1 | FIT | 1280 x 1280 | 8.000s | flow_mekong_1x1_resized.mp4 |
| 21:9 | FILL | 1280 x 540 | 8.000s | flow_mekong_21x9_resized.mp4 |
| Custom 1440x1080 (gõ vào) | FILL | 1280 x 960 | 8.000s | flow_mekong_custom_4x3.mp4 |

FILL phóng to cho đầy khung rồi cắt phần thừa (hệ số zoom hiện ngay trên
khung). FIT giữ nguyên toàn bộ khung hình, thêm viền đen, hệ số giữ 1.00x.
Xuất xong Video Resizer ghi ngược vào gallery project, không tải thẳng về máy.

## 3. Ba quy luật bắt buộc phải biết trước khi dùng Resizer

1. **Chiều rộng đầu ra của Video Resizer luôn luôn là 1280px**, bất kể tỉ lệ
   chọn gì; chiều cao = 1280 chia cho tỉ lệ. Đã loại bỏ giả thuyết "gấp đôi
   nguồn" bằng phép thử độc lập: nạp một file 1280x1280 làm nguồn, đổi sang
   16:9, kết quả vẫn ra 1280x720 chứ không phải 2560x1440. Đã thử với hai
   chiều rộng nguồn khác nhau (640 và 1280), cùng ra 1280.
   **[chưa xác minh]** với nguồn rộng 1920px hoặc clip 1080p thật. Nếu quy
   luật giữ nguyên, đưa clip 1080p vào Video Resizer sẽ bị hạ độ phân giải
   xuống 1280px chiều rộng. Đo lại file xuất ra trước khi tin.
2. **Ở chế độ Custom, tool chỉ lấy TỈ LỆ, không lấy số pixel đã gõ.** Gõ
   1440x1080 (tỉ lệ 4:3) ra đúng 1280x960, đúng tỉ lệ 4:3 nhưng sai hoàn toàn
   số pixel đã nhập. Hai ô input WIDTH/HEIGHT có min=1, max=4096, mặc định
   1080x1080; dòng chữ "Ratio: 4:3 (1.33:1)" chỉ cập nhật khi rời ô (blur),
   không cập nhật khi đang gõ.
3. **Tên asset trong gallery ghi kích thước danh nghĩa, không phải kích thước
   thật.** Chỉ có tỉ lệ là khớp, số pixel trong tên luôn sai, phải ffprobe
   file thật mới biết:

| Tên asset trong gallery | Kích thước THẬT đo bằng ffprobe |
|---|---|
| Resized_1440x1080_... | 1280 x 960 |
| Resized_2560x1080_... | 1280 x 540 |
| Resized_1080x1080_... | 1280 x 1280 |
| Resized_1080x1350_... | 1280 x 1600 |

Mọi lần resize đều giữ 24fps, giữ audio AAC 48kHz stereo, giữ đúng thời
lượng gốc, và tool vừa đổi tỉ lệ vừa **upscale** (nguồn 640 lên 1280).

## 3b. Menu tải về: nội dung thật, đo ngày 08/09/2026 `[live]`

Nâng độ phân giải KHÔNG phải một nút riêng trên giao diện. Nó nằm trong menu
`Download media` ở thanh trên khi mở một clip. Nội dung menu đổi theo độ phân giải gốc của
clip đó.

Clip gốc **360p**, menu hiện đúng ba mục nguyên văn:

| Mục | Trạng thái |
|---|---|
| `270p Animated GIF` | dùng được |
| `360p Original size` | dùng được |
| `720p Upscaled` | dùng được |

Clip gốc **720p**, menu hiện đúng bốn mục nguyên văn:

| Mục | Trạng thái trên gói Pro |
|---|---|
| `270p Animated GIF` | dùng được |
| `720p Original size` | dùng được |
| `1080p Upscaled` | **dùng được** |
| `4K Upscaled` | **bị khoá**, kèm link `Upgrade` trỏ sang trang nâng gói |

Ba điều rút ra.

Thứ nhất, đây là bằng chứng trực tiếp rằng **Flow đã xuất được 1080p ngay trên gói Pro**, và
4K tồn tại nhưng khoá cho tới khi lên Ultra. Trước ngày 08/09/2026 tài liệu này nói Flow chỉ
có 720p, điều đó đã sai kể từ bản cập nhật 27/08/2026.

Thứ hai, có một mức không ai nhắc tới trong tài liệu chính thức: **`270p Animated GIF`**.
Đây là đường xuất ảnh động sẵn có, tiện cho ảnh xem trước và cho nội dung nhúng vào bài viết.

Thứ ba, **menu này KHÔNG hiện giá credit**. Bảng giá chính thức nói nâng lên 1080p miễn phí
cho người trả phí và nâng lên 4K tốn 50 credit chỉ dành cho Ultra, nhưng giao diện không lặp
lại con số đó ở chỗ bấm. Riêng mức `720p Upscaled` từ nguồn 360p thì bảng giá chính thức
không có dòng nào tương ứng, nên giá của nó `[chưa xác minh]`. Phép đo ngày 08/09/2026 cố ý
KHÔNG bấm vào các mục này để tránh kích hoạt một hành động tốn credit hoặc không đảo ngược
được, nên phần giá vẫn là khoảng trống bằng chứng.

## 4. Độ phân giải và thời lượng — chỉ Omni chọn được, ba model Veo thì không

Đọc trực tiếp panel cài đặt prompt (nhãn "Generating will use N credits"
hiện trước khi sinh, không tốn credit để đọc), khớp lại với trang giá chính
thức support.google.com/flow/answer/16526234:

| Model | Có chọn độ phân giải? | Có chọn thời lượng? |
|---|---|---|
| Omni 1.1 Flash | Có: 360p hoặc 720p | Có: 4s, 6s, 8s, 10s |
| Veo 3.1 Lite / Fast / Quality | Không | Không, cố định theo model |

Bảng credit Omni theo độ phân giải và thời lượng:

| Độ phân giải | 4s | 6s | 8s | 10s |
|---|---|---|---|---|
| 360p | 4 | 5 | 6 | 7 |
| 720p | 7 | 10 | 12 | 15 |

Ba model Veo tính credit cố định mỗi lần sinh, không phụ thuộc thời lượng
hay độ phân giải trên UI: Lite 10, Fast 20, Quality 100 (giá thường của gói
Pro; giá Ultra bằng đúng một nửa cho Lite và Fast, tức 5 và 10, xem bảng giá đo trực tiếp trên tài khoản ngày 06/09/2026).

Lý do chỉ Omni có 360p: tính năng "Omni 360p has landed" mới ra ngày
26/08/2026, tức khoảng hai tuần trước khi đo, theo changelog chính thức tại
flow.google.com/changelogs. Không có tiêu đề nào trong 40 mục changelog nhắc tới 360p cho Veo. Nội dung chi tiết từng mục là ảnh hoặc video nên chưa đọc được, vì vậy đây chỉ là bằng chứng ở mức tiêu đề, không phải bằng chứng đã quét hết nội dung. Ba model Veo không thấy có mốc 360p trong toàn bộ
40 mục changelog. Mốc thời lượng 4s/6s xuất hiện từ changelog "Link Sharing
and 4s/6s Videos" ngày 21/04/2026.

Ở cấp giao diện chọn khi generate, thời lượng có 4 mức cố định 4s/6s/8s/10s,
8s thường gắn nhãn "Recommended". Video dài hơn 10 giây không ghép được
trong editor nội bộ của Flow (cảnh báo "Videos longer than 10s can't be
edited"), phải ghép ngoài bằng Scenebuilder, Stringout Creator, hoặc CapCut.

### 4.1 Nâng độ phân giải sau khi sinh — thay đổi lớn, cập nhật 08/09/2026

**Phần này đã lạc hậu trong bản trước của skill: không phải chỉ có 720p.** Bảng ở trên
chỉ nói về độ phân giải CHỌN ĐƯỢC LÚC SINH (native khi generate). Ngoài lúc sinh, Flow còn
cho nâng độ phân giải SAU KHI ĐÃ CÓ VIDEO, áp dụng cho MỌI MODEL kể cả ba model Veo, theo
trang giá chính thức `[doc, đọc 08/09/2026]`
https://support.google.com/flow/answer/16526234?hl=en:

| Nâng lên | Giá | Điều kiện gói |
|---|---|---|
| 1080p | Miễn phí | Người dùng trả phí (Plus/Pro/Ultra) |
| 4K | 50 credit | Chỉ Google AI Ultra |

Trang giá chính thức KHÔNG nói rõ lượt nâng độ phân giải thất bại có mất credit hay không.

**Quy trình tiết kiệm nhất hiện nay: nháp ở 360p rồi nâng độ phân giải, KHÔNG sinh lại từ
đầu.** Đây là thay đổi lớn về cách làm so với trước, khi skill còn khuyên sinh thẳng ở độ
phân giải mong muốn. Vì Omni 360p rẻ hơn nhiều so với 720p ở cùng thời lượng (4 đến 7
credit so với 7 đến 15 credit, xem bảng credit ở trên), quy trình khuyến nghị là: sinh nháp
ở 360p để duyệt bố cục và chuyển động trước, chọn bản ưng ý, rồi mới nâng lên 1080p (miễn
phí nếu có gói trả phí) hoặc 4K (50 credit, chỉ Ultra), thay vì sinh lại toàn bộ ở độ phân
giải cao ngay từ đầu và tốn credit cho những lần thử sai. Nguồn: blog Google Labs ngày
27/08/2026 "New creative controls in Google Flow" và trang giá chính thức trên
`[doc, đọc 08/09/2026]`.

## 5. Lệnh ffmpeg đã chạy thật (không phải chép từ doc)

Hai lệnh dưới đã chạy bằng ffmpeg 9.0.1 trên máy, kiểm bằng ffprobe, giữ
nguyên văn từ bản export-spec cũ, nay đã gỡ khỏi skill cũ vì vẫn đúng:

```bash

# 16:9 -> 9:16, cắt hai bên rồi đưa về khung Shorts chuẩn

# test thật: 1280x720 -> ra đúng 720x1280
ffmpeg -i final.mp4 -vf "crop=ih*9/16:ih,scale=720:1280" -c:a copy final_916.mp4

# 9:16 -> 16:9, giữ trọn khung, thêm viền đen hai bên

# test thật: 720x1280 -> ra đúng 1920x1080
ffmpeg -i vertical.mp4 -vf "scale=-2:1080,pad=1920:1080:(ow-iw)/2:0" -c:a copy out_169.mp4
```

**Cảnh báo giữ nguyên, lệnh cũ đã HỎNG, đừng dùng lại:** bản trước ghi
`pad=iw+2*trunc(oh*iw/ih/2):iw*9/16:...`. Chạy thật trên clip 720x1280,
ffmpeg báo lỗi *"Padded dimensions cannot be smaller than input dimensions"*
và tạo ra file 0 byte, vì chiều cao pad tính ra `iw*9/16 = 405`, nhỏ hơn
chiều cao nguồn 1280.

Lệnh xuất chuẩn cho re-encode khi cần (không đổi tỉ lệ, chỉ chuẩn hoá
codec/bitrate):

```bash
ffmpeg -i final.mp4 \
  -c:v libx264 -pix_fmt yuv420p -r 24 -b:v 8M \
  -c:a aac -ar 48000 -ac 2 \
  -movflags +faststart -preset medium \
  output_youtube.mp4
```

`scripts/assemble_video.py` KHÔNG dùng cố định `-b:v 8M`: nhánh không có
narration/nhạc nền không đặt `-b:v` (giữ nguyên bitrate mã hoá lại theo mặc
định của libx264), còn nhánh có narration hoặc nhạc nền mới chọn bitrate,
và chọn theo CẠNH NGẮN của khung hình, không theo tỉ lệ khung: cạnh ngắn
từ 1080 trở lên thì `8M`, dưới 1080 thì `5M`.

Thông số file Flow xuất ra đo thật (04/09/2026 đến 06/09/2026): MP4, H.264,
24fps chính xác (`r_frame_rate=24/1`), AAC 48kHz stereo, container không cần
re-encode khi tải lên YouTube.

## 6. Chuẩn xuất theo từng nền tảng

| Nền tảng | Tỉ lệ | Cách đạt tỉ lệ | Độ dài hợp lý |
|---|---|---|---|
| YouTube ngang | 16:9 | Sinh native | Tùy nội dung, thường 8 đến 15 phút [chưa xác minh giới hạn hiện hành] |
| YouTube Shorts | 9:16 | Sinh native | [chưa xác minh giới hạn hiện hành] |
| TikTok | 9:16 | Sinh native | 15 đến 60 giây [kinh nghiệm cộng đồng, không phải số liệu nền tảng] |
| Instagram Reels | 9:16 | Sinh native | 15 đến 30 giây [kinh nghiệm cộng đồng, không phải số liệu nền tảng] |
| Instagram feed dọc | 4:5 | Video Resizer, verify 1280x1600 | Tùy nội dung |
| Instagram feed vuông | 1:1 | Video Resizer, verify 1280x1280 | Tùy nội dung |
| Facebook feed / Reels | [chưa xác minh] | [chưa xác minh] | [chưa xác minh] |
| Ảnh bìa điện ảnh 21:9 | 21:9 | Video Resizer, verify 1280x540 | Tùy nội dung |

Facebook chưa có nguồn nào trong batch video hay tài liệu chính thức đã đọc
xác nhận riêng; không suy diễn từ Instagram/TikTok để lấp chỗ trống.

Nguyên tắc chi phí đã kiểm bằng ledger thật (không phải suy đoán): sinh một
lần ở 9:16 rồi dùng Video Resizer ra thêm bản 1:1 và 4:5 không tốn thêm
credit, chỉ tốn thời gian xử lý. Số dư trước/sau một phiên chạy Video Resizer
và Type Overlays lệch đúng bằng tổng các lần sinh video xen giữa, hai tool
này không hề xuất hiện riêng trong ledger.

Thumbnail: khuyến nghị 16:9, 1280x720, JPG/PNG/GIF dưới 2MB [con số phổ
biến, chưa đối chiếu lại trang chính thức YouTube ở lần verify này].

## 7. Định dạng video tải lên Flow

Nguồn: https://support.google.com/flow/answer/16935718 `[doc, đọc 08/09/2026]`

Định dạng chấp nhận: `.mov`, `.mp4`, `.avi`, `.wmv`. Giới hạn: tối đa 60 giây và tối đa
1GB mỗi file. Áp dụng cho việc tải video lên Flow (ví dụ để dùng làm video tham chiếu,
sửa, hoặc đưa qua Video Resizer), không phải video do Flow tự sinh ra.

## 8. Watermark — mục quan trọng vì Việt Nam nằm trong vùng bắt buộc

### 8.1 Watermark hiển thị tự động bật ở Việt Nam

Nguồn: https://support.google.com/flow/answer/16353333?hl=en `[doc, đọc 08/09/2026]` nói rõ:
**watermark hiển thị tự động bật ở Ấn Độ, Hàn Quốc, và Việt Nam.** Đây là vùng bắt buộc
theo điều kiện dùng Flow, không phải tuỳ chọn mặc định có thể lờ đi.

Đối chiếu với quan sát trực tiếp trên giao diện `[live]`, đo ngày 06/09/2026: menu tài
khoản Flow hiện dòng nguyên văn **"Visible watermarking is required in your region"**, và
mọi clip xuất ra đều có một dấu lấp lánh nhỏ ở góc dưới bên phải, không tìm thấy nút tắt
trong giao diện tại thời điểm đo. Hai nguồn độc lập, một `[doc]` một `[live]`, khớp nhau,
đây là tín hiệu mạnh xác nhận Việt Nam nằm trong vùng bắt buộc watermark hiển thị.

### 8.2 [chưa xác minh] Có tin nói tắt được watermark hiển thị từ 14/08/2026

Nguồn: https://techcrunch.com/2026/08/14/google-will-now-allow-users-to-remove-visible-watermark-from-its-ai-generations/
— đây là nguồn bên thứ ba, KHÔNG phải trang chính thức của Google, nên toàn bộ đoạn này
gắn nhãn `[chưa xác minh]`.

Theo tin trên, từ ngày 14/08/2026 Google cho phép tắt watermark HIỂN THỊ trong phần
Settings, mục "Media Watermark", áp dụng cho nội dung của Nano Banana, Omni và Lyria
trong cả Gemini và Flow. Tin này ra TRƯỚC thời điểm quan sát UI trực tiếp ngày 06/09/2026
ở mục 8.1, vốn không thấy nút tắt và vẫn thấy dòng cảnh báo bắt buộc watermark — có thể
do đợt đo 06/09/2026 chưa mở đúng mục Settings > Media Watermark, hoặc tính năng chưa bật
cho tài khoản đo, hoặc tin bên thứ ba không chính xác. Chưa ai mở lại đúng màn hình
Settings > Media Watermark để kiểm chứng trực tiếp. Trước khi báo với khách hàng là
watermark tắt được, phải tự mở Settings và xác nhận bằng mắt, đừng dựa vào tin này.

**Dù tắt được watermark hiển thị, SynthID vô hình và metadata C2PA vẫn giữ nguyên và
KHÔNG tắt được**, theo cùng nguồn bên thứ ba trên, vẫn `[chưa xác minh]` vì chưa đọc được
trang công bố chính thức nào của Google (kể cả trang SynthID tại deepmind.google/models/synthid/)
xác nhận lại chi tiết này.

### 8.3 Hệ quả khi dựng

Chừa lề an toàn ở góc dưới bên phải khi crop hoặc đặt chữ đè, vì cắt trúng dấu watermark
khi crop giữa khung chỉ là hệ quả ngoài ý muốn, không phải cách gỡ watermark hợp lệ.

## 9. Đăng thẳng lên YouTube bằng Composio MCP `[live 09/09/2026]`

Trước bản này tài liệu chỉ ghi hai đường đăng: chuột phải trong Flow chọn
`Publish to YouTube`, hoặc tải về rồi tự đăng tay. Có đường thứ ba đã chạy thật,
tự động hoàn toàn, dùng được cho video render bằng Remotion tức thứ Flow không biết tới.

**Nút thắt:** công cụ `YOUTUBE_UPLOAD_VIDEO` và `YOUTUBE_MULTIPART_UPLOAD_VIDEO` của
Composio đều bắt trường `videoFile` phải là object có `s3key`, tức file đã nằm sẵn
trên S3 của Composio. Chúng KHÔNG nhận đường dẫn file trên máy. Composio MCP chạy
remote tại `https://connect.composio.dev/mcp` nên nó cũng không đọc được ổ đĩa của bạn.
Helper `upload_local_file()` trong sandbox chỉ thấy file trong chính sandbox, không giúp gì.

**Cách vượt, bốn bước, đã chạy thật:**

1. Trong `COMPOSIO_REMOTE_WORKBENCH`, xin một presigned URL:
   `POST {BACKEND_URL}/api/v3/tool_router/internal/presigned_url` với body
   `{"operation": "upload"}` và header `x-session-access-key: $COMPOSIO_WORKBENCH_ACCESS_KEY`.
   Trả về `upload_url`, `key`, `download_url`, hạn **3600 giây**.
2. Từ máy mình đẩy file thẳng lên: `curl -T <file> -H "Content-Type: video/mp4" "<upload_url>"`.
   URL chỉ ký theo header `host` nên không cần khớp Content-Type lúc ký.
3. Đối chiếu: tải `download_url` về trong sandbox, so số byte với file gốc, kiểm 16 byte
   đầu có chuỗi `ftyp`. Đừng bỏ bước này, đăng nhầm file hỏng là công khai luôn.
4. Gọi `YOUTUBE_MULTIPART_UPLOAD_VIDEO` với `videoFile.s3key` chính là `key` ở bước 1.

Đo thật: file 37.886.929 byte đẩy lên hết **8 giây**, khớp từng byte. Không cần bất kỳ
dịch vụ lưu trữ bên thứ ba nào.

**Bốn cạm bẫy đã vấp:**

- Tham số của `YOUTUBE_GET_VIDEO_DETAILS_BATCH` là `id`, KHÔNG phải `ids`. Truyền sai ra
  lỗi 400 `Following fields are missing: {'id'}`.
- YouTube tự gán `defaultAudioLanguage` thành `en-US` kể cả khi lời đọc là tiếng Việt.
  `YOUTUBE_UPDATE_VIDEO` của Composio KHÔNG có trường này, muốn sửa phải vào YouTube Studio
  đổi tay. Bỏ qua thì video bị giảm cơ hội đề xuất cho người Việt.
- **Mốc chương trong mô tả phải lấy từ thời lượng RENDER THẬT, không lấy từ kịch bản.**
  Kịch bản đặt mục tiêu 180 giây, bản render ra 164,47 giây, lệch 17 giây làm mọi mốc từ
  chương thứ tư trở đi sai hết. Nguồn đúng là `durations.json`: cộng dồn `durationInFrames`
  rồi chia `fps`. Đây là lỗi đã mắc thật và phải sửa sau khi video đã công khai.
- Nếu tài khoản Composio có nhiều kênh YouTube, `account_selection` là `required`. Phải
  truyền đúng alias hoặc account id, không thì nó dùng kênh mặc định và đăng nhầm kênh.

## Tự soát nguồn

- Ba tầng tỉ lệ và bảng 6 Output Ratio của Video Resizer: số đo Video Resizer ngày 06/09/2026,
  đọc DOM trực tiếp 06/09/2026.
- Bảng đo ffprobe mục 2 và ba quy luật mục 3: số đo Video Resizer ngày 06/09/2026, đo trực
  tiếp bằng ffprobe.exe 9.0.1 trên file tải về.
- Bảng credit Omni và Veo mục 4: bảng giá đo trực tiếp trên tài khoản ngày 06/09/2026, đọc nhãn credit
  trong panel cài đặt, khớp với support.google.com/flow/answer/16526234.
- Mốc ngày 360p và 4s/6s: `changelog.md`, flow.google.com/changelogs,
  đọc 06/09/2026.
- Hai lệnh ffmpeg mục 5 và cảnh báo lệnh hỏng: bản export-spec cũ, nay đã gỡ khỏi skill bản cũ, đã
  chạy thật bằng ffmpeg 9.0.1, kiểm bằng ffprobe.
- Thông số file Flow (H.264/24fps/AAC 48kHz): `format-and-export.md` bản cũ mục 4,
  đo bằng ffprobe trên nhiều file trong `output/`.
- Nâng độ phân giải 1080p/4K mục 4.1: đọc trực tiếp
  https://support.google.com/flow/answer/16526234?hl=en và blog Google Labs 27/08/2026
  "New creative controls in Google Flow", ngày đọc 08/09/2026.
- Định dạng video tải lên mục 7: đọc trực tiếp
  https://support.google.com/flow/answer/16935718, ngày đọc 08/09/2026.
- Watermark bắt buộc ở Việt Nam mục 8.1: đọc trực tiếp
  https://support.google.com/flow/answer/16353333?hl=en ngày đọc 08/09/2026, đối chiếu với
  quan sát menu tài khoản Flow và frame thật ngày 06/09/2026.
- Tin tắt watermark từ 14/08/2026 mục 8.2: nguồn bên thứ ba techcrunch.com, chưa có trang
  chính thức xác nhận, giữ nguyên nhãn [chưa xác minh].
- Facebook và các giới hạn thời lượng nền tảng: chưa tìm thấy nguồn trong
  batch video hay tài liệu chính thức đã đọc, gắn [chưa xác minh].
- Mục 9 đường đăng YouTube: tự chạy thật ngày 09/09/2026 trong phiên làm việc. Mã nguồn
  helper đọc bằng `inspect.getsource` trong sandbox Composio; presigned URL, mã trạng thái
  HTTP 200, số byte hai đầu, và id video trả về đều là output lệnh thật, không suy đoán.
