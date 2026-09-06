# Tỉ lệ khung hình và chuẩn xuất video (verify 06/09/2026)

File này gộp và thay thế phần còn dùng được của `format-and-export.md` và
bản export-spec cũ, nay đã gỡ khỏi skill. Mọi con số đều kèm nguồn; phần chưa ai đo lại được gắn
`[chưa xác minh]`, không đoán.

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

## 7. Watermark

Menu tài khoản Flow hiện dòng nguyên văn **"Visible watermarking is required
in your region"**. Đối chiếu trên frame thật: mọi clip đều có một dấu lấp
lánh nhỏ ở góc dưới bên phải, đúng vị trí ràng buộc theo khu vực này, không
tắt được từ giao diện. Ngoài dấu hiện có, theo hiểu biết chung thì Google còn gắn thêm SynthID vô
hình, nhưng đợt xác minh này KHÔNG đọc lại trang công bố nào của Google về
SynthID, và không tư liệu nào thu thập được nhắc tới chuỗi đó `[chưa xác minh]`.
Muốn khẳng định thì phải mở trang công bố chính thức và dẫn URL.

Hệ quả khi dựng: chừa lề an toàn ở góc dưới bên phải khi crop hoặc đặt chữ
đè, vì cắt trúng dấu watermark khi crop giữa khung chỉ là hệ quả ngoài ý
muốn, không phải cách gỡ watermark hợp lệ.

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
- Watermark: `format-and-export.md` bản cũ mục 6, đọc menu tài khoản Flow và
  quan sát frame thật.
- Facebook và các giới hạn thời lượng nền tảng: chưa tìm thấy nguồn trong
  batch video hay tài liệu chính thức đã đọc, gắn [chưa xác minh].
