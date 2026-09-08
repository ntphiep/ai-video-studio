# Google Flow — Tài liệu tham chiếu tổng hợp

Phạm vi: chỉ nói về chính Google Flow (labs.google/fx/tools/flow, còn gọi flow.google.com). Không bao gồm NotebookLM, Canva, AI Studio, Remotion, OpenMusic, Stitch, Pomelli, VMEG dù các công cụ này xuất hiện trong cùng video hướng dẫn.

## Chú giải nguồn

- `[live]` = tự mở giao diện Flow và đọc DOM, tự đo bằng `ffprobe`, tự gọi API, hoặc tự đọc HTML thô của trang tài liệu chính thức, thực hiện ngày 06/09/2026. Đây là mức bằng chứng cao nhất vì không qua trung gian nào. Đúng năm nguồn được mang nhãn này: doc Veo đọc bằng HTML thô, bảng giá đo trực tiếp trên tài khoản, số đo Video Resizer bằng `ffprobe`, danh mục tool đọc từ DOM, và kết quả gọi `GET /v1beta/models`.
- `[changelog]` = đọc trực tiếp `https://flow.google.com/changelogs`. Mức cao, là tài liệu chính thức của Google, nhưng khác `[live]` vì đó là điều Google công bố chứ không phải điều tự đo được.
- `[frame]` hoặc `[bXX t=Ys]` = xem từng khung hình của một video hướng dẫn trên YouTube, kèm mốc giây gốc. Mức trung bình. Đây là quan sát giao diện thật trên màn hình người quay, nhưng khác thời điểm và khác tài khoản với `[live]`, nên có thể lệch do giao diện đổi theo thời gian. Nếu thứ nhìn thấy là **slide do tác giả video tự soạn** chứ không phải giao diện Flow, phải ghi rõ điều đó.
- `[bên thứ ba]` = blog, bài đánh giá, hoặc thảo luận cộng đồng. Mức thấp nhất. Luôn ghi tên nguồn và ngày.
- Khi hai nguồn mâu thuẫn, tài liệu này luôn ưu tiên `[live]`, ghi rõ lý do, và vẫn giữ lại số liệu của nguồn kia để không mất thông tin.
- `[chưa xác minh]` = chỉ một nguồn duy nhất nói, chưa ai kiểm chứng lại độc lập.
- Khi hai nguồn mâu thuẫn, tài liệu này LUÔN ưu tiên `[live]` và ghi rõ lý do bên cạnh, đồng thời vẫn giữ lại số liệu từ `[bXX]` để không mất thông tin.
- `[chưa xác minh]` = chỉ một nguồn duy nhất nói, chưa ai kiểm chứng lại độc lập.

Bảng tra video nguồn (mã batch — ID YouTube — tên video):

| Mã | ID video | Tên video |
|---|---|---|
| b01, b02 | 3LNvnkVez44 | Google Flow 2026: How to 100% Lock Character, Voice & Avatar Consistency |
| b03, b04 | 3o8SlHavQmQ | Claude Automatically Creates Bulk UGC Videos When Connected to This Tool! (chỉ đoạn có Google Flow được dùng) |
| b05 | 6PktkVSgLL8 | video lẻ không tiêu đề, không có phụ đề đối chiếu |
| b06 | Hf-rqDme1PQ | Create AI Videos from Storyboards in 1 Minute with Gemini & Google Flow! |
| b12 | ZCrEU1A64Z0 | AI Speaking Natural Vietnamese? How to Maintain Voice & Emotion for Each Character |
| b14 | jk25EmJm0iU | EVERY Google AI Tool Compiled in 1 Video (chỉ đoạn Google Flow) |
| b16, b17 | mCnR9j-Qk9Y | Fully Automated: Claude Writes Scripts, Creates Characters, Storyboards, and Videos on Google Flow |
| b20, b21, b22 | xfLoVaQxvv8 | Google Flow A-Z: Tất Cả Tính Năng Bạn Cần Biết Để Tạo Video AI (9 Chương) — nguồn chính, chuyên sâu nhất về riêng Flow |
| b23, b24 | z6ToeG58hPU | New Gemini Omni Update: BIG OPPORTUNITY in 2026 (chỉ đoạn Google Flow) |
| b35 | SujPpuMb6XI | How to Build Your Own AI Image Generator App for Beginners (chủ yếu về Tools/Create Tool trong Flow) |

Các batch còn lại trong `vision/` (b07 đến b49, trừ các mã kể trên) hoặc không có cảnh Google Flow nào, hoặc chỉ nhắc tên "Flow" một lần không kèm thao tác cụ thể (đã kiểm bằng grep từ khóa "flow/labs.google/Veo/Nano Banana/Omni Flash/Scenebuilder" trên cả 49 file rồi đọc lại từng đoạn khớp) — không được dùng làm nguồn cho tài liệu này.

---

## 1. Bản đồ giao diện

### 1.1 Trang chủ và điều hướng chung

Trang chủ có hai địa chỉ. Địa chỉ hiện hành nên dùng là **`flow.google.com`**. Địa chỉ cũ
`labs.google/fx/tools/flow` vẫn chạy nhưng bản mirror changelog ở đó thiếu mục mới, nên
đừng lấy làm nguồn.

Đo lại header ngày 08/09/2026 trên `flow.google.com` `[live 08/09/2026]`: có link
**`Flow Music`** trỏ sang `flowmusic.app`, link **`Flow TV`** trỏ RA NGOÀI tới
`labs.google/flow/tv` chứ không phải một panel bên trong ứng dụng, nút `Account details`
hiện huy hiệu `PRO tier`, và nút `More options` mở menu gồm: About Flow, Learn Flow, Send
app feedback, Report legal issue, Privacy notice, công tắc `Help improve Flow`, và
`Delete all projects`. Mục cuối cùng đó xoá TOÀN BỘ project, hãy cẩn thận khi thao tác
bằng script tự động.

Thanh trên cùng theo quan sát cũ qua video: logo "Google Flow" bên trái; bên phải có nút "Google Flow TV", icon Discord, Instagram, X (Twitter), dấu hỏi (Help), menu ba chấm, nhãn gói đang dùng (PRO hoặc ULTRA), avatar tài khoản [b01 t=146s; b06 t=53.7s; b12 t=0s; b16 t=3s; b20 t=123s; b23 t=42.7s].

Banner lớn xoay vòng (carousel) trên trang chủ, ba mẫu quan sát được: "A creative partner at every step." (nút "Try the Google Flow Agent"), "Your face, your voice, your story." (nút "Get started", giới thiệu tính năng Avatar thử nghiệm), "Introducing Gemini Omni Flash" (nút "Try Omni now", mô tả "Cinematic realism, powerful editing, world knowledge: try our latest video generation model!") [b01 t=146s; b06 t=53.7s; b20 t=123-133s]. Dưới banner là lưới các thẻ project đã lưu và nút "+ New project" [b20 t=142-154s].

Banner khuyến mãi phụ từng thấy: "Your Google AI plan now comes with 50 additional Flow credits daily." và banner cảnh báo tải cao: "Flow is currently experiencing high demand, affecting video generation. Requests may need to be retried at a later time. AI Credits will be refunded for any failed requests." [live, danh mục tool đọc từ DOM ngày 06/09/2026].

### 1.2 Bên trong một project

Sidebar trái theo thứ tự thấy đầy đủ nhất: **All Media, Images, Videos, Characters, Scenes, Favorites, Uploads, Tools, Trash, Collapse** [b01 t=64s; b06 t=100.7s; b20 t=169s]. Lưu ý quan trọng: mục **Images** và **Videos** KHÔNG xuất hiện ngay từ đầu — chúng chỉ hiện ra trong sidebar sau khi người dùng tạo ra ảnh/video đầu tiên trong project đó [b01 t=29s, t=351.6s; b05 t=144-158s]. Mục **Uploads** cũng chỉ xuất hiện sau khi có ít nhất một lần tải file lên [b05 t=202s]. Một số phiên bản giao diện hiển thị sidebar dạng icon dọc không có nhãn chữ, thứ tự icon: lưới (all), ảnh, phim, hình người (Characters), lịch, dấu cộng lưới (được suy luận là Ingredients) [b16 t=33s, t=68s] — đây có thể là chế độ thu gọn (collapsed) của cùng một sidebar, chưa xác minh chắc chắn liệu có phải phiên bản giao diện khác hay chỉ là trạng thái thu gọn.

Khi project trống: chữ mờ giữa canvas "Start creating or drop media" [b01 t=154.2s; b16 t=17s; b23 t=132s].

Khung nhập prompt chính (composer) ở cuối màn hình luôn có: placeholder "What do you want to create?"; nút "+" (thêm ảnh/asset) và nút "Agent" ở bên trái; bên phải hiện chip tóm tắt cấu hình hiện tại (ví dụ "Nano Banana Pro · x4" hoặc "Video · 10s · x1"); nút gửi hình mũi tên (→) ngoài cùng [b01, b05, b16, b20 — nhiều mốc].

Bấm vào chip cấu hình sẽ mở popup cài đặt gồm: 2 tab lớn **Image / Video**; khi ở Video còn có thêm 2 tab **Frames / Ingredients**; hàng nút tỉ lệ khung hình; hàng nút số lượng sinh (x1/x2/x3/x4); dropdown chọn model; dòng chữ nhỏ "Generating will use N credits" hiện NGAY TRƯỚC khi bấm gửi [b05 t=150s; b16 t=42s; b20 t=169s; b23].

Bấm nút "+" mở **Asset Picker**: các tab lọc **All | Images | Videos | Voices | Characters | Avatar | Uploads**, ô "Search assets", dropdown lọc theo tháng và sắp xếp "Recent", nút "Upload media" ở góc dưới trái, nút chính màu trắng đổi tên tùy ngữ cảnh ("Add to Prompt" ở composer thường, "Add to Character" khi đang ở trang nhân vật, "Add to instruction" khi đang ở Agent Instructions) [b01 t=125.9s; b06 t=97.6s; b16, b17, b20, b21, b22, b23; live/số đo Video Resizer ngày 06/09/2026 xác nhận lại đúng bố cục này trong Video Resizer].

### 1.3 Characters — đường dẫn thao tác

Sidebar > Characters > "New Character" (dấu +) hoặc "Create my avatar" (icon người) [b21 t=701s]. Trang "New character" ghi tiêu đề "Build and reuse characters for consistent videos. Use a sample prompt below, or create from scratch." kèm các thẻ mẫu tính cách dựng sẵn. Số lượng thẻ mẫu quan sát được KHÔNG nhất quán giữa các video: 4 thẻ (**The Familiar, The Eccentric, The Wicked, The Fantastical**) ở một số video [b01 t=110.9s; b16 t=79s; b23 t=260s], còn 6 thẻ (thêm **The Professional, The Wildcard**) ở các video khác [b06 t=92.2s; b12 t=213s; b21 t=705s]. Chưa xác minh được đây là khác biệt theo thời điểm cập nhật giao diện hay theo tài khoản/gói dùng — ghi nhận cả hai, không gộp thành một con số.

Ô nhập "Describe your character..." + dropdown model (thường là **Nano Banana 2**, đôi khi **Nano Banana Pro**) + nút "Upload" + nút "Add from Project" để lấy ảnh có sẵn trong project làm tham chiếu [b01 t=110.9s; b06 t=92.2s; b21 t=705s].

Nút **"Format"**: gõ mô tả ngắn bằng tiếng Việt rồi bấm Format để Flow tự viết lại thành một prompt tiếng Anh chi tiết, chuyên nghiệp (kèm thông số máy ảnh, ánh sáng studio...) [b12 t=236-240s, ví dụ nguyên văn ở Mục 5].

Sau khi có ảnh đầu tiên, vào trang chi tiết Character (`/character/<id>`): tiêu đề mặc định "Untitled Character" (đổi tên được), nút "Select a voice", khung "Character Info (optional)" placeholder "Describe how your character acts...", kèm dòng chú thích "The Flow agent can use this information to help craft scenes with your character.", hai nút chuyển đổi "Portrait" / "Create Body", khung ảnh lớn, khung nhập "What do you want to change?" [b01 t=439.6s; b06 t=92.5s; b12 t=219s; b23 t=275-315s].

"Create Body": sinh ảnh toàn thân 3 góc (triptych) từ chân dung có sẵn. Prompt mẫu do chính Flow gợi ý sẵn trong ô nhập: *"Full-body triptych, three distinct views: front facing, 3/4 side view, and back view. High resolution, flat studio lighting, consistent anatomical proportions across all views, solid white background. [DESCRIBE BODY AND OUTFIT]"* [b21 t=790s].

### 1.4 Voices — đường dẫn thao tác

Từ trang chi tiết Character, bấm "Select a voice" mở panel **Voices**: danh sách giọng có sẵn dạng thẻ (tên + mô tả ngắn giới tính/tính chất/cao độ), nút **"+ Create New Voice"** ở đầu danh sách, nút "Add to Character" ở cuối [b12 t=117.6s; b21 t=798s; b23 t=311-315s].

Dialog **"Edit Voice"** (khi tạo mới hoặc chỉnh sửa): trường **Base Voice** (dropdown chọn giọng gốc làm nền), **Name**, **Voice Performance** (ô mô tả tự do, chấp nhận tiếng Việt, dùng để định hướng chất giọng/độ tuổi/vùng miền), **Sample Dialogue** (giới hạn hiển thị **0/120 characters**, dùng để nghe thử qua nút Preview), nút Cancel / Save New Voice / Reset [b01 t=465-498.8s; b06 t=41.5s; b12 t=117.6-147.6s; b17 t=637s; b23 t=340-373s].

Xem chi tiết đầy đủ về danh sách giọng, giới hạn, và hạn chế ngôn ngữ ở Mục 5.

### 1.5 Tools — bản đồ đầy đủ

Trang vào: `flow.google.com/project/<id>/tools`, tiêu đề trang "Explore tools". Số tab đo được `[live]` ngày 06/09/2026 là **đúng BA TAB: My Tools, Community, Templates** [live, danh mục tool đọc từ DOM ngày 06/09/2026 — tài liệu cũ ghi 4 tab là sai]. Một số video hướng dẫn cũ hơn chỉ thấy **hai tab "Discover" / "My Tools"** [b06 t=54.1s; b20 t=169s; b21 t=1213s; b35 t=22s] — khả năng cao đây là giao diện TRƯỚC ngày 21/07/2026, vì changelog chính thức ghi "The Tools Community Gallery is Live!" đúng ngày đó [live, changelog.md]; tức tab Community là tính năng MỚI được thêm, và "Discover" nhiều khả năng chính là tiền thân của "Templates" (tên gọi khác thời điểm khác nhau). Đây là suy luận có căn cứ từ changelog, không phải bằng chứng trực tiếp về việc đổi tên.

Banner đầu trang (mọi thời điểm): *"Build all the tools you can imagine. An idea and a description are all it takes to make whatever tool you need."* kèm nút "Create Tool" [b01, b06, b21, b35].

Danh mục tool đầy đủ (34 tool tab Templates, 28 tool tab Community) nằm ở `flow-tools.md` mục 1, không lặp lại ở đây.

**Tab My Tools**: chứa hai loại thẻ — tool cộng đồng đã "Remix" (bấm "Remix tool" trên bất kỳ tool nào để sao chép về của mình rồi tùy biến) và tool tự tạo bằng "Create Tool". Có phần con **"My creations"** chỉ liệt kê tool do chính người dùng dựng, ví dụ quan sát được: Nature Documentary Maker, (Gia dụng) Tạo video..., Story Animator, (Gia dụng) Tải ảnh sản phẩm..., Fashion Motion Lab [b21]; ở một tài khoản khác: Style Portrait, Claymation Studio [b02, b35].

### 1.6 Đường dẫn thao tác chi tiết từng tool đã có bằng chứng thao tác thật

**Storyboard Studio**: Tools > (Discover/Templates) > "Storyboard Studio". Modal chào "Welcome to Story Studio" có dropdown chọn style (mặc định "Realistic", đổi được sang "Claymation"...), liệt kê 3 bước "1. Workshop your script", "2. Create your cast and locations", "3. Visualize your storyboard", nút "Get Started" [b06 t=61.5s]. Bên trong có đúng 3 tab **"1. Script"**, **"2. Assets"**, **"3. Storyboard"**, mỗi tab có dropdown style riêng.
- Tab Script: khung chat "Ask Gemini" để định vai trò đạo diễn, Gemini trả về bảng kịch bản với cột Cảnh/Thời lượng/Hình ảnh/Âm thanh/Voiceover; ràng buộc cứng lời bình mỗi cảnh 25-35 từ để khớp 10 giây/cảnh [b06 t=7.2s, t=26.7s].
- Tab Assets: nút "Autofill Characters" mở 3 lựa chọn **Add Character | Autofill descriptions | Autocreate images** [b06 t=71-73s]. Upload nhiều ảnh tham khảo cùng lúc (ví dụ 10 file, 7.3 MB) [b06 t=75.4s].
- Tab Storyboard: mỗi Scene có "Scene 01", tên cảnh, số khung ("6 frames"), nút "Autofill Scene", ảnh được đặt tên riêng từng khung, tiến trình "Generating images X/10" kèm nút "Stop" [b06 t=79.9-88s].
Cạm bẫy quan sát trực tiếp: phải yêu cầu lặp lại "tạo ảnh storyboard số X nốt nhé" cho từng cảnh — công cụ không tự sinh hết tất cả cảnh cùng lúc dù đã có kịch bản đầy đủ [b06 mục 7]. Khi điều khiển bằng agent ngoài (Claude in Chrome), phải ép rõ chế độ "Image" nếu muốn ra MỘT ảnh storyboard dạng lưới — nếu không, Flow/agent có thể tự tách thành nhiều clip video riêng theo từng panel [b16 t=463-501s].

**Image Editor**: panel trái **"Layers (0)"** với "+ Add Image" và "Add text layer"; panel phải **"Canvas dimensions"** (Preset "Default", **Width 1344px, Height 768px** mặc định, nút "Reset defaults") và **"AI settings"** (Image Model mặc định **Nano Banana 2**; Background Removal: **"MODNet (People, Fast)"**); thanh công cụ dưới ảnh: **Refine, Inpaint, Outpaint, Cutout, Crop**; nút **"Save to gallery"** [b01 t=635-654s; xác nhận lại kích thước mặc định ở b35 t=326s]. Chèn ảnh có sẵn qua hộp thoại "Media Grid" (lọc theo tháng, "Search assets", "Recent", tab Images/Uploads, "Upload media"). Text layer chọn font trong Google Sans, Inter, Bebas Neue, Montserrat, Playfair Display, Cinzel (danh sách còn cuộn thêm); có tính năng "depth": toggle Enable depth, thanh trượt "Depth offset", toggle "Flatten layer depth", nút "Save depth composite". Mỗi layer ảnh có thanh trượt Opacity/Brightness/Contrast/Saturation/Blur. Quy trình thật: thêm 2 layer ảnh, dùng Refine để hòa trộn thành một ảnh, rồi Inpaint để chèn chữ tiêu đề đè lên [b35 t=396-453s].

**Mockup**: URL dạng `labs.google/fx/tools/flow/project/<id>/tool/<id>`. Header có nút "Remix tool", icon tim/ghim/chia sẻ/cờ, nút "Done". Panel trái "Canvas media" + nút "Import Image". **12 loại mockup dựng sẵn**: laptop, phone, tv, shirt, hat, bag, pin, book, poster, window, billboard, mural, cộng thêm **"+ custom mockup"** để nhập mô tả tự do [live, danh mục tool đọc từ DOM ngày 06/09/2026; b24 t=699.7s; b35 t=235s]. Toggle **Fast/Pro** và nút "RESET SESSION". "Import Image" mở hộp thoại **Media Grid** giống các tool khác. Chọn "custom mockup" mở ô nhập text placeholder "Describe your mockup..." — **chấp nhận tiếng Việt trực tiếp**, ví dụ đã dùng thật: "hiển thị trang web của tôi bên trong chiếc máy tính xách tay nó được đặt trên một chiếc bàn làm việc hiện đại..." ra kết quả đúng yêu cầu [b24 t=719.4-746.2s].

**Converge**: tiêu đề "CONVERGE". Panel trái "HISTORY STACK" + nút "CLEAR ALL". Công cụ vẽ: Sketch, Annotate, Fill, Dropper. Panel phải "AI SETTINGS" (model mặc định **Nano Banana Pro**), "GUIDING PROMPT", "RENDER OUTPUT SETTINGS" (Style, Aspect Ratio "Auto (Match Input)"), toggle "CONTEXTUAL BACKGROUND" (mặc định tắt), nút "GENERATE RENDER" [b35 t=629s]. Quy trình BẮT BUỘC 2 bước: (1) vẽ phác thảo rồi bấm "Generate Vector Layer" để ra vector sạch, chọn 1 trong các biến thể; (2) chỉ sau đó mới bấm "Generate Render" để ra ảnh render 3D. Bỏ qua bước vector sẽ không render được [b35 t=629-664s].

**Shot Explorer**: panel trái "SELECT IMAGE". Ba nhóm nút: "Perspective" (overhead/side/back), "Pan" (left/right/up/down), "Zoom" (zoom in/zoom out/extreme detail/surprise me), nút RESET, toggle Fast/Pro [b35 t=601s]. Mỗi lần bấm một nút sẽ tạo biến thể góc máy mới, không cần viết prompt.

**Simple Sketch**: khung vẽ tay ("DRAW HERE") + công cụ vẽ (chọn, bút chì, hình vuông, hình tròn, chữ T, bảng màu, 2 cỡ nét, undo/redo, upload ảnh, xóa) + ô nhập prompt bên dưới; kết quả hiện bên phải kèm nhãn "FAST" [b01 t=603-618s; b35 t=139-220s]. Có thể vẽ và viết prompt tiếng Việt cùng lúc; tinh chỉnh thêm bằng cách khoanh vùng đỏ trên ảnh kết quả rồi nhập mô tả bổ sung.

**Video Resizer** (đo `[live]` bằng ffprobe, xem chi tiết đầy đủ ở Mục 8).

Các tool có tên trong catalog nhưng CHƯA có video nào ghi lại thao tác chi tiết bên trong (chỉ có mô tả một dòng): Scene Explorer, Mask Magic, Grid Architect, Whisk, Style Writer, Type Overlays (Type Overlays chỉ xác nhận được KHÔNG tốn credit qua đo `[live]`, không có ảnh giao diện chi tiết) [chưa xác minh].

### 1.7 Create Tool — tự tạo công cụ bằng ngôn ngữ tự nhiên

Vào từ Tools > Explore Tools > nút "Create Tool", hoặc My Tools > "Create New". Trang khởi tạo luôn ghi: *"Start building any creative tool you can dream by describing it below."* kèm 3 gợi ý mẫu đổi theo phiên bản (đã thấy "Image Filter, Time Stretcher, Voice Over" [b01] và "Style Morph, Image Filter, Voice Over" [b35]) [b01 t=749-770.6s; b35 t=664s].

Người dùng mô tả tool mong muốn bằng tiếng Việt tự nhiên. Flow tự sinh một công cụ hoàn chỉnh với: model mặc định (thường Nano Banana Pro), tỉ lệ khung hình mặc định (ví dụ 1:1), một prompt phong cách mặc định do AI tự viết. Giao diện tool vừa tạo: 2 tab "Tool"/"Edit"; bên trong Tool có 2 tab con "Preview"/"Code"; panel phải cố định tên **"Tool Builder"** — khung chat để tiếp tục chỉnh sửa tool bằng lời [b01 t=772-811.6s; b02 t=826.6s].

Năm ví dụ thật đã quan sát:
1. **Claymation Studio** — biến ảnh bất kỳ sang phong cách claymation. Prompt gốc: *"...xây dựng một công cụ cho phép tôi tải lên bất kỳ hình ảnh nào, và công cụ đó sẽ tự động chuyển nó sang phong cách hoạt hình đất sét"*. AI tự chọn Nano Banana Pro làm mặc định "vì khả năng hiểu phong cách nghệ thuật rất tốt", gợi ý Imagen 4 nếu cần chi tiết cao hơn, tỉ lệ 1:1, tự viết prompt phong cách mặc định [b01 t=772.7s; b02 t=826.6-852.9s].
2. **Story Animator** — kịch bản tóm tắt biến thành phim hoạt hình nhiều cảnh. Giao diện 3 cột: "1. KỊCH BẢN & LỜI BÌNH", "2. THIẾT LẬP NHÂN VẬT" (dropdown Phong cách: Điện ảnh/Tả thực/Anime/Hoạt hình 3D/Tranh sơn dầu/Màu nước; chọn khung Ngang/Dọc; tối đa 2 ảnh nhân vật), nút "Phân tích & Tạo Phim". Công cụ TỰ CHIA kịch bản thành tối đa 6 cảnh, mỗi cảnh có mô tả hình ảnh chi tiết do AI viết, rồi bấm "Bắt đầu quay" từng cảnh để tạo video 8 giây/cảnh, tiến độ "x/6 cảnh hoàn tất" [b21 t=1026-1078s].
3. **Style Portrait** — trả về 3 phong cách chân dung từ 1 ảnh (Pixar Style, Biếm họa, Sách tô màu), nút "Bắt đầu chuyển đổi", nút "Tải về tất cả". Code sinh ra dùng React/TSX với thư viện nội bộ "flow-sdk" [b35 t=664-759s].
4. **Outfit & Env Switcher** (đổi tên nhiều lần: Outfit Change → Outfit Persona → Outfit & Env Switcher) — 3 cột OPTION 1/2/3 mỗi cột có Outfit/Environment/nút RANDOM/nút "TAO BIEN THE", nút "BATCH GENERATE ALL", thanh trượt "Độ tương đồng khuôn mặt" (90%), Aspect Ratio 4 nút (9:16/3:4/1:1/16:9), mỗi ảnh có nút DOWNLOAD và xóa riêng [b35 t=986-1034s].
5. **Fashion Motion Lab** — tải ảnh người mẫu + trang phục vào 2 ô riêng, tool tự tạo bộ ảnh 8 góc/tư thế của người mẫu mặc đúng trang phục đó [b21 t=1250s].

Nguyên tắc chung: mô tả ban đầu càng cụ thể (số lượng đầu ra, tên style, ràng buộc giữ nhận dạng) thì tool tạo ra càng sát ý; chỉnh sửa nên đi qua nhiều lượt chat nhỏ (đổi tên, thêm nút, đổi bố cục) thay vì một prompt lớn; mọi tool tự tạo đều mang cảnh báo cố định cuối trang về khả năng tốn credit.

### 1.8 Cảnh báo chuẩn trên mọi tool

Chân trang khi mở bất kỳ tool nào (kể cả tool của Google) luôn ghi nguyên văn: *"Google Flow can make mistakes, so double check it. This Tool may consume credits."* — với tool cộng đồng (remix) còn thêm: *"This app was created by another person and may be inaccurate or unsafe. Report unsafe content."* [live, tự đọc chân trang trên DOM ngày 06/09/2026; xác nhận lại ở b21 và b35 t=326s]. Điều này bác bỏ khẳng định cũ "tool không tốn credit" — phát biểu đúng là Flow chỉ CẢNH BÁO tool có thể tốn credit, không cam kết miễn phí tuyệt đối. Đã đo được cụ thể: **Video Resizer** và **Type Overlays** xử lý phía client, KHÔNG trừ credit qua nhiều lần đo `[live]`; mọi tool khác gọi lại model sinh ảnh/video nền (Nano Banana, Imagen 4, Omni Flash...) nên phải giả định CÓ khả năng tốn credit cho tới khi tự đo được con số cụ thể.

---

## 2. Model và chi phí

### 2.1 Danh sách model — gộp một bảng

| Model | Dùng cho | Ghi chú |
|---|---|---|
| Nano Banana 2 | Ảnh (character mặc định, chỉnh sửa ảnh, Image Editor) | id kỹ thuật quan sát ở AI Studio: `gemini-3.1-flash-image-preview` [ngoài phạm vi Flow, chỉ tham khảo] |
| Nano Banana Pro | Ảnh (đặc biệt khi ghép nhiều ảnh tham chiếu/character phức tạp, Converge, Claymation Studio) | |
| Imagen 4 | Ảnh (lựa chọn thứ 3 trong một số dropdown, ít được dùng làm mặc định) | b14 t=399s |
| Gemini Omni Flash / Omni 1.1 Flash | Video, model DUY NHẤT cho phép chọn độ phân giải VÀ thời lượng | Tên hiển thị khác nhau tùy chỗ: banner ghi "Gemini Omni Flash", composer chip ghi ngắn "Omni Flash", panel cài đặt model ghi "Omni 1.1 Flash" [live, bảng giá đo trực tiếp trên tài khoản ngày 06/09/2026] |
| Veo 3.1 - Lite | Video, giá rẻ nhất trong nhóm Veo, tốc độ ngang Fast, dùng để thử nhiều ý tưởng | |
| Veo 3.1 - Fast | Video, cân bằng giá/tốc độ, dùng sản xuất hàng ngày | |
| Veo 3.1 - Quality | Video, đắt nhất, chậm nhất, chất lượng cao nhất, dùng cho bản final | |
| Veo 3.1 - Lite [Lower Priority] | Video, CHỈ dành cho gói Ultra, đổi lấy hàng đợi lâu hơn để giảm/miễn phí credit | Xem 2.3 |

Model video nền tảng thực sự (API, không phải tên hiển thị UI) `[live, doc Veo đọc bằng HTML thô ngày 06/09/2026]`: `veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`, `veo-3.1-lite-generate-preview`; `veo-3.0-generate-001` ghi rõ "Deprecated" trên trang tài liệu — mọi tài liệu còn nhắc Veo 2/Veo 3.0 là đã lạc hậu (Veo 2 chính thức khai tử từ 02/03/2026 theo changelog).

Trang tổng quan model chính thức (`deepmind.google/models/`) ghi rõ nơi dùng được từng model: Gemini Omni dùng được trong Gemini app và **Google Flow**; Veo dùng được trong Gemini app, **Google Flow**, và Google AI Studio; Nano Banana dùng được trong Gemini app, Google AI Studio, Gemini Enterprise (trang tổng quan này KHÔNG liệt kê Flow cho Nano Banana dù thực tế Nano Banana vẫn dùng được trong Flow qua UI — có thể trang chỉ liệt các kênh chính, không đầy đủ) [b23 t=38-40s].

### 2.2 Bảng credit theo model — đối chiếu 3 nguồn

Bảng chính thức từ trang hỗ trợ Google (`support.google.com/flow/answer/16526234`, tài liệu chính thức của Google, đọc ngày 06/09/2026; mức cao nhưng không phải `[live]` vì không tự đo):

| Model | Credit gói thường | Credit gói Ultra |
|---|---|---|
| Veo 3.1 Lite (4s/6s/8s) | 10 | 5 |
| Veo 3.1 Fast | 20 | 10 |
| Veo 3.1 Quality | 100 | 100 (như nhau mọi hạng) |
| Gemini Omni Flash 720p (4-10s) | 7 đến 15 tùy thời lượng | như thường |
| Omni 360p | bằng khoảng nửa giá 720p | như thường, Pro/Ultra được upscale 360→720 miễn phí |
| Gemini Omni Flash, sửa video | 40 | 40 |
| Upscale 1080p | miễn phí cho người có gói trả phí | miễn phí |
| Upscale 4K | không có | 50 credit, CHỈ Ultra mới dùng được |

Đọc lại trang trên ngày 08/09/2026, số liệu không đổi so với lần đọc ngày 06/09/2026, và
lần này lấy thêm được dòng **sửa video 40 credit** vốn bị bỏ sót lần trước
`[doc, support.google.com/flow/answer/16526234, 08/09/2026]`. Dòng "Veo 3.1 Quality" trên
trang chính thức ghi rõ phạm vi là "8s videos, Extend", tức bản Quality chỉ có 8 giây.

Một hệ quả về giá đáng nhớ: **sửa một video tốn 40 credit, còn sinh mới một clip 10 giây ở
720p chỉ tốn 15**. Sửa chỉ đáng tiền khi cần giữ lại phần lớn khung hình cũ.

Bảng đo trực tiếp trên tài khoản **AI Pro** ngày 06/09/2026, đọc nhãn "Generating will use N credits" TRƯỚC khi sinh, không tốn credit nào để lấy số này `[live, bảng giá đo trực tiếp trên tài khoản ngày 06/09/2026]` — mức bằng chứng CAO NHẤT cho phần này:

| Omni 1.1 Flash | 4s | 6s | 8s | 10s |
|---|---|---|---|---|
| 360p | 4 | 5 | 6 | 7 |
| 720p | 7 | 10 | 12 | 15 |

| Model Veo (Pro, không chọn được resolution/duration riêng) | Credit mỗi lần sinh |
|---|---|
| Veo 3.1 - Lite | 10 |
| Veo 3.1 - Fast | 20 |
| Veo 3.1 - Quality | 100 |

Số liệu này khớp CHÍNH XÁC với bảng hỗ trợ chính thức ở trên (hai nguồn độc lập trùng khớp). Ghi chú quan trọng: 360p KHÔNG đúng bằng nửa giá 720p như tài liệu hỗ trợ diễn đạt "khoảng một nửa" — số đo thực tế là 4 và 7, 5 và 10, 6 và 12, 7 và 15 (ba cặp sau đúng nửa, cặp 4 giây thì 7 chia 2 ra 3,5 nhưng Flow tính tròn thành 4). Trên tài khoản Pro, dropdown model video CHỈ CÓ ĐÚNG 4 MỤC: Omni 1.1 Flash, Veo 3.1 Lite, Veo 3.1 Fast, Veo 3.1 Quality — KHÔNG có mục "Lite [Lower Priority]" (xem lý do ở 2.3).

Số liệu đo được qua các video hướng dẫn (`[bXX]`, khác tài khoản/thời điểm với `[live]`), CHO CÙNG MỘT CẤU HÌNH DANH NGHĨA "Omni Flash, 10 giây, x1" lại cho ba con số credit khác nhau:
- 15 credit (16:9) [b20 t=336s]
- 30 credit (16:9) [b23 t=564-573s]
- 13 credit (chế độ Agent) [b16 t=99s]

Chỉ có con số **15 credit** khớp với bảng đo `[live]` (Omni 720p 10s = 15). Hai con số còn lại (30 và 13) KHÔNG khớp bất kỳ ô nào trong bảng chính thức lẫn bảng đo trực tiếp — có thể do độ phân giải thực tế khi quay không hiện rõ trên frame (ví dụ 30 credit gần bằng gấp đôi 15, có thể do một biến thể độ phân giải hoặc số lượng x khác không được ghi chú lại đầy đủ trên màn hình), hoặc do giá đã thay đổi giữa các thời điểm quay các video khác nhau (đây là các video độc lập, không rõ ngày quay chính xác). **[chưa xác minh nguyên nhân chênh lệch]** — ghi nhận cả ba số, tin tưởng nhất vào 15 vì trùng khớp với đo trực tiếp `[live]`.

Cấu hình khác đo được qua vision (không mâu thuẫn, cùng nguồn b20): Veo 3.1 Quality 8s = 100 credit; Veo 3.1 Lite [Lower Priority] 8s = 0 credit; Omni Flash 8s = 10 credit [b20 t=333-347s]. Cấu hình 8s×4 biến thể (16:9, Omni Flash) đo được 100 credit [b23 t=549.7s] — số này gần bằng 4 lần con số đơn lẻ ước tính (12-15 mỗi clip 8s×4 ≈ 48-60), cho thấy có thể chi phí không đơn thuần nhân tuyến tính theo số lượng biến thể, hoặc độ phân giải khi đo lần này khác — **[chưa xác minh cơ chế tính chính xác khi chọn nhiều biến thể cùng lúc]**.

Ảnh (Image mode): mọi lần quan sát trên vision đều thấy dòng "Generating will use **0 credits**" trước khi sinh ảnh, bất kể model Nano Banana Pro/2 và số lượng x1-x4 [b01 t=209.6s; b05 t=150s]. Đây là mẫu hình lặp lại nhất quán qua nhiều video khác nhau nhưng CHƯA có phép đo nào từ `[live]` xác nhận độc lập cho ảnh (live chỉ đo credit của video) — tạm coi ảnh cơ bản là miễn phí trên tài khoản trả phí, nhưng gắn `[chưa xác minh đầy đủ]` cho trường hợp độ phân giải cao hoặc thao tác upscale ảnh.

### 2.3 "Veo 3.1 Lite [Lower Priority]" — mục đã gây nhầm lẫn, nay đã giải quyết

Vision (`b20`, badge tài khoản không rõ ràng nhưng có khả năng ULTRA) cho thấy dropdown đủ 5 mục kể cả "Veo 3.1 - Lite [Lower Priority]" ghi "0 credit". Live đo trên tài khoản **Pro** ngày 06/09/2026 chỉ thấy 4 mục, không có mục này. Đây KHÔNG phải mâu thuẫn — nguồn quyết định là changelog chính thức tại `flow.google.com/changelogs`, mục ngày **10/04/2026** ghi nguyên văn: *"'Veo 3.1 Lite - Lower Priority' in Ultra"* [changelog]. Tức tính năng này CÓ THẬT nhưng CHỈ dành cho gói Ultra; tài khoản Pro theo thiết kế không bao giờ được cấp, nên việc chỉ thấy 4 model trên Pro không phải lỗi quan sát.

Chi phí 0 credit cho mục này ở mức bằng chứng trung bình cao: changelog không ghi thẳng "0 credit", con số này đến từ một bài đăng mạng xã hội cùng ngày 10/04/2026. Cảnh báo vận hành: hai thread hỗ trợ Google (20/05/2026 và 13/07/2026) là người dùng ĐÃ TRẢ TIỀN Ultra nhưng VẪN KHÔNG thấy option này (một trường hợp có mã số case kỹ thuật của Google) — vậy kể cả lên Ultra cũng không chắc chắn có, có thể đang rollout dần hoặc theo khu vực.

Đây cũng là lần thứ ba Google áp dụng chính sách 0-credit tạm thời riêng cho Ultra: 26/08/2025 ("Ultra subscribers: Veo 3 - Fast is now 0 credits"), 25/11/2025 ("Ultra tier: return of zero credit Veo 3.1 Fast generations"), 10/04/2026 (đổi sang Veo 3.1 Lite Lower Priority) [live, changelog.md]. Gói Pro chưa từng được hưởng chế độ 0-credit này.

### 2.4 Gói và hạn mức credit

Free: 50 credit/ngày, không cộng dồn (reset hàng ngày, chính thức từ thay đổi changelog "Free credits now refresh daily" ngày 03/02/2026). AI Plus: +200/tháng. AI Pro: +1.000/tháng. AI Ultra 100 USD: +10.000/tháng. AI Ultra 200 USD: +25.000/tháng [tài liệu chính thức Google, đọc ngày 06/09/2026 qua công cụ tóm tắt trung gian nên thấp hơn một mức so với [live]]. Credit KHÔNG cộng dồn sang tháng/ngày sau. AI credit KHÔNG khả dụng ở Nhật Bản.

Clip rẻ nhất có thể tạo trên tài khoản trả phí: Omni 1.1 Flash, 360p, 4 giây = 4 credit. Với 50 credit miễn phí mỗi ngày, làm được khoảng 12 clip nháp/ngày [live, bảng giá đo trực tiếp trên tài khoản ngày 06/09/2026].

### 2.5 Sổ credit ở Google One đã đổi cơ chế, và nó mâu thuẫn với chính Flow

Đây là phát hiện của lần đo ngày 08/09/2026 và nó ảnh hưởng tới cách kiểm tra số dư.

Mở `one.google.com/ai/activity` trên tài khoản Pro thì trang hiện **`AI credits: 0`** kèm
một dòng cảnh báo nguyên văn: *"AI credits included with your plan have been replaced by
product-based usage limits"*, dẫn tới `support.google.com/googleone/answer/16287445`. Mục
hoạt động gần đây thì trống, ghi *"No recent activity"* `[live 08/09/2026]`.

Nhưng ngay bên trong Flow, panel cài đặt vẫn hiện số credit cụ thể trước mỗi lần sinh, đo
được nguyên văn `Generating will use 12 credits` `[live 08/09/2026]`.

Hai dòng chữ này nói ngược nhau. Chưa xác minh được cơ chế thật. Giả thuyết là có hai tầng
riêng biệt: Flow tự quản một quỹ credit của riêng nó, còn thứ bị thay bằng hạn mức theo sản
phẩm là phần credit cộng thêm mua qua Google One. **Đây là giả thuyết, chưa kiểm chứng.**

Hệ quả thực tế cho cách làm việc: **đừng dùng `one.google.com/ai/activity` làm nguồn số dư
nữa**. Nguồn đáng tin duy nhất hiện nay là nhãn `Generating will use N credits` hiện ngay
trong panel cài đặt của Flow trước khi bấm sinh. Nhãn đó vừa cho biết giá, vừa là cách duy
nhất còn hoạt động để đối chiếu chi phí.

---

## 3. Tỉ lệ khung hình, độ phân giải, thời lượng

### 3.1 Ảnh

Tỉ lệ khung hình trong composer chính: **5 lựa chọn — 16:9, 4:3, 1:1, 3:4, 9:16** [b01 t=150s; b05 t=150s; b14 t=399s; b16; xác nhận lại ở Agent settings mục "Image generation default" b22 t=1405s]. Bài đăng chính thức của tài khoản Flow trên X xác nhận thêm rằng tính năng "New Image Aspect Ratios" ra mắt 19/03/2026 chính là gốc của việc ảnh có thêm 4:3, 1:1, 3:4 [bài đăng chính thức của tài khoản Flow trên X, đối chiếu với `changelog.md` mục ngày 19/03/2026].

Số lượng ảnh sinh mỗi lần: **1x, x2, x3, x4** (như nhau cho mọi công cụ có tùy chọn này).

Độ phân giải ảnh: KHÔNG quan sát được dropdown độ phân giải riêng cho ảnh trong composer chính của Flow qua các frame đã xem (khác với AI Studio, nơi có "1K"/"2K" — nhưng đó là công cụ khác, không tính) [chưa xác minh].

### 3.2 Video

Tỉ lệ khung hình: CHỈ 2 lựa chọn — **16:9 và 9:16** — xác nhận nhất quán qua nhiều nguồn độc lập: vision b20/b21/b22/b23 (composer, Frames tab, Agent settings mục "Video generation default" chỉ có 2 nút) VÀ tài liệu HTML gốc của Veo API đọc trực tiếp (`[live, doc Veo đọc bằng HTML thô ngày 06/09/2026]`: `aspectRatio` chỉ nhận "16:9" hoặc "9:16", không có 21:9, không có 4:3, không có Custom).

Thời lượng: **4 mức cố định — 4s, 6s, 8s, 10s**, với 8s thường được gắn nhãn "Recommended" trong popup chọn thời lượng khi bắt đầu ("Thời lượng mỗi cảnh video bạn muốn? 1) 8 giây (Recommended) 2) 10 giây 3) 6 giây 4) 4 giây" + nút "Something else"/"Skip") [b16 t=3s]. Tính năng 4s/6s ra mắt chính thức từ changelog "Link Sharing and 4s/6s Videos" ngày 21/04/2026 [live, changelog.md] — các video quay TRƯỚC mốc này có thể chỉ thấy 2 lựa chọn 8s/10s cố định, chưa xác minh cụ thể video nào rơi vào trường hợp đó.

Ở cấp API (`[live, doc Veo đọc bằng HTML thô ngày 06/09/2026]`), tham số `durationSeconds` nhận giá trị KIỂU CHUỖI "4"/"6"/"8" (không phải số nguyên), và BẮT BUỘC phải là "8" khi dùng tính năng extension, reference images, hoặc độ phân giải 1080p/4K. Lưu ý: giá trị 10s xuất hiện trên UI Flow không khớp trực tiếp với danh sách "4"/"6"/"8" của tham số API cấp thấp này — cơ chế nội bộ để tạo video 10 giây trong UI (có thể ghép nhiều đoạn, hoặc dùng tham số khác) chưa được xác minh.

Độ phân giải: tài liệu HTML gốc của Veo (`[live]`) ghi Veo 3.1 hỗ trợ "720p" (mặc định), "1080p", "4k" (4K không có ở bản Lite); "the higher the resolution, the higher the latency will be. 4k videos are also more expensive"; "Video extension is also limited to 720p videos." Trên UI Flow chính, KHÔNG quan sát được dropdown độ phân giải riêng cho model Veo qua các frame vision đã xem — chỉ thấy độ phân giải là biến số ĐO ĐƯỢC cho riêng model Omni (360p/720p, xem bảng credit ở Mục 2). [chưa xác minh UI chọn resolution cho Veo trông như thế nào trên màn hình thật].

Đo lại ngày 08/09/2026 trên tài khoản Pro, panel cài đặt khi model là Omni 1.1 Flash chỉ
có **hai** mức độ phân giải: `360p` kèm chú thích nguyên văn *"360p generates faster at
lower resolution"*, và `720p` đang được chọn. **KHÔNG có 1080p và không có 4K trong ô chọn
lúc sinh** `[live 08/09/2026]`.

Đây là chỗ dễ hiểu lầm nhất sau bản cập nhật 27/08/2026, nên tách bạch cho rõ.

| Việc | Có những mức nào |
|---|---|
| Lúc SINH video | 360p và 720p, chỉ với Omni. Đây là cái quyết định giá clip |
| Lúc TẢI VỀ hoặc XUẤT | Thêm 1080p và 4K, dưới dạng nâng độ phân giải cho clip đã có |

Nói cách khác, 1080p và 4K không phải là mức để sinh mà là mức để nâng. Điều này khớp với
bảng giá: nâng lên 1080p miễn phí cho người trả phí, nâng lên 4K tốn 50 credit và chỉ Ultra
`[doc, support.google.com/flow/answer/16526234, 08/09/2026]`. Ai đi tìm ô 1080p trong panel
lúc sinh sẽ không thấy, và đó là đúng thiết kế chứ không phải lỗi.

Số lượng video sinh mỗi lần: **1x, x2, x3, x4**, giống ảnh.

Giới hạn chỉnh sửa: video dài hơn 10 giây KHÔNG chỉnh sửa được trong editor, hiện cảnh báo nguyên văn *"Videos longer than 10s can't be edited. Trim to 10s or under to edit."* kèm nút **"Trim Automatically"** [b22 t=1382s, t=1424s; khớp lại ghi chép xem frame video hướng dẫn].

Mặc định khi tạo video qua Agent (không tùy chỉnh gì thêm): 8 giây, x1 [b21 t=1112s, t=1348s].

---

## 4. Chế độ tạo: Văn bản, Frames to Video, Ingredients to Video

### 4.0 Bảng năng lực chính thức theo model — đọc bảng này TRƯỚC khi chọn model

Nguồn: `https://support.google.com/flow/answer/16352836`, đọc ngày 08/09/2026 `[doc]`.
Đây là câu trả lời có thẩm quyền cho câu hỏi "model nào làm được chế độ nào, ở thời lượng
nào". Trước đợt cập nhật này skill không hề có bảng nào tương đương, nên người dùng phải
đoán, và đoán sai thì mất credit.

| Chế độ | Veo 3.1 Lite | Veo 3.1 Fast | Veo 3.1 Quality | Gemini Omni Flash 1.1 |
|---|---|---|---|---|
| Text to Video | 4s, 6s, 8s | 4s, 6s, 8s | 4s, 6s, 8s | 4s, 6s, 8s, 10s |
| Frames to Video: First | 4s, 6s, 8s | 4s, 6s, 8s | 4s, 6s, 8s | 4s, 6s, 8s, 10s |
| Frames to Video: First and last | 4s, 6s, 8s | 4s, 6s, 8s | 4s, 6s, 8s | 4s, 6s, 8s, 10s |
| Ingredients / References to Video | chỉ 8s | chỉ 8s | KHÔNG hỗ trợ | 4s, 6s, 8s, 10s |
| Extend videos | chỉ 8s, áp lên video do ba model Veo 3.1 sinh | KHÔNG hỗ trợ | KHÔNG hỗ trợ | ghi "Coming Soon" |
| Video to Video editing | KHÔNG hỗ trợ | KHÔNG hỗ trợ | KHÔNG hỗ trợ | có, video tối đa 10 giây |

Mọi chế độ trong bảng đều chạy được ở cả hai tỉ lệ khung hình.

Bốn kết luận rút ra từ bảng này.

Thứ nhất, **chỉ Veo 3.1 Lite mới nối dài được video**. Bản Fast và bản Quality đều không.
Đây là điều ngược với trực giác, vì Lite là bản rẻ nhất. Nếu cần một cảnh dài hơn 8 giây
bằng đường Veo thì bắt buộc phải sinh bằng Lite ngay từ đầu.

Thứ hai, **chỉ Gemini Omni Flash mới sửa được video đã có**. Chi phí là 40 credit mỗi lần
sửa, đắt hơn cả một clip 10 giây ở 720p vốn chỉ 15 credit. Hãy cân nhắc sinh lại thay vì sửa.

Thứ ba, **Veo 3.1 Quality không nhận Ingredients**. Quy trình giữ nhân vật nhất quán bằng
Ingredients không dùng được với model chất lượng cao nhất. Cách đi thực tế là chốt nhân vật
bằng Lite hoặc Fast, rồi mới nghĩ tới Quality cho cảnh cần đẹp nhất, và chấp nhận rằng cảnh
đó không có Ingredients.

Thứ tư, **Ingredients trên Veo bị khoá cứng ở 8 giây**. Chỉ Omni mới cho chọn thời lượng
khác khi dùng Ingredients.

### 4.0b Mâu thuẫn chưa giải quyết về ô chọn thời lượng của Veo

Bảng chính thức ở trên ghi cả ba model Veo 3.1 đều hỗ trợ 4s, 6s và 8s cho Text to Video.
Nhưng phần đo trực tiếp ở mục 2.2 lại ghi ba model Veo "không chọn được resolution và
duration riêng", đo trên tài khoản Pro ngày 06/09/2026.

Hai khả năng, chưa biết cái nào đúng.

Một, giao diện Flow không phơi ô chọn thời lượng cho Veo dù model có hỗ trợ ở cấp API. Khi
đó bảng chính thức mô tả năng lực model, còn phép đo mô tả năng lực giao diện, và cả hai
đều đúng theo cách riêng.

Hai, phép đo ngày 06/09/2026 đã bỏ sót ô đó, hoặc giao diện đã đổi sau bản cập nhật ngày
27/08/2026.

**Chưa được kết luận bên nào sai.** Khi cần dùng, hãy tự mở panel cài đặt, chọn từng model
Veo, và đọc xem có ô duration hay không, rồi cập nhật lại mục này kèm ngày đo.

Đã thử giải quyết ngày 08/09/2026 nhưng KHÔNG xong. Lần đo đó mở panel cài đặt khi model
đang chọn là Omni 1.1 Flash và đọc được đủ bốn mốc 4s, 6s, 8s, 10s, tất cả đều bấm được
trên tài khoản Pro. Nhưng phép đo đó **không chuyển sang từng model Veo rồi đọc lại panel**,
nên nó không nói được gì về Veo. Mâu thuẫn vẫn còn nguyên. Đây chính xác là một bước còn
thiếu, không phải một câu trả lời.

Một dữ kiện phụ thu được cùng lần đo đó: changelog ngày 21/04/2026 giới thiệu hai mốc 4
giây và 6 giây như tuỳ chọn thử nghiệm dành cho người dùng Ultra, nhưng tài khoản Pro ngày
08/09/2026 chọn được cả hai và không bị khoá `[live 08/09/2026]`. Nghĩa là tính năng đã mở
rộng ra ngoài Ultra sau đó, dù không có mục changelog nào ghi lại việc mở rộng.

### 4.0c Mâu thuẫn thứ hai: Omni có nhận cả khung đầu lẫn khung cuối không

Hai nguồn chính thức nói ngược nhau và đây là mâu thuẫn về THỜI GIAN, không phải về sự thật.

Changelog ngày 04/06/2026 và 10/06/2026 nói nguyên văn: *"Note: Omni Flash currently
supports First Frame only; First + Last Frame combinations coming soon!"* `[changelog]`.

Bảng năng lực chính thức đọc ngày 08/09/2026 lại ghi Gemini Omni Flash 1.1 hỗ trợ cả
`Frames to Video: First and last` ở 4, 6, 8 và 10 giây
`[doc, support.google.com/flow/answer/16352836, 08/09/2026]`.

Giải thích khả dĩ nhất là lời hứa "coming soon" hồi tháng 6 đã được thực hiện trong bản
Gemini Omni Flash 1.1 ra ngày 27/08/2026, và bảng năng lực là bản mới hơn nên đúng hơn.
Đây là SUY LUẬN, chưa xác minh. Trước khi dựa vào khung cuối với Omni, hãy tự mở tab Frames
và xem có đủ cả ô Start lẫn ô End hay không.

### 4.1 Bốn tab của panel cấu hình

Panel cấu hình khi ở chế độ Video có đúng **4 tab**: **Image, Video, Frames, Ingredients** [b16 t=42s; b20 t=169s].

**Văn bản (Text/Voice-over-to-Video)** — chế độ mặc định, gõ mô tả cảnh tự do vào ô nhập chính. Có thể dùng mẫu câu chuyên biệt "Create a video base on the voice over: Voice Over: ... Note: Realistic Video, show the shock and viral. Text animation with eye-catching in the middle" để Flow tự dựng hình ảnh minh họa khớp với đoạn lời đọc cho trước [b20 t=169-333s]. Dùng khi: đã có kịch bản/lời thoại rõ ràng, muốn Flow tự nghĩ ra hình ảnh minh họa.

**Frames to Video** — mở qua "Model picker → Frames tab", thay ô nhập tự do bằng cặp nút **"Start"** và **"End"** (có mũi tên hai chiều ⇄ giữa chúng), cho phép nạp ảnh đầu và ảnh cuối để Flow nội suy chuyển động nối liền giữa hai khung hình [b05 t=189.8s; b16 t=109s]. Dùng khi: đã có 2 ảnh cố định (ví dụ storyboard scene đầu/cuối) và muốn Flow tự tạo chuyển động nối giữa chúng, hoặc khi làm hoạt hình animation từ ảnh 2D. Tính năng chính thức "Frame to Video now available for Gemini Omni Flash" ra mắt 04/06/2026, và "Omni Frames to Video" mở rộng thêm 10/06/2026 [live, changelog.md] — cho thấy Frames to Video ban đầu chỉ dành cho Veo, sau mới mở rộng sang Omni.

**Ingredients to Video** — ghép nhiều ảnh "nguyên liệu" riêng biệt (người, trang phục, phụ kiện, bối cảnh...) vào cùng một cảnh bằng cách đính kèm nhiều ảnh tham chiếu rồi mô tả cách kết hợp, ví dụ prompt thật: *"The girl in image 1 wearing exactly the tank top in image 2 and exactly pants in image 3, wearing exactly glasses in image 4. Place her in a suitable background with the outfit and posing exactly like image 5"* [b20 t=549-553s]. Dùng khi: cần giữ đúng nhiều yếu tố hình ảnh tách rời (trang phục cụ thể, phụ kiện cụ thể, tư thế tham chiếu) hợp nhất vào một nhân vật/cảnh mà không cần dựng character reference sheet đầy đủ trước. Theo changelog chính thức, "Ingredients to Video" đã có với Veo Lite từ 16/04/2026 và trước đó đã hỗ trợ định dạng dọc (Portrait) từ 18/12/2025 — tức đây là tính năng có lịch sử phát triển riêng, không phải phần phụ của Frames [live, changelog.md].

Ghi chú liên quan (Voice là "ingredient" riêng): có thể gắn đồng thời Character reference + Voice + Storyboard image làm 3 "ingredients" vào cùng một prompt video, ví dụ đã làm thật khi tạo video từ storyboard có nhân vật cố định và giọng đọc cố định [b17 t=634s]. "Experimental Voice Ingredients for Ultra Users" là tính năng chính thức riêng từ 02/04/2026 theo changelog — có thể đây là cơ chế gắn giọng nói dưới dạng ingredient khác với việc gắn Voice thông thường vào Character, [cần kiểm lại, chưa xác minh chi tiết khác biệt].

**Extend** — nối dài một clip đã có bằng cách phân tích khung hình cuối rồi sinh tiếp hành
động, thay vì sinh lại từ đầu. Theo bảng chính thức, trong Flow chỉ **Veo 3.1 Lite** làm
được, ở mức 8 giây mỗi lần, và chỉ áp lên video do một trong ba model Veo 3.1 sinh ra. Với
Omni thì bảng ghi "Coming Soon" `[doc, support.google.com/flow/answer/16352836, 08/09/2026]`.
Giá bằng đúng giá sinh một clip cùng model, tức 10 credit với Lite và 5 với Ultra
`[doc, support.google.com/flow/answer/16526234, 08/09/2026]`.

Ở cấp API thì con số khác hẳn và rộng hơn nhiều. Veo qua Gemini API nối dài được video đầu
vào tới 141 giây và cho ra tối đa 148 giây, nhưng chỉ với `veo-3.1-generate-preview` và
`veo-3.1-fast-generate-preview`, và video đầu vào phải là 720p
`[doc, ai.google.dev/gemini-api/docs/veo, 08/09/2026]`. Omni qua Interactions API nối được
vào cuối clip cho tới tổng 40 giây `[doc, ai.google.dev/gemini-api/docs/omni, 08/09/2026]`.
Chi tiết tham số nằm ở `api-guide.md`.

Đây là chỗ giao diện và API lệch nhau rõ nhất trong toàn bộ Flow. Nếu cần một cảnh liền
mạch dài hơn 10 giây thì đường API mạnh hơn hẳn đường giao diện.

**Video to Video editing** — sửa một video đã có bằng mô tả bằng lời, giữ nguyên phần không
đổi. Theo bảng chính thức chỉ **Gemini Omni Flash 1.1** làm được, và video phải từ 10 giây
trở xuống. Giá 40 credit mỗi lần sửa
`[doc, support.google.com/flow/answer/16526234, 08/09/2026]`.

Ba điều cần cân nhắc trước khi dùng. Thứ nhất, 40 credit đắt hơn sinh mới một clip 10 giây
720p vốn chỉ 15 credit, nên nếu chỉ cần đổi nội dung thì sinh lại rẻ hơn; sửa chỉ đáng khi
cần GIỮ phần lớn khung hình cũ. Thứ hai, ở khu vực EEA, Thuỵ Sĩ và Anh thì không sửa được
video TẢI LÊN, còn video do model sinh ra thì vẫn sửa được ở mọi nơi
`[doc, ai.google.dev/gemini-api/docs/omni, 08/09/2026]`. Thứ ba, định dạng tải lên được là
`.mov`, `.mp4`, `.avi`, `.wmv`, tối đa 60 giây và 1GB
`[doc, support.google.com/flow/answer/16935718, 08/09/2026]`; con số 60 giây này là giới hạn
tải lên, còn giới hạn sửa vẫn là 10 giây.

---

## 5. Characters và Voices

### 5.1 Cách tạo Character (tóm tắt quy trình đầy đủ)

1. Sidebar > Characters > "New Character" > chọn 1 trong 4-6 mẫu preset (**The Familiar, The Eccentric, The Wicked, The Fantastical**, và ở một số bản có thêm **The Professional, The Wildcard**) hoặc gõ mô tả tự do.
2. Model ảnh mặc định: **Nano Banana 2** (đôi khi **Nano Banana Pro** khi cần ghép nhiều ảnh tham chiếu).
3. Có thể gõ mô tả ngắn bằng tiếng Việt rồi bấm nút **"Format"** để Flow tự viết lại thành prompt tiếng Anh chi tiết (kèm loại máy ảnh, ống kính, ánh sáng studio). Ví dụ thật: mô tả gốc *"Tạo nhân vật mẹ chồng ở độ tuổi U60, mẹ chồng miền Bắc, hiện đại, mặc đồ sang trọng nhưng mà khó tính"* được Format thành một đoạn tiếng Anh dài mô tả chi tiết trang phục Áo Dài, ánh sáng clamshell, máy ảnh Hasselblad H6D-100c, ống kính 50mm [b12 t=227-240s].
4. Vào trang chi tiết Character: đặt tên, bấm **"Select a voice"** để gắn giọng, điền **"Character Info (optional)"** — mô tả tính cách để Agent tham khảo khi tạo cảnh sau này (ví dụ: *"nhân vật này bình tĩnh, điềm đạm và đĩnh đạc"* [b23 t=366s]).
5. Bấm **"Create Body"** để sinh ảnh toàn thân 3 góc (triptych front/3-4/back) từ chân dung đã có, dùng prompt mẫu Flow gợi ý sẵn (xem 1.3).
6. Muốn thêm biến thể góc chụp/trang phục: gắn thêm ảnh tham chiếu qua asset picker "+" rồi mô tả yêu cầu, ví dụ *"Tạo cho tôi phiên bản 2D của cô gái này, giữ nguyên đường nét gương mặt, tóc, trang phục, để nền trắng"* [b21 t=805s].

### 5.1b Gọi nhân vật bằng cú pháp @ ngay trong prompt

Đây là cách dùng mà skill trước đây hoàn toàn không có, dù nó là cách nhanh nhất để giữ
nhân vật nhất quán mà không phải gắn ảnh thủ công mỗi lần.

**`@tên_nhân_vật`** gọi một Character đã lưu vào thẳng prompt. Changelog ngày 19/05/2026
giới thiệu Characters với khẩu hiệu nguyên văn *"Design once, cast anywhere"*: tạo nhân vật
một lần từ mô tả bằng chữ hoặc từ ảnh tham chiếu, gắn giọng nói cho nó, rồi gõ
`@character_name` trong prompt để đưa nhân vật đó vào cảnh `[changelog]`.

**`@me`** đưa chính bạn vào cảnh. Cùng mục changelog ngày 19/05/2026 mô tả đường thao tác:
vào Account Settings, chọn `Create avatar`, quay một video selfie ngắn và đọc vài từ để ghi
lại giọng, sau đó gõ `@me` trong prompt `[changelog]`. Tính năng này **không dùng được ở
khu vực EEA, Anh và Thuỵ Sĩ**.

Giao diện thật xác nhận có hạ tầng cho cả hai: bảng chọn asset khi bấm nút thêm ingredient
có đủ các tab `All`, `Images`, `Videos`, `Voices`, `Characters`, `Avatars`, `Uploads`
`[live 08/09/2026]`. Tab `Avatars` tách riêng khỏi tab `Characters`, tức đây là hai khái
niệm khác nhau chứ không phải một.

Chưa xác minh: chưa tự gõ `@` trong ô prompt để xem danh sách gợi ý hiện ra thế nào, và
chưa thử `@me` vì tài khoản chưa tạo avatar.

### 5.2 Giới hạn ký tự

**Sample Dialogue** (dùng khi nghe thử giọng): giới hạn hiển thị **0/120 characters** — xác nhận nhất quán qua nhiều video độc lập (b01, b06, b12, b17, b23).

### 5.3 Danh sách giọng đọc (Voices)

Danh sách tên giọng + mô tả ngắn quan sát được qua UI Flow (gộp từ nhiều video, KHÔNG một video nào chụp đủ hết trong 1 lần, tổng cộng hơn 20 tên riêng biệt xuất hiện rải rác):

Achernar (Female, soft, high pitch), Achird (Male, friendly, mid pitch), Algenib (Female, gravelly, low pitch), Algieba (Male, easy-going, mid-low pitch), Alnilam (Male, firm, mid-low pitch), Aoede (Female, breezy, mid pitch), Autonoe (Female, bright, mid pitch), Callirrhoe (Female, easy-going, mid pitch), Charon (Male, informative, lower pitch), Despina (Female, smooth, mid pitch), Enceladus (Male, breathy, lower pitch), Erinome (Female, clear, mid pitch), Fenrir (Male, excitable, younger pitch), Gacrux (Female, mature, mid pitch), Iapetus (Male, clear, mid-low pitch), Kore (Female, firm, mid pitch), Laomedeia (Female, upbeat, mid-high pitch), Sadachbia (Male, lively, low pitch), Sadaltager (Male, knowledgeable, mid pitch), Schedar (Male, even, mid-low pitch), Sulafat (Female, warm, mid pitch), Umbriel (Male, smooth, lower pitch), Vindemiatrix (Female, gentle, mid pitch), Zephyr (Female, bright, mid-high pitch), Zubenelgenubi (Male, casual, mid-low pitch) [b12 t=117.6s; b17 t=637s; b23 t=311-393s].

Cần phân biệt rõ hai ngữ cảnh khác nhau, KHÔNG gộp thành một con số: danh sách trên là quan sát UI Flow (đếm dồn qua nhiều video, không phải một lần đếm đủ). Riêng ở cấp **API TTS** (`generation_config.speech_config`), bản tổng hợp tài liệu Gemini lấy qua công cụ fetch có model tóm tắt trung gian liệt kê **30 giọng**, gồm cùng bộ tên như trên cộng thêm vài tên chưa thấy trên UI Flow, ví dụ Puck, Leda, Orus, Rasalgethi, Pulcherrima. Mức bằng chứng ở đây là **trung bình**, không phải `[live]`, và trong 30 tên đó nhóm mới tự gọi thử được 5 tên. Đây là số liệu qua API, khác kênh với UI Flow, nên không chắc UI Flow lộ ra đúng 30 giọng này hay một tập khác.

Ví dụ giọng tùy chỉnh (Custom Voice) đã tạo thật:
- **"Mẹ chồng - Bà Nga"** — base Vindemiatrix; Voice Performance: *"Giọng tiếng Việt 100% của một người mẹ tuổi 60 ở Việt Nam. Người mẹ khó tính, giọng nói sẽ hơi đanh đá, chua ngoa một chút. Nói tiếng Việt tự nhiên"* [b12 t=132.6s].
- **"Aoede Custom"** và **"Nữ Việt Nam"** — base Aoede; Customize Performance: *"Giọng nói dùng tiếng Việt miền Bắc chuẩn, không lơ lớ, nói tự nhiên."* [b17 t=870s].
- **"giọng nam trầm"** — base Aoede; Voice Performance: *"tôi muốn nó là giọng nói có âm sắc trầm phù hợp với một người đàn ông gốc Phi từ 20 đến 30 tuổi"* [b23 t=340s]. Lưu ý cạm bẫy: sau khi đặt tên và mô tả này, nhãn preview card VẪN hiển thị mô tả CŨ kế thừa từ Base Voice gốc ("Female, breezy, mid pitch") — nhãn không tự cập nhật theo mô tả mới nhập [b23 t=340s].

### 5.4 Hạn chế ngôn ngữ — quan trọng nhất

Chính Agent/Gemini trong Flow xác nhận bằng CHỮ hiện trên màn hình (không phải suy đoán của người dùng): *"Tính năng tạo lời thoại và giọng nói trong các mô hình video của Google Flow (như Omni Flash) hiện tại chỉ hỗ trợ và tối ưu hóa cho tiếng Anh. Khi bạn nhập lời thoại bằng tiếng Việt, hệ thống tự động dịch hoặc chuyển hướng sang tiếng Anh vì công cụ tổng hợp giọng nói chưa thể xử lý và phát âm tiếng Việt."* [b12 t=571.7s]. Hai cách khắc phục do chính Agent gợi ý: (1) tạo video chỉ tập trung biểu cảm nhân vật không kèm lời nói, rồi tự lồng tiếng Việt bằng phần mềm ngoài; (2) thêm phụ đề tiếng Việt trực tiếp bằng công cụ dựng phim [b12 t=585.8s].

Thực tế quan sát khớp với cảnh báo trên: giọng tiếng Việt tạo trong Flow (kể cả với voice mặc định như "Aoede") bị "lơ lớ" — nghe như giọng nước ngoài cố đọc tiếng Việt [b16, b17]. Giải pháp phổ biến nhiều video độc lập cùng dùng: generate video KHÔNG lồng tiếng trong Flow, rồi lồng tiếng riêng bằng công cụ TTS tiếng Việt chuyên dụng (FPT AI, ElevenLabs) và ghép lại bằng Remotion hoặc CapCut [b16 t=512s; b17 t=643s].

### 5.5 Giới hạn thực tế khác về Voice

Giọng không sinh hết nếu lời thoại quá dài: giới hạn thực tế tối đa khoảng 10 giây lời thoại, trung bình 2 dòng thoại mỗi lượt tạo [b22, slide tổng kết do tác giả video tự soạn; khớp lại bảng lỗi ở Mục 9; chưa tự đo lại].

### 5.6 Cạm bẫy quan trọng: nhân vật trong video có thể KHÔNG khớp Character đã lưu

Quan sát trực tiếp: nhân vật xuất hiện trong video kết quả (một người đàn ông da trắng) hoàn toàn khác với Character "Untitled Character" (người đàn ông da đen) đã được tạo, gán giọng, và điền Character Info công phu ngay trước đó trong CÙNG một phiên làm việc [b23, mục Cạm bẫy]. Nguyên nhân chưa rõ ràng — có thể model không tự áp dụng đúng character đã lưu khi tạo video chỉ từ prompt văn bản (không kéo thả character vào prompt). Bài học: LUÔN kiểm tra kỹ nhân vật trong video kết quả, đừng giả định Flow tự nhận diện và áp dụng đúng Character đã lưu trên canvas nếu không chủ động gắn nó vào prompt bằng nút "+".

---

## 6. Scenes và Collections

Nút "+" cạnh sidebar mở 2 lựa chọn: **"Create Collection"** hoặc **"Create Scene"** [b21 t=1291-1329s; chưa tự mở lại trên tài khoản].

**Collection**: gom nhiều ảnh/video liên quan vào một nhóm, mỗi collection card hiện icon số lượng ảnh/video bên trong. Tên mặc định "Untitled Collection" vẫn dùng được nếu ảnh đại diện đã đủ gợi nhớ nội dung, không nhất thiết phải đổi tên [b21 t=1250s].

**Scene**: cho phép kéo nhiều clip khác nhau (không nhất thiết cùng nguồn gốc) vào chung MỘT dòng thời gian (timeline). Bên trong Scene, bấm "+" mở asset picker để chọn video có sẵn, rồi bấm **"Add to Scene"** để ghép clip vào timeline [b21 t=1312-1329s].

Khác biệt với Storyboard Studio (Mục 1.6): Scene là cơ chế TỔ CHỨC/ghép clip đã có sẵn thành một dòng thời gian chung, còn Storyboard Studio là một TOOL riêng chuyên tạo mới nội dung theo kịch bản (script → cast → storyboard) rồi mới xuất ra từng ảnh/clip để đưa vào Scene hay project.

---

## 7. Agent mode

### 7.1 Kích hoạt và luồng duyệt cơ bản

Nút **"Agent"** nằm cạnh khung nhập chính. Bấm vào mở panel chat riêng bên phải (tên phiên mặc định "Untitled session", có nút đổi tên bằng bút chì, nút đóng X) [b01 t=178.6-201.5s].

Trước khi tạo bất kỳ nội dung nào tốn credit, Agent LUÔN hỏi xác nhận theo mẫu: *"Would you like me to kick off these N image/video generations, costing X credits?"* với hai nút **Reject / Approve** [b01 t=209.6s, t=312.9s]. Kèm toggle **"Approve, do not ask again"** — mô tả đầy đủ: *"Switching this on lets the agent generate freely across this entire project without asking first."* — mặc định TẮT [b01 t=209.6s].

Khi tải cao, Agent có thể trả lời rằng đã "lên lịch và đang chờ xử lý do nhu cầu cao. Bạn có thể kiểm tra lại sau vài phút nhé" thay vì render ngay [b22 t=1363s] — khớp với banner chính thức toàn site: *"Flow is currently experiencing high demand, affecting video generation. Requests may need to be retried at a later time. AI Credits will be refunded for any failed requests."* [live, danh mục tool đọc từ DOM ngày 06/09/2026].

Quan sát: Agent đôi khi trả lời bằng TIẾNG ANH dù người dùng hỏi bằng tiếng Việt, ngay trong cùng một cuộc hội thoại (ví dụ: *"I'll generate a video of a cute kitten cooking grilled oysters with scallion oil—a delicious choice!"* để trả lời một câu hỏi tiếng Việt) [b22 t=1354s].

### 7.2 Agent Settings

Mở qua icon bánh răng cạnh nút Agent. Có 2 mục cấu hình chính:

**Xác nhận trước khi tạo** — 2 lựa chọn dạng radio: **"Always"** (mặc định, Agent hỏi xác nhận trước khi tạo) / **"Never"** (Agent tự tạo và tự tốn credit không hỏi lại) [b22 t=1405s, t=1491s].

**Image generation default**: tỉ lệ khung hình (5 nút 16:9/4:3/1:1/3:4/9:16), số lượng (1x/x2/x3/x4), model mặc định **"Nano Banana 2"**.

**Video generation default**: tỉ lệ khung hình (CHỈ 2 nút 16:9/9:16 — ít hơn hẳn so với ảnh), số lượng (1x/x2/x3/x4), model mặc định **"Omni Flash"** [b22 t=1405s, t=1495s].

### 7.3 Agent Instructions

Panel riêng để lưu hướng dẫn phong cách áp dụng xuyên suốt TOÀN BỘ dự án, không phải chỉ một lần tạo. Gồm 2 ô văn bản (ví dụ: mô tả nhân vật lặp lại xuyên suốt, mô tả phong cách hình ảnh chung), nút **"+ Add Instruction"**, có thể gắn thêm ảnh tham chiếu qua asset picker rồi bấm **"Add to instruction"**, nút **"Done"** ở cuối [b22 t=1412-1415s].

Theo chính lời giải thích của Agent (đọc nguyên văn trên màn hình, kèm link nguồn tham chiếu chính thức *"Use the Google Flow Agent - Section: Add instructions for the Google Flow Agent"*): *"Agent Instructions là tính năng giúp bạn duy trì sự nhất quán trong suốt quá trình thực hiện dự án. Bạn có thể hiểu nó như một bản 'hướng dẫn phong cách' riêng biệt cho Agent: Thiết lập quy tắc — Bạn có thể thêm hình ảnh tham chiếu và các chỉ dẫn cụ thể về cách mà Agent nên hành xử hoặc sáng tạo nội dung. Duy trì tính nhất quán — Những hướng dẫn này sẽ được áp dụng cho toàn bộ dự án, giúp các sản phẩm tạo ra sau này luôn được đồng bộ về phong cách hoặc nội dung theo ý bạn."* [b22 t=1405s].

Quy trình thao tác thật đã ghi lại: mở asset picker (tab All/Images/Characters/Avatar), chọn một "Saved Frame" đã lưu trước đó, bấm "Add to instruction" — hệ thống hiện thông báo "Uploading frame..." rồi "Frame saved as image" kèm link "View image"/"Dismiss" [b22 t=1412-1430s].

---

## 8. Giới hạn cứng (mọi con số đọc trực tiếp trên màn hình)

- Sample Dialogue (Voice): giới hạn **120 ký tự** (0/120) [b01, b06, b12, b17, b23].
- Video dài hơn **10 giây** KHÔNG chỉnh sửa được trong editor (phải Trim Automatically) [b22; live].
- Tỉ lệ khung hình Video: chỉ **2 lựa chọn** (16:9, 9:16). Tỉ lệ khung hình Ảnh: **5 lựa chọn** (16:9, 4:3, 1:1, 3:4, 9:16).
- Số lượng sinh mỗi lần: tối đa **x4** (1x/x2/x3/x4), như nhau cho ảnh và video.
- Thời lượng video: **4 mức cố định** 4s/6s/8s/10s. API cấp thấp chỉ nhận chuỗi "4"/"6"/"8" và BẮT BUỘC "8" khi dùng extension/reference images/1080p/4K [live, doc Veo đọc bằng HTML thô ngày 06/09/2026].
- Video Resizer (đo `[live]` bằng ffprobe): Output Ratio đúng **6 mục** — 9:16, 16:9, 1:1, 4:5, 21:9, Custom. Custom: input Width/Height min=1, max=**4096**, giá trị mặc định 1080×1080, nhưng đầu ra CHỈ LẤY TỈ LỆ, chiều rộng đầu ra LUÔN LUÔN chuẩn hóa về **1280px** bất kể số pixel đã gõ hay độ rộng nguồn (đã thử với nguồn 640px và 1280px, đều ra 1280 chiều rộng). [chưa xác minh] với nguồn rộng 1920px hoặc 1080p — nếu quy luật giữ nguyên, đưa clip 1080p vào tool này sẽ bị HẠ xuống 1280px, tức MẤT độ phân giải.
- Free tier: **50 credit/ngày**, không cộng dồn. AI Plus **+200/tháng**. AI Pro **+1.000/tháng**. AI Ultra 100 USD **+10.000/tháng**. AI Ultra 200 USD **+25.000/tháng** [live].
- Upscale 1080p: miễn phí cho subscriber. Upscale 4K: **50 credit**, chỉ Ultra.
- Canvas Image Editor mặc định: **Width 1344px, Height 768px** (Preset "Default") [b01, b35].
- Background Removal (Image Editor): **"MODNet (People, Fast)"**.
- Font Text Layer: Google Sans, Inter, Bebas Neue, Montserrat, Playfair Display, Cinzel (danh sách còn cuộn thêm, chưa xác nhận hết).
- 12 loại Mockup dựng sẵn (laptop, phone, tv, shirt, hat, bag, pin, book, poster, window, billboard, mural) + custom.
- Explore Tools: đúng **3 tab** (My Tools, Community, Templates) tính đến 06/09/2026 [live].
- Voice không sinh hết nếu lời thoại quá dài: giới hạn thực tế tối đa khoảng **10 giây**, trung bình **2 dòng thoại**.

---

## 9. Lỗi thường gặp và cách xử lý

Bảng 3 lỗi phổ biến nhất, lấy từ slide tổng kết chính thức trong video hướng dẫn (khớp lại độc lập giữa ghi chép xem frame và b22):

| Lỗi | Cách xử lý (ghi trên slide/UI) |
|---|---|
| Clip bị blur hoặc nhân vật biến dạng | Đơn giản hóa mô tả, tách ra thành nhiều clip ngắn hơn thay vì nhồi tất cả vào một cảnh |
| Voice không được gen hết khi tạo | Cắt xén câu thoại tối đa 10 giây, trung bình 2 dòng mỗi câu lệnh |
| Audio lệch không khớp với hình | Chia lời thoại thành đoạn ngắn hơn, generate từng đoạn thay vì một lần dài |

Các lỗi kỹ thuật khác quan sát trực tiếp trên màn hình (không phải slide tổng kết mà là sự cố thật xảy ra khi thao tác):

- **"Chunk upload failed: 400"** khi build custom Tool ("Story Animator") — Agent tự báo đã sửa bằng "Strict Data Validation", "FFmpeg Result Checking", "Memory Management" [b21 t=1026s].
- Prompt không submit được ở lần bấm đầu tiên khi một agent ngoài (Claude in Chrome) thao tác tự động — phải chụp lại màn hình xác định đúng nút gửi (mũi tên "→") rồi thử lại mới thành công [b17 t=623s].
- Asset ảnh tham chiếu "biến mất" khỏi asset picker giữa một phiên làm việc dài — không tìm lại được dù lọc theo tab Images/Characters hay tìm theo tên, phải dùng ảnh thay thế [b17 t=653s].
- Đổi Base Voice/mô tả giọng mới nhưng nhãn preview vẫn hiển thị mô tả CŨ kế thừa từ giọng gốc, không tự cập nhật [b23 t=340s].
- Nhân vật trong video kết quả có thể khác với Character đã lưu công phu trước đó — cần luôn kiểm tra lại (xem Mục 5.6) [b23].
- Tỉ lệ khung hình đã chọn trong bảng cấu hình (ví dụ "16:9") có thể hiển thị SAI trên icon của trang editor sau khi video đã tạo xong (hiện "9:16" dù chọn 16:9) — nghi là do icon mặc định của giao diện editor, chưa chắc phản ánh đúng tỉ lệ thật của file video [b23, chưa xác minh].

Cảnh báo hệ thống toàn site khi tải cao: *"Flow is currently experiencing high demand, affecting video generation. Requests may need to be retried at a later time. AI Credits will be refunded for any failed requests."* — có nghĩa Flow CÓ chính sách hoàn credit cho request thất bại do quá tải [live, danh mục tool đọc từ DOM ngày 06/09/2026].

---

## 10. Cạm bẫy

- **Không xuống dòng khi gõ prompt.** Nếu prompt bị xuống dòng (Enter), Flow hiểu thành NHIỀU lệnh riêng biệt và sinh dư thừa nhiều ảnh/video ngoài ý muốn — luôn viết prompt thành một đoạn liền mạch. Người dẫn của video `mCnR9j-Qk9Y` nhấn mạnh cạm bẫy này hai lần, ở b16 và b17, mà b16 với b17 là hai phần của CÙNG một video. Vậy đây là lời của một người, chưa có video độc lập nào khác xác nhận và nhóm cũng chưa tự thử `[chưa xác minh độc lập]`. Vẫn nên viết prompt liền mạch vì chi phí tuân thủ bằng không.
- **Giọng tiếng Việt bị "lơ lớ".** Mọi voice có sẵn trong Flow đều là giọng gốc nước ngoài đọc tiếng Việt — chính Agent xác nhận bằng chữ trên màn hình đây là hạn chế kỹ thuật thật, không phải lỗi dùng sai. Giải pháp: tạo video không lồng tiếng, lồng tiếng riêng bằng công cụ TTS tiếng Việt chuyên dụng rồi ghép ngoài Flow (xem Mục 5.4).
- **Yêu cầu "storyboard" có thể ra nhầm thành nhiều video** nếu không ép rõ chế độ "Image" — Flow/Agent có xu hướng tự hiểu "storyboard" thành việc tạo NHIỀU clip video riêng theo từng panel thay vì một ảnh lưới tĩnh. Phải yêu cầu tường minh "tạo đúng 1 ảnh" khi cần một storyboard grid [b16 t=463-501s].
- **Đổi từ chế độ tạo ẢNH sang VIDEO làm giao diện ô nhập thay đổi hoàn toàn** (từ prompt tự do sang cặp nút Start/End), dễ gây nhầm lẫn nếu không để ý kỹ đang ở chế độ nào [b05].
- **Mỗi cảnh Storyboard cần 2 ảnh** (START và FINISH image prompt), không phải 1 ảnh, để Flow nối thành video mượt mà — nguyên tắc này được nhấn mạnh bằng dòng chữ lớn "2 IMAGE PROMPT PER SCENE" chồng lên giao diện trong video hướng dẫn [b05 t=170.3s].
- **Quy ước đặt tên asset trong Video Resizer gây hiểu lầm**: tên file trong gallery ghi kích thước DANH NGHĨA người dùng đã gõ, KHÔNG phải kích thước THẬT của file kết quả — chỉ có tỉ lệ là khớp, số pixel trong tên luôn sai, phải tự đo (ffprobe hoặc công cụ tương đương) mới biết chính xác [live, số đo Video Resizer ngày 06/09/2026].
- **Tool cộng đồng (remix từ người khác) có thể sai và vẫn tốn credit** — luôn có cảnh báo cố định cuối trang: *"This app was created by another person and may be inaccurate or unsafe. Report unsafe content. This app may consume credits."* [b35 t=326s].
- **Nút "Format" trong tạo Character** tự động dịch và mở rộng mô tả ngắn tiếng Việt thành một prompt tiếng Anh chi tiết (kèm thiết bị máy ảnh, ánh sáng) — tiện lợi nhưng cần đọc lại kỹ nội dung AI tự thêm vào trước khi dùng, vì có thể thêm chi tiết không mong muốn.
- **Đặt tên tiếng Việt phải giữ đầy đủ dấu** khi dùng cho storyboard/video có chữ hiển thị trên hình, để tránh lỗi hiển thị chữ thiếu dấu — mẹo rút ra từ một chuỗi automation dài dùng Flow qua agent ngoài [b17, Insight 5].
- **Một chuỗi thao tác tự động hóa (agent ngoài điều khiển Flow) kéo dài nhiều bước có thể khiến ứng dụng điều khiển phải nén ngữ cảnh** ("Compacting conversation") — không phải lỗi của riêng Flow nhưng ảnh hưởng trực tiếp đến độ tin cậy của các workflow tự động hóa nhiều bước liên tiếp [b17 t=634s].
- **Giao diện Flow thay đổi khá nhanh theo thời gian** — số tab Explore Tools (2 → 3), số model trong dropdown video (4 → 5 tùy hạng tài khoản), số thẻ mẫu Character (4 → 6) đều khác nhau giữa các video quay ở thời điểm khác nhau. Khi áp dụng tài liệu này, nên đối chiếu lại với giao diện thật tại thời điểm sử dụng, đặc biệt là số credit chính xác vì phần này biến động nhiều nhất và ít được đo lại độc lập ngoài `[live]`.
