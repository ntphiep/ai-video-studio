---
name: ai-video-studio
description: >
  Sản xuất video AI toàn diện, mọi loại nội dung, mọi style, mọi format. Bốn
  đường sản xuất: Google Flow qua giao diện (Playwright, gói Free trở lên),
  Gemini API (Veo 3.1, Omni, Nano Banana, TTS, Lyria), Gemini Notebook tức
  NotebookLM cũ (video từ tài liệu), và Claude Code kết hợp Remotion (video
  dựng bằng code). Bao gồm: story nhiều nhân vật có thoại tiếng Việt, faceless
  giáo dục, Shorts, TikTok, Reels, quảng cáo UGC, ASMR, MV ca nhạc, kinetic
  typography, motion graphics, explainer, hoạt hình 2D, video đa ngôn ngữ có
  lip sync, video nhiều cảnh giữ nhân vật nhất quán. Dùng skill này khi người
  dùng muốn TẠO VIDEO AI cho bất kỳ nền tảng, style hay mục đích nào, hoặc khi
  họ nhắc "Google Flow", "flow.google.com", "veo", "omni", "nano banana",
  "shorts", "faceless", "UGC", "kinetic typography", "clone style",
  "multi-scene", "nhân vật nhất quán", "đổi tỉ lệ video", "MV", "lip sync",
  "Remotion", "NotebookLM", "Gemini Notebook". KHÔNG dùng cho việc dựng phim
  thủ công trên video có sẵn, hay cho chiến lược kênh thuần tuý.
compatibility: python 3, ffmpeg, curl, Gemini API key (env GEMINI_API_KEY), Playwright MCP cho đường giao diện
---

# ai-video-studio

Kiến thức trong skill này được rút ra từ bốn mức bằng chứng khác nhau. Hãy giữ
đúng thứ bậc đó khi trả lời người dùng, đừng nâng cấp mức tin cậy của bất cứ
điều gì.

| Mức | Nghĩa là gì | Cách nhận ra trong tài liệu |
|---|---|---|
| Cao nhất | Tự chạy, tự đo, tự đọc DOM, hoặc gọi API thật | ghi `[live]`, hoặc kèm số đo `ffprobe` |
| Cao | Đọc trực tiếp tài liệu chính thức của Google | có URL kèm ngày đọc |
| Trung bình | Nhìn thấy trên màn hình một video hướng dẫn | ghi `[bNN t=...s]` |
| Thấp | Chỉ nghe nói, hoặc nguồn bên thứ ba | ghi `[chưa xác minh]` |

## Bước 0. Chọn đường sản xuất

| Đường | Dùng khi | Chi phí | Reference |
|---|---|---|---|
| A. Google Flow qua giao diện | Cần chất lượng điện ảnh, có thoại, giữ nhân vật qua nhiều cảnh | Credit Flow | `flow-core.md` |
| B. Gemini API | Cần tự động hoá bằng code, sinh hàng loạt | Tiền theo giây hoặc theo token | `api-guide.md` |
| C. Gemini Notebook | Biến tài liệu dài thành video giảng giải | Chưa xác minh. Một số tính năng có nhãn PRO, chưa đọc được bảng giá nào | `other-routes.md` |
| D. Claude Code với Remotion | Motion graphics, chữ động, đồ hoạ dữ liệu, kiểm soát từng khung | Không tốn credit Flow, nhưng tốn TTS hoặc API ảnh của bên thứ ba nếu dùng | `other-routes.md` |

Đường A và B cho ra hình ảnh do model sinh. Đường D cho ra hình ảnh do code vẽ,
nên chính xác tuyệt đối nhưng không có chất điện ảnh. Nhiều video thật ghép cả
hai, dùng Flow cho cảnh quay và Remotion cho chữ cùng đồ hoạ.

## Bảng giá credit của Flow

Số dưới đây đọc trực tiếp từ nhãn `Generating will use N credits` mà chính Flow
hiện ra trước khi sinh, trên tài khoản gói AI Pro, ngày 06/09/2026.

| Model | 4s | 6s | 8s | 10s |
|---|---|---|---|---|
| Omni 1.1 Flash, 360p | 4 | 5 | 6 | 7 |
| Omni 1.1 Flash, 720p | 7 | 10 | 12 | 15 |
| Veo 3.1 Lite | 10 cho mỗi lần sinh, không chọn được độ phân giải lẫn thời lượng | | | |
| Veo 3.1 Fast | 20, cũng không chọn được | | | |
| Veo 3.1 Quality | 100, cũng không chọn được | | | |

Ba điều phải nhớ. Thứ nhất, **chỉ Omni mới có 360p và mới chọn được thời lượng**.
Thứ hai, clip rẻ nhất là **4 credit**, nên quỹ 50 credit mỗi ngày làm được 12
clip nháp. Với tài khoản trả phí, 50 credit này đến từ một banner khuyến mãi và
có bản ghi hạn chót, nên hãy coi là ưu đãi có thể hết chứ không phải hạn mức
cố định của gói. Thứ ba, gói Ultra có thêm mục `Veo 3.1 Lite - Lower Priority`, mà một bài
đăng mạng xã hội nói là giá 0 credit; changelog chính thức chỉ ghi tên mục chứ
không ghi con số đó. Gói Pro không có mục này và đó là **đúng thiết kế chứ không
phải lỗi**. Lưu ý thêm rằng cả người đã trả tiền Ultra cũng có trường hợp báo
không thấy mục này.

## Năm luật vàng

1. **Luôn nháp ở Omni 360p trước.** Chốt bố cục và nội dung xong mới lên 720p.
   Cách ép mạnh nhất là đặt Agent instruction, xem `flow-core.md` mục 7.3.
2. **Báo giá trước khi sinh.** Flow hiện sẵn số credit ngay trong panel cài đặt.
   Đọc con số đó và nói cho người dùng biết trước khi bấm.
3. **Prompt phải là một đoạn liền, không xuống dòng.** Xuống dòng làm Flow hiểu
   thành nhiều lệnh và sinh dư, tốn credit oan.
4. **Chữ cần chính xác từng ký tự thì đừng để model vẽ.** Trong lần tự thử duy
   nhất, model viết đúng dấu tiếng Việt nhưng đảo thứ tự cụm từ (n=1, chưa lặp
   lại). Một bài đánh giá bên thứ ba đo tiếng Nhật cũng cho kết quả rất tệ. Rủi
   ro đủ lớn để tránh, nên dùng tool Type Overlays hoặc chèn chữ khi dựng.
5. **Đo file thật trước khi nói xong.** Tải về rồi chạy `ffprobe`. Nhãn trên giao
   diện Flow có nhiều chỗ ghi sai kích thước thật.

## Giới hạn cứng cần biết ngay

| Giới hạn | Giá trị | Hệ quả | Bằng chứng |
|---|---|---|---|
| Tỉ lệ sinh video | Chỉ 16:9 và 9:16 | Mọi tỉ lệ khác phải đi qua Video Resizer | `[live]` đọc DOM, khớp doc Veo |
| Tỉ lệ sinh ảnh | 16:9, 4:3, 1:1, 3:4, 9:16 | Ảnh rộng đường hơn video | `[live]` đọc Agent settings |
| Thời lượng một clip | Omni cho chọn 4, 6, 8, 10 giây. Ba model Veo trên Flow không có ô chọn thời lượng. API Veo chỉ nhận chuỗi `"4"`, `"6"`, `"8"` | Video dài phải ghép nhiều clip | `[live]` đọc panel, cộng doc Veo đọc HTML thô |
| Video dài quá 10 giây | Không sửa được trong Flow | Giao diện có nút `Trim Automatically` | `[b22]` nguyên văn trên màn hình |
| Ô Sample Dialogue khi tạo giọng | 120 ký tự | Viết mẫu thoại thật ngắn | Bốn video độc lập xác nhận |
| Thoại trong một clip | Khoảng 10 giây, trung bình 2 dòng | Dài hơn thì giọng bị cắt | `[b22]` slide do tác giả video tự soạn, chưa tự đo |
| Số lượt sửa liên tiếp | Khoảng 4 lượt | Từ lượt thứ 5 nhân vật bắt đầu trôi | `[bên thứ ba]` jxp.com 21/05/2026, chưa tự đo |

## Bản đồ reference

Chỉ nạp đúng file cần dùng, đừng nạp hết.

| File | Nạp khi |
|---|---|
| `flow-core.md` | Làm việc trên Flow: giao diện, model, credit, Character, Agent |
| `flow-tools.md` | Cần dùng hoặc tự tạo công cụ trong Flow, 62 tool có sẵn |
| `prompt-library.md` | Cần viết prompt, hoặc cần prompt mẫu nguyên văn |
| `style-library.md` | Cần một phong cách cụ thể, hoặc cần clone style từ ảnh |
| `format-and-export.md` | Cần đổi tỉ lệ, ghép, hoặc xuất cho một nền tảng |
| `other-routes.md` | Đi đường C hoặc D, hoặc cần dịch đa ngôn ngữ, làm MV |
| `api-guide.md` | Gọi API bằng code |
| `troubleshooting.md` | Gặp lỗi, hoặc kết quả ra sai |
| `changelog.md` | Cần biết một tính năng có tồn tại không, từ bao giờ, cho gói nào |
| `content-playbook.md` | Chọn dạng nội dung, ước chi phí theo dạng video, lịch sản xuất, cảnh báo chính sách |

## Chạy bằng script

Thư mục `scripts/` có 8 file Python cho đường B, tức đường gọi API. Đây là phần
duy nhất của skill chạy được không cần trình duyệt.

| Script | Làm gì |
|---|---|
| `config.py` | Đọc key từ biến môi trường `GEMINI_API_KEY` hoặc `~/.gemini_key`, giữ danh sách model |
| `write_script.py` | Sinh kịch bản và chia shot, xuất ra `spec.json` |
| `generate_image.py` | Sinh ảnh bằng Nano Banana |
| `generate_video.py` | Sinh một clip bằng Veo hoặc Omni |
| `generate_audio.py` | Sinh giọng đọc bằng TTS và nhạc nền bằng Lyria |
| `assemble_video.py` | Nối clip, trộn tiếng, đổi tỉ lệ, xuất bản cuối |
| `upload_video.py` | Chỉ sinh file metadata JSON, không tải lên đâu cả |
| `pipeline.py` | Điều phối các bước trên theo `spec.json` |

Chạy từng bước một, đừng chạy hết một mạch, vì mỗi bước đều tốn tiền API:

```bash
python pipeline.py --spec spec.json --stage video --model omni
```

Ba điều cần biết trước khi dùng. Thứ nhất, `assemble_video.py` sẽ **dừng và báo**
nếu các clip khác độ phân giải, vì nối thẳng sẽ mất chất lượng mà không ai hay.
Thứ hai, nếu lời đọc dài hơn hình, script giữ khung hình cuối cho đủ tiếng và in
cảnh báo kèm số giây. Thứ ba, `pipeline.py` dừng ngay khi một bước con lỗi thay
vì chạy tiếp trên dữ liệu hỏng.

## Quy tắc tra cứu khi nghi ngờ

Khi người dùng hỏi một tính năng có tồn tại hay không, **đừng chỉ mở giao diện ra
xem**. Giao diện chỉ cho biết tài khoản này thấy gì, không cho biết tính năng có
tồn tại ở gói khác, vùng khác, mới ra hay vừa bị gỡ. Hãy làm song song ba việc:
tự thử trên giao diện, mở `changelog.md` cùng trang gốc
`https://flow.google.com/changelogs`, và tra tin tức gần đây.

Bài học này đến từ một lần suýt kết luận sai. Mục `Veo 3.1 Lite - Lower Priority`
không có trên tài khoản Pro, nhưng changelog chính thức ngày 10/04/2026 ghi rõ nó
tồn tại và dành riêng cho gói Ultra.

## Kịch bản thường gặp

| Người dùng muốn | Làm gì |
|---|---|
| Một clip thử nhanh | Omni 360p, 4 giây, hết 4 credit |
| Video kể chuyện nhiều cảnh | Tạo Character trước, gắn vào mọi prompt bằng nút cộng |
| Video dọc cho Shorts hoặc TikTok | Đặt 9:16 ngay từ đầu, đừng sinh 16:9 rồi cắt |
| Tỉ lệ lạ như 4:3, 21:9, hoặc số đo riêng | Sinh 16:9 rồi qua Video Resizer. Đo hai lần không thấy trừ credit, nhưng Flow vẫn cảnh báo `This Tool may consume credits` |
| Chữ tiếng Việt chính xác trên hình | Type Overlays, hoặc dựng bằng Remotion |
| Thoại tiếng Việt nghe tự nhiên | Sinh video không lồng tiếng, lồng tiếng riêng rồi ghép |
| Một video ra nhiều thứ tiếng | Đường VMEG trong `other-routes.md` |
| Video từ tài liệu dài | Gemini Notebook, mục Video Overview |
| Chữ động, biểu đồ, đồ hoạ dữ liệu | Claude Code với Remotion |

## Trước khi nói đã xong

Bắt buộc làm đủ bốn việc sau rồi mới báo hoàn thành.

1. Tải file về máy, không chỉ nhìn thấy nó nằm trong thư viện.
2. Chạy `ffprobe` và đọc ra kích thước, thời lượng, có tiếng hay không.
3. Nếu video có thoại hoặc có chữ, mở một khung hình ra xem hoặc nghe lại để đối
   chiếu với kịch bản.
4. Nói cho người dùng biết đã tiêu hết bao nhiêu credit.

Nếu bất cứ bước nào không làm được, hãy nói thẳng là chưa xác minh, đừng nói xong.
