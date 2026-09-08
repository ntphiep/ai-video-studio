# Dòng thời gian chính thức của Google Flow

Tài liệu này có HAI bảng, lấy từ hai nguồn khác nhau. Đừng trộn chúng vào nhau, vì mỗi
nguồn trả lời một loại câu hỏi khác nhau.

| Bảng | Nguồn | Trả lời câu hỏi gì |
|---|---|---|
| Bảng A, 40 mục | `flow.google.com/changelogs` | Tính năng của giao diện Flow có từ bao giờ, cho gói nào |
| Bảng B, mục mới | Changelog của Gemini API và blog chính thức | Model và API đổi gì, kể cả những thay đổi chưa lên trang changelog của Flow |

Bảng B tồn tại vì trang changelog của Flow đi CHẬM HƠN blog và changelog API. Bài blog
ngày 27/08/2026 giới thiệu ba tính năng lớn mà bảng A chưa ghi mục nào. Khi cần biết
trạng thái mới nhất, phải đọc cả hai bảng.

## Bảng A. Giao diện Flow

Nguồn: `https://flow.google.com/changelogs`, đọc ngày 06/09/2026 và **đọc lại ngày
08/09/2026**. Mức bằng chứng cao nhất cho câu hỏi "tính năng này có tồn tại không, từ bao
giờ, cho gói nào".

Kết quả đọc lại ngày 08/09/2026 `[live 08/09/2026]`: trang liệt kê đủ 40 mục liền một
mạch, không có nút tải thêm, và số nút đếm được bằng đúng số mục hiển thị. Mục trên cùng
vẫn là `Omni 360p has landed` ngày 26/08/2026. **Không có mục nào mới hơn.** Nghĩa là trang
này đã hai tuần không cập nhật, trong khi cùng khoảng đó blog chính thức và changelog của
Gemini API đã có sáu mục mới. Đó là lý do bảng B ở dưới tồn tại.

**Lưu ý kỹ thuật quan trọng.** Bản mirror tại `labs.google/fx/tools/flow/changelogs`
thiếu hai mục mới nhất. Phải dùng đúng địa chỉ `flow.google.com/changelogs`. Ngày trên
trang gốc theo định dạng tháng/ngày/năm của Mỹ, bảng dưới đây đã đổi sang ngày/tháng/năm.

Nội dung chi tiết của từng mục là ảnh hoặc video nên không trích được chữ. Bảng này giữ
nguyên tiêu đề tiếng Anh vì đó là chuỗi hiển thị thật.

### Bảng đầy đủ 40 mục

| Ngày | Mục |
|---|---|
| 26/08/2026 | Omni 360p has landed |
| 21/07/2026 | The Tools Community Gallery is Live! |
| 30/06/2026 | Community Tools Market, Nano Banana 2 Lite |
| 23/06/2026 | Maps Imagery Grounding |
| 10/06/2026 | Gemini Omni Pricing Update + Omni Frames to Video |
| 04/06/2026 | Frame to Video now available for Gemini Omni Flash |
| 19/05/2026 | Agent, Google Flow Tools, Gemini Omni Flash, and more! |
| 29/04/2026 | Archive, Shortcuts and more! |
| 21/04/2026 | Link Sharing and 4s/6s Videos |
| 16/04/2026 | Ingredients to Video with Veo Lite |
| 10/04/2026 | "Veo 3.1 Lite - Lower Priority" in Ultra |
| 02/04/2026 | Experimental Voice Ingredients for Ultra Users |
| 30/03/2026 | Veo 3.1 Lite is now available in Flow! |
| 19/03/2026 | New Image Aspect Ratios |
| 02/03/2026 | Veo 2 Deprecation |
| 26/02/2026 | Introducing Nano Banana 2 |
| 25/02/2026 | A new way to Flow |
| 03/02/2026 | Free credits now refresh daily |
| 18/12/2025 | Ingredients-to-Video: now in Portrait aspect ratio |
| 16/12/2025 | Nano Banana Pro: now with 2k and 4k upscaling! |
| 02/12/2025 | Object Removal (new) |
| 25/11/2025 | Ultra tier: return of zero credit Veo 3.1 Fast generations |
| 21/11/2025 | Extending Nano Banana Pro to all Paid tiers |
| 20/11/2025 | Introducing Nano Banana Pro! |
| 18/11/2025 | Service disruption |
| 18/11/2025 | Heavy Load! |
| 11/11/2025 | A better way to create and edit images in Flow! |
| 04/11/2025 | New experimental feature: camera adjustment |
| 29/10/2025 | Keeping Veo 2 availability longer! |
| 21/10/2025 | Doodle on your images |
| 15/10/2025 | Introducing Veo 3.1! |
| 09/10/2025 | Prompt in any language |
| 24/09/2025 | Custom Prompt Expanders |
| 10/09/2025 | Go Vertical with Portrait Orientation |
| 26/08/2025 | Ultra subscribers: Veo 3 - Fast is now 0 credits |
| 21/08/2025 | Learn Flow with Starter Projects |
| 18/08/2025 | Google AI Ultra subscribers now get double the credits! |
| 06/08/2025 | Ingredients to Video now has a fast option, and it's available in Pro and Ultra |
| 22/07/2025 | Scenebuilder now autosaves your work |
| 01/07/2025 | You can now make your images talk with Veo 3 |

## Bảng B. Model và API, những mục bảng A chưa có

Mọi mục dưới đây đọc ngày 08/09/2026. Nguồn ghi ở cột cuối. Đây là những thay đổi xảy ra
SAU mục mới nhất của bảng A, tức sau ngày 26/08/2026, cộng một mục ngày 14/08/2026 mà
bảng A không hề nhắc tới.

| Ngày | Việc | Nguồn | Mức |
|---|---|---|---|
| 14/08/2026 | Cho tắt watermark HIỂN THỊ trong Settings, mục Media Watermark, áp dụng cho Nano Banana, Omni và Lyria trong Gemini và Flow. SynthID vô hình cùng metadata C2PA vẫn giữ, không tắt được | techcrunch.com | `[chưa xác minh]` |
| 27/08/2026 | Blog Google Labs đăng "New creative controls in Google Flow" gồm Start and End Frames, xuất 1080p và 4K, và nháp ở 360p rồi nâng độ phân giải | `blog.google/innovation-and-ai/models-and-research/google-labs/new-creative-controls-google-flow/` | `[doc]` |
| 27/08/2026 | `gemini-omni-1.1-flash` ra bản chính thức đại trà, thêm nối dài video, nội suy ảnh, và chọn độ phân giải 360p, 720p, 1080p, 4K | `ai.google.dev/gemini-api/docs/changelog` | `[doc]` |
| 01/09/2026 | Agentic video understanding cho Gemini 3.7, 3.6 và 3.5 Flash-Lite. Đây là HIỂU video đầu vào chứ không phải sinh video, nên chỉ liên quan gián tiếp | `ai.google.dev/gemini-api/docs/changelog` | `[doc]` |
| 02/09/2026 | Gemini 3.8 Flash ra bản chính thức, nhắm vào lập trình, gần như không liên quan tới video | `ai.google.dev/gemini-api/docs/changelog` | `[doc]` |
| 03/09/2026 | Lyria 3.5 vào public preview, sinh trọn bài hát, giọng hát tự nhiên hơn, kiểm soát cấu trúc và thời lượng tốt hơn | `ai.google.dev/gemini-api/docs/changelog` | `[doc]` |

Hai điều bảng B nói mà bảng A không nói.

Thứ nhất, **Flow đã xuất được 1080p và 4K từ 27/08/2026**. Mọi chỗ trong skill còn nói
Flow chỉ ra 720p đều lạc hậu kể từ ngày đó. Giá kèm theo nằm ở `flow-core.md`, tóm tắt là
nâng lên 1080p miễn phí cho người trả phí, còn nâng lên 4K tốn 50 credit và chỉ gói Ultra.

Thứ hai, **quy trình tiết kiệm credit đã đổi bản chất**. Trước đây nháp ở độ phân giải
thấp rồi phải SINH LẠI ở độ phân giải cao, tức trả tiền hai lần. Nay nháp ở 360p rồi NÂNG
CẤP chính clip đó, tức phần nâng lên 1080p không mất thêm credit.

## Không tìm thấy gì cho hai cái tên này

Trang chính thức của Flow không có tài liệu nào cho tính năng tên `Starter Projects` hay
`Archive`. Hai cái tên đó chỉ tồn tại trong tiêu đề mục changelog ngày 21/08/2025 và
29/04/2026. Đây là "chưa tìm thấy tài liệu", KHÔNG phải "tính năng không tồn tại".

## Mười điều dòng thời gian này giải thích được

1. **Omni 360p chỉ mới có từ 26/08/2026**, tức khoảng hai tuần trước thời điểm đọc. Đây
   là lý do chỉ Omni mới cho chọn 360p, còn ba model Veo thì không có ô đó.
2. **Flow chính thức nhận prompt mọi ngôn ngữ từ 09/10/2025.** Viết prompt tiếng Việt là
   cách dùng hợp lệ, không phải mẹo lách.
3. **Quỹ credit miễn phí làm mới theo ngày từ 03/02/2026.** Đó là gốc của 50 credit mỗi ngày.
4. **Ảnh có thêm tỉ lệ mới từ 19/03/2026.** Đây là lý do ảnh có năm tỉ lệ trong khi video
   vẫn chỉ có 16:9 và 9:16.
5. **Hai mức thời lượng 4 giây và 6 giây có từ 21/04/2026.** Trước đó không chọn được.
6. **Chế độ 0 credit chỉ dành cho gói Ultra và đã lặp lại ba lần**, vào các ngày 26/08/2025
   với Veo 3 Fast, 25/11/2025 với Veo 3.1 Fast, và 10/04/2026 với Veo 3.1 Lite Lower
   Priority. Gói Pro chưa bao giờ được hưởng chế độ này.
7. **Veo 2 đã khai tử từ 02/03/2026.** Mọi tài liệu còn hướng dẫn dùng Veo 2 đều lạc hậu.
8. **Ba tính năng lớn nhất của Flow hiện nay cùng ra ngày 19/05/2026**, gồm Agent, Flow
   Tools và Gemini Omni Flash. Nghĩa là chúng mới khoảng bốn tháng, nên tài liệu cũ hơn
   mốc đó gần như chắc chắn thiếu cả ba.
9. **Maps Imagery Grounding có từ 23/06/2026**, cho phép lấy hình ảnh địa điểm thật từ
   Google Maps làm nền. Đây là tính năng skill chưa từng khai thác.
10. **Voice Ingredients dành cho người dùng Ultra, có từ 02/04/2026.** Cần phân biệt tính
    năng này với việc gắn giọng vào một Character, vì hai thứ không giống nhau.
    `[chưa xác minh]` chưa tự thử nên chưa biết trên gói Pro có dùng được hay không.

## Quy tắc sử dụng trang này

Trước khi khẳng định một tính năng của Flow có hay không có, hãy mở BA nguồn chứ đừng chỉ
một. Giao diện chỉ cho biết tài khoản đang dùng thấy gì. Changelog của Flow cho biết tính
năng có tồn tại không và dành cho hạng nào. Còn hai nguồn dưới đây đi nhanh hơn changelog
của Flow và là nơi tính năng mới xuất hiện trước.

| Nguồn | Địa chỉ | Mạnh ở đâu |
|---|---|---|
| Changelog của Flow | `https://flow.google.com/changelogs` | Tính năng giao diện, kèm ngày và hạng tài khoản |
| Bảng năng lực chính thức | `https://support.google.com/flow/answer/16352836` | Model nào làm được chế độ nào, thời lượng nào |
| Changelog của Gemini API | `https://ai.google.dev/gemini-api/docs/changelog` | Model mới và thay đổi API, đi trước changelog của Flow |

Bài học cụ thể của đợt cập nhật ngày 08/09/2026. Skill từng dừng ở mục changelog ngày
26/08/2026 và tưởng đó là mới nhất. Thực ra ngay hôm sau, ngày 27/08/2026, blog chính thức
đã công bố ba tính năng lớn và Gemini Omni Flash 1.1 đã ra bản đại trà. Chỉ đọc changelog
của Flow thì bỏ lỡ toàn bộ.

Ví dụ thực tế. Mục `Veo 3.1 Lite - Lower Priority` không xuất hiện trên tài khoản gói AI
Pro, nhưng changelog ngày 10/04/2026 ghi rõ nó tồn tại và dành riêng cho gói Ultra. Nếu
chỉ nhìn giao diện thì sẽ kết luận sai rằng tính năng đó không tồn tại.
