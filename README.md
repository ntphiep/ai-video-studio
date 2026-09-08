# AI Video Studio

Plugin cho Claude Code, gói một skill sản xuất video AI qua bốn đường khác nhau.
Điểm khác biệt của skill này nằm ở **kỷ luật bằng chứng**: mọi con số trong tài
liệu đều kèm nhãn cho biết nó đến từ đâu, và những chỗ chưa kiểm chứng được ghi
thẳng là chưa kiểm chứng thay vì đoán cho đủ.

## Cài đặt

```bash
/plugin marketplace add ntphiep/ai-video-studio
/plugin install ai-video-studio@ntphiep-ai-video-studio
```

Sau khi cài, kiểm tra môi trường trước khi dùng:

```bash
python skills/ai-video-studio/scripts/doctor.py
```

Lệnh này liệt kê thứ đang có, thứ còn thiếu, và thiếu thì cài bằng lệnh nào trên
đúng hệ điều hành của bạn.

## Bốn đường sản xuất

| Đường | Dùng khi | Chi phí |
|---|---|---|
| Google Flow qua giao diện | Cần chất lượng điện ảnh, có thoại, giữ nhân vật qua nhiều cảnh | Credit Flow |
| Gemini API | Tự động hoá bằng code, sinh hàng loạt | Tính theo giây hoặc token |
| Gemini Notebook | Biến tài liệu dài thành video giảng giải | Chưa xác minh |
| Claude Code với Remotion | Motion graphics, chữ động, đồ hoạ dữ liệu | Không tốn credit Flow |

## Điều kiện chạy

Bắt buộc: Python 3.9 trở lên, `ffmpeg` và `ffprobe` trong PATH, và một khoá
Gemini API đặt ở biến môi trường `GEMINI_API_KEY` hoặc file `~/.gemini_key`.

Tuỳ chọn: `node` cùng `npx` nếu muốn đi đường Remotion, `yt-dlp` nếu muốn tải
video tham khảo, `curl` để tải file từ URL ký tên của Flow.

Skill không nhúng cứng khoá vào bất kỳ file nào, và không chứa đường dẫn riêng
của máy nào.

## Nội dung

```
skills/ai-video-studio/
├── SKILL.md                      bản đồ điều hướng, nạp mỗi phiên
├── references/
│   ├── flow-core.md              giao diện Flow, model, credit, Character, Agent
│   ├── flow-tools.md             62 công cụ trong Flow và cách tự tạo công cụ mới
│   ├── prompt-library.md         thư viện prompt nguyên văn, gom theo mục đích
│   ├── style-library.md          phong cách hình ảnh và cách sao chép style
│   ├── format-and-export.md      tỉ lệ khung hình, đổi tỉ lệ, lệnh ffmpeg đã chạy thử
│   ├── other-routes.md           Remotion, Gemini Notebook, dịch đa ngôn ngữ, làm MV
│   ├── api-guide.md              Veo, Omni, Nano Banana, TTS, Lyria
│   ├── troubleshooting.md        lỗi và cạm bẫy, tra cứu nhanh
│   ├── changelog.md              dòng thời gian chính thức của Google Flow
│   └── content-playbook.md       chọn dạng nội dung và ước chi phí
├── scripts/                      9 script Python cho đường API
└── evals/evals.json              41 bản ghi kiểm thử, giữ cả những lần từng sai
```

## Cách đọc nhãn bằng chứng

Tài liệu dùng bốn mức, và không mức nào được nâng lên cho đẹp:

| Nhãn | Nghĩa |
|---|---|
| `[live]` | Tự mở giao diện đọc DOM, tự đo bằng `ffprobe`, hoặc tự gọi API |
| `[doc]` | Đọc trực tiếp tài liệu chính thức của Google, kèm URL và ngày đọc |
| `[changelog]` | Đọc trực tiếp trang thay đổi chính thức của Google |
| `[bNN t=...s]` | Nhìn thấy trên khung hình một video hướng dẫn, kèm mốc giây |
| `[chưa xác minh]` | Chỉ một nguồn nói, chưa ai kiểm chứng lại |

## Vài thứ skill này biết mà tài liệu thường không nói

Bảng giá credit của Flow đo trực tiếp từ nhãn mà chính Flow hiện ra trước khi
sinh, nên lấy được mà không tốn đồng nào, và số đo đó khớp chính xác với bảng giá
chính thức. Video sinh ra chỉ có 16:9 và 9:16, mọi tỉ lệ khác phải đi qua công cụ
Video Resizer, và công cụ đó luôn xuất chiều rộng 1280 bất kể bạn gõ số pixel nào.

Bảng năng lực chính thức phơi ra bốn điều ngược trực giác. Chỉ Veo 3.1 Lite, bản
rẻ nhất, mới nối dài được clip. Veo 3.1 Quality, bản đắt nhất, lại không nhận
Ingredients nên không giữ được nhân vật nhất quán. Chỉ Gemini Omni Flash mới sửa
được video, và một lần sửa tốn 40 credit trong khi sinh mới một clip 10 giây chỉ
tốn 15. Còn 1080p và 4K không phải mức để sinh mà là mức để nâng clip đã có.

Không có nguồn nào một mình là đủ. Trang `flow.google.com/changelogs` cho biết một
tính năng giao diện có từ bao giờ và cho gói nào, nhưng nó đi chậm hơn blog chính
thức: ngày 08/09/2026 trang đó vẫn dừng ở mục ngày 26/08/2026 trong khi blog và
changelog của Gemini API đã có sáu mục mới. Bản mirror ở `labs.google` còn thiếu
mục mới nhất. Vì vậy skill đọc bốn nguồn song song, liệt kê đầy đủ trong SKILL.md.

## Bộ eval

41 bản ghi, trong đó mười ba bản mang trạng thái `FAIL rồi mới PASS`. Chữ FAIL được
giữ nguyên có chủ đích, để không xoá dấu vết một bản ghi từng sai. Hai nguyên tắc
cho mọi eval về script. Thứ nhất, parse được cú pháp **không phải** bằng chứng,
phải chạy thật và kiểm file đầu ra. Thứ hai, một agent báo PASS cũng **không phải**
bằng chứng: đã có trường hợp bài kiểm của agent khớp với code chứ không khớp với
tài liệu, nên nó không bao giờ chạm vào nhánh hỏng.

## Giấy phép

MIT. Xem file LICENSE.
