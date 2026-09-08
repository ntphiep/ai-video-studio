# Hệ sinh thái Flow Tools (Google Flow) — tài liệu tổng hợp

Nguồn: [live] = do agent tự mở giao diện Flow xác nhận trực tiếp ngày 06/09/2026 (mức bằng chứng cao nhất). [bXX] = agent xem frame video hướng dẫn kèm mốc giây gốc trong file. Mục nào chỉ dựa một nguồn duy nhất được gắn [chưa xác minh].

## 1. Ba tab của "Explore Tools" và danh mục đầy đủ

Trang vào: `flow.google.com/project/<id>/tools`, tiêu đề trang "Explore tools". Đúng **BA TAB**: My Tools, Community, Templates [live, danh mục tool đọc từ DOM ngày 06/09/2026]. Một số video hướng dẫn cũ gọi tab là "Discover" thay vì "Templates" và có nơi chỉ thấy 2 tab Discover/My Tools do tài khoản đó chưa có tool cộng đồng nào được thêm [b06, b20, b21, b35] — tên tab hiển thị có thể lệch theo phiên bản giao diện tại thời điểm quay, nhưng cấu trúc ba nhóm nội dung (tool của Google, tool cộng đồng, tool tự tạo) là nhất quán.

Banner đầu trang: "Build all the tools you can imagine. An idea and a description are all it takes to make whatever tool you need." kèm nút "Create Tool" [b01, b06, b21, b35].

### Tab Templates — 34 tool do Google hoặc tác giả được Google ghi tên [live, danh mục tool đọc từ DOM ngày 06/09/2026]

| Tool | Tác giả | Mô tả nguyên văn |
|---|---|---|
| Simple Sketch | Google | Turn any drawing into a stylized image |
| Scene Explorer | Google | Explore visuals for scenes based on an initial location |
| Mockup | Google | Comp your image into different environments |
| Image Editor | Google | Transform objects, add text and adjust image sizing |
| Shot Explorer | Google | See your scene from new angles |
| Mask Magic | Arden Schager, Google | Perform selective image edits using segmentation |
| Converge | Chris Maestas | Render your sketches |
| Grid Architect | Henry Daubrez | Create image grids and extract individual images from them |
| Shader Effects | Google | Apply customizable filters to your media |
| Type Overlays | Google | Add animated text to your videos |
| pixelBento | Laszlo Gaal | Apply post-processing effects like lo-fi and glitch |
| Poster Designer | Heysu Oh và Kaloyan Kolev, Google | Create animated posters from your media |
| Video Sketch | Google | Animate drawings on top of your videos |
| Transition Machine | Scotch Johnson, Google | Generate seamless transitions between your videos |
| Weirdcore | Kaloyan Kolev, Google | Fry, chop, melt and distort your videos |
| Video Resizer | Google | Resize your videos into any aspect ratio |
| Stringout Creator | Google | Stitch multiple video clips together |
| Video Granulator | Arden Schager, Google | Play your videos like an instrument |
| Character X-Ray | MetaPuppet | Develop your characters and their backstory |
| Style Writer | Google | Turn your mood board into a style prompt |
| Storyboard Studio | Google | Write a script, create the cast, and visualize a storyboard |
| Prompt Tree | Scotch Johnson, Google | Organize prompts using a branching structure for precise edits |
| Story Sketch | Google | Create storyboards that follow any visual style |
| Frame Deconstructor | Shashwath Santosh và Alan Yam, Google | Deconstruct videos and gifs to create 3D sculptures |
| Blob Tracking | Arden Schager, Google | Generate futuristic tracking effects |
| DepthWarp 4D | Sam Lawton, Google | See your video in a new dimension |
| Webcam Set | Google | Drop yourself into footage |
| Datamosh | Kaloyan Kolev, Google | Add datamoshing effects to your videos |
| 3D Model Visualizer | Filip Havlena, Google | Use a 3D model to guide your image generation |
| Scout360 | PJ Ace | Capture a 360 degree environment from an image |
| Ribbit | Kat Zhang | Perform videos live as the beat drives playback |
| Whisk | Google | Use images as prompts to visualize your ideas |
| Pose Text | Alan Yam, Google | Add text labels that track a character in your video |
| 3D Face Swap | Google | Swap your face with virtual characters |

Ghi chú thêm từ video hướng dẫn: mục Image trong Discover từng liệt kê thêm "Character X-Ray" ngay cạnh nhóm Storyboard Studio, Style Writer, Prompt Tree [b06], và nhóm Image còn hiển thị cùng lúc Simple Sketch, Scene Explorer, Mockup, Image Editor, Shot Explorer, Mask Magic, Converge, Grid Architect, Shader Effects, Type Overlays, pixelBento, Poster Designer, Video Sketch, Transition Machine, Weirdcore, Video Resizer, Stringout Creator, Video Granulator [b23], khớp với bảng Templates ở trên.

### Tab Community — 28 tool do người dùng tự build và chia sẻ [live, danh mục tool đọc từ DOM ngày 06/09/2026]

Đáng chú ý cho làm video:
- **AI Subtitle Generator** (Classic_Ai_Apps): tự động tạo phụ đề từ giọng nói, xuất SRT hoặc burn-in (nhúng cứng) vào video.
- **Character Persona Generator** (MrRobotX): sinh 22 trở lên chân dung nhất quán từ MỘT ảnh tham chiếu duy nhất, nhiều góc chụp khác nhau.
- **LyricFlow** (MAHENDER TOMAR): sinh MV và audio chất lượng cao trực tiếp từ lời bài hát.
- **Screen Script** (Zach M): trình soạn kịch bản định dạng chuẩn màn ảnh, có AI hỗ trợ viết.
- **Director Camera & Path Vector Board** (adcraftai): vẽ quỹ đạo camera bằng brush, có tham số vật lý điều khiển chuyển động.
- **GeoVisualizer** (eteek): nhận diện địa điểm trong media rồi sinh cú máy drone bay vòng quanh địa điểm đó.
- **Background Remover** (Keera): xóa nền ảnh, xuất nền trong suốt.
- **Face Morph** (Nuwan Shilpa Hennayake): đổi biểu cảm khuôn mặt nhân vật.
- **LuzRelighting** (Dany): đánh sáng lại cảnh bằng cách bấm chọn vị trí nguồn sáng mong muốn.
- **Text Effect** (inxstudio): sinh chữ tạo kiểu theo phong cách của media mẫu đính kèm.
- Nhóm truyện tranh/manga: **ComicGen Studio** (Brinsley), **Manga Architect Pro** (Stormy), **B-2 Illustrator** (B2).
- **8-Bit Quest** (Trollceratops): biến video thật thành phong cách game 8-bit điện ảnh.
- Các tool khác cùng danh mục: Vector Sticker Studio (Glenn B), Doodle Logo Architect (Janith Anjana), Brand Carousel Builder (Exterly.io), Fashion Grid Analyzer (Zuhal Mughni), Editorial Jewelry Studio (aditya shukla), Car Showdown (KareemAfterWork), Emote Crafter Pro (Rotti), GridCraft (Queen Usouwa), Lumina Filter Studio (AJEET PAL), Elite Designer Collective (nuraiza siddiq), Bouquet & Note Studio (Maxai), RETRO-TERM 80 (Matthew Wyatt), Mars Blueprint Architect (Sridhar), Void Velocity (Joker).

### Tab My Tools

Chứa hai loại thẻ: các tool cộng đồng đã "Remix" (bấm nút "Remix tool" trên tool bất kỳ để sao chép về của mình rồi tùy biến tiếp) và các tool tự tạo bằng tính năng "Create Tool" (xem mục 4). Trong "My Tools" có phần con "My creations" liệt kê chỉ những tool do chính người dùng dựng, ví dụ một tài khoản có: Nature Documentary Maker, (Gia dụng) Tạo video..., Story Animator, (Gia dụng) Tải ảnh sản phẩm..., Fashion Motion Lab [b21]; một tài khoản khác có Style Portrait, Claymation Studio [b02, b35].

## 2. Tool nào tốn credit, tool nào không

Chắn màn hình mở BẤT KỲ tool nào (kể cả tool do Google làm) đều ghi nguyên văn: **"Google Flow can make mistakes, so double check it. This Tool may consume credits."** (với tool cộng đồng còn thêm "This app was created by another person and may be inaccurate or unsafe. Report unsafe content.") [live, tự đọc chân trang trên DOM ngày 06/09/2026; xác nhận lại ở b21 và b35]. Nghĩa là khẳng định cũ "tool không tốn credit" là **quá rộng và sai một phần**. Phát biểu đúng: Flow chỉ cảnh báo tool CÓ THỂ tốn credit, không cam kết miễn phí tuyệt đối.

Phân biệt theo cơ chế xử lý:

- **Xử lý phía client (đo được: không trừ credit)**: Video Resizer (đo 2 lần, số dư tài khoản không đổi) và Type Overlays (đo 1 lần) [live, số đo Video Resizer ngày 06/09/2026]. Đây là các tool chỉnh sửa hình học/overlay thuần túy, không gọi model sinh ảnh/video mới.
- **Tool gọi model sinh ảnh/video (phải giả định CÓ tốn credit cho đến khi đo được số cụ thể)**: Simple Sketch, Image Editor (khi dùng Refine/Inpaint/Outpaint), Mockup, Converge, Shot Explorer, Mask Magic, Scene Explorer, Whisk, Storyboard Studio (mỗi ảnh/video sinh ra), và mọi tool tự tạo qua Create Tool vì bản chất chúng chỉ là một giao diện gọi lại các model ảnh/video nền của Flow (Nano Banana 2/Pro, Imagen 4, Omni Flash...). Trong khi thao tác thật với Mockup, dòng hiển thị chỉ là cảnh báo chung, không thấy số credit cụ thể bị trừ trên màn hình [b24] — do đó số credit chính xác của từng tool riêng lẻ vẫn [chưa xác minh], chỉ chắc chắn là CÓ khả năng trừ.
- Riêng khi tạo ảnh/video ở màn hình chính của project (ngoài các Tool phụ), Flow luôn hiện dòng "Generating will use N credits" TRƯỚC khi sinh, cho một số ví dụ đo trực tiếp: 0 credit cho lần sinh ảnh bằng Nano Banana Pro [b01, t=209.6s], 15 credit cho video 4 giây bằng Omni Flash [b01, t=312.9s], 13 credit cho video 10 giây Omni Flash chế độ Agent [b16, t=99s]. LƯU Ý: hai con số này LỆCH với bảng đo `[live]` ngày 06/09/2026, nơi Omni 720p 4 giây là 7 credit còn 10 giây là 15 credit. Có thể khung hình không hiện đủ cấu hình thật, hoặc giá đã đổi giữa hai thời điểm. Khi hai bên lệch nhau thì tin bảng đo `[live]`.

Bảng giá credit theo model nằm ở `flow-core.md` mục 2 và ở `SKILL.md`, không nằm trong file này. File này chỉ nói về credit của riêng từng Tool phụ.

## 3. Hướng dẫn chi tiết từng tool đã có thao tác thật trong video

### 3.1 Storyboard Studio

Mở qua Tools > Discover (hoặc Templates) > "Storyboard Studio" (by Google) [b06]. Modal chào "Welcome to Story Studio": chọn "Choose your storyboard style" (dropdown, giá trị mặc định thấy được là "Realistic", có thể đổi sang "Claymation"...), liệt kê 3 bước "1. Workshop your script", "2. Create your cast and locations", "3. Visualize your storyboard", nút "Get Started" [b06, t=61.5s].

Bên trong công cụ có đúng 3 tab: **"1. Script"**, **"2. Assets"**, **"3. Storyboard"**, mỗi tab có dropdown chọn style riêng (ví dụ đổi thành "Claymation" ở cả 3 tab) [b06, t=62.5s].

- Tab Script: khung chat "Ask Gemini" nơi gõ prompt định vai trò đạo diễn (ví dụ: "Tôi muốn bạn đóng vai trò như một đạo diễn phim truyện thật thụ, tôi sẽ đưa cho bạn kịch bản, tôi cần bạn xem, đọc, góp ý và đưa ra chi tiết lời thoại, bối cảnh"). Gemini phân tích kịch bản, trả về Bảng Kịch Bản Giai đoạn 1 với các cột Cảnh, Thời lượng (chuẩn 10 giây/cảnh), Hình ảnh (Visual), Âm thanh (Audio), Voiceover chính xác theo nhân vật. Ràng buộc cứng: **lời bình mỗi cảnh phải dài 25-35 từ** để khớp thời gian đọc thực tế trong tối đa 10 giây [b06, t=7.2s, t=26.7s].
- Tab Assets: khu vực "Characters" có nút "Autofill Characters" mở menu 3 lựa chọn: **Add Character | Autofill descriptions | Autocreate images** [b06, t=71-73s]. Có thể upload cùng lúc nhiều ảnh tham khảo phong cách (một lần upload thấy "10 mục, 10 tài liệu, 7.3 MB") [b06, t=75.4s].
- Tab Storyboard: mỗi Scene hiển thị "Scene 01", tên cảnh (ví dụ "Ext. Rừng Thưa - Ngày"), số khung "6 frames", nút "Autofill Scene", các ảnh được đánh số và đặt tên riêng (ví dụ "01 Sunlight Through the Trees", "02 Elara Gathering Wood"...) [b06, t=79.9-88s]. Tiến trình sinh ảnh hiện dạng "Generating images 8/10" kèm nút "Stop" [b06, live-key-findings cũng xác nhận mẫu tiến trình này].

Nhân vật: màn "New character" có 6 mẫu tính cách dựng sẵn để chọn nhanh: **The Eccentric, The Professional, The Wildcard, The Familiar, The Wicked, The Fantastical** [b06, live]. Chọn giọng qua modal "Select Voice": dropdown loại giọng, ô "Search assets", nút "Preview", "Sample Dialogue" (giới hạn 120 ký tự, đo được "111/120"), "Customize Performance (optional)", "Voice Name", nút "Reset" [b06, t=41.5s].

Cạm bẫy quan sát trực tiếp: nhiều lần phải yêu cầu lặp lại "tạo ảnh storyboard số X nốt nhé" cho từng cảnh một — công cụ không tự sinh hết tất cả các cảnh cùng lúc dù đã có kịch bản đầy đủ [b06, mục 7].

Khi dùng Storyboard Studio nối tiếp bằng Claude điều khiển trình duyệt (workflow tự động hóa của [b16], [b17]): điểm quan trọng nhất là **phải ép chế độ "Image"** khi muốn ra một tấm ảnh storyboard dạng lưới nhiều panel; nếu không kiểm soát chặt, Flow/agent có thể tự hiểu nhầm thành lệnh tạo NHIỀU clip video riêng lẻ theo từng panel (đã xảy ra thật, phải yêu cầu sửa lại) [b16, t=463-501s]. Prompt gửi lên Flow phải là MỘT ĐOẠN LIỀN, tuyệt đối không xuống dòng — xuống dòng sẽ khiến Flow hiểu thành nhiều lệnh riêng và sinh dư ảnh/video [b16; nhắc lại ở b17, cùng một video, nên chưa phải xác nhận độc lập]. Muốn giữ đúng nhân vật giữa các cảnh, luôn gắn ảnh tham chiếu nhân vật (character reference sheet 3 góc: front/3-4/side) vào mỗi prompt bằng nút "+" [b17, t=623-650s].

Prompt hoàn chỉnh mẫu để biến toàn bộ storyboard thành video (đọc được nguyên văn từ tài liệu "Storyboard Image Animation Prompt" dùng kèm công cụ) yêu cầu: giữ nguyên đặc điểm khuôn mặt/tóc/trang phục/tỷ lệ cơ thể xuyên suốt; hoạt họa từng khung như cảnh riêng với chuyển động máy quay điện ảnh nhẹ (lia chậm, quay theo dõi, zoom mềm); chuyển cảnh tự nhiên bằng mờ dần/cắt khớp, tránh cắt đột ngột; lời thoại đúng ngôn ngữ ghi trên storyboard; đồng bộ hiệu ứng âm thanh theo nhịp nội dung; cuối cùng biên tập tất cả cảnh thành một phim ngắn liền mạch [b06, t=38.7-41.4s].

### 3.2 Image Editor

Mở qua Tools; giao diện gồm: panel trái **"Layers (0)"** với hai nút **"+ Add Image"** và **"Add text layer"**; panel phải **"Canvas dimensions"** (Preset "Default", **Width 1344px, Height 768px** mặc định, nút "Reset defaults") và **"AI settings"** (Image Model: **Nano Banana 2**; Background Removal: **"MODNet (People, Fast)"**); thanh công cụ dưới ảnh: **Refine, Inpaint, Outpaint, Cutout, Crop**; nút **"Save to gallery"** [b01, t=635-654s; xác nhận lại kích thước mặc định 1344x768 ở b35, t=326s].

Chèn ảnh có sẵn qua hộp thoại **"Media Grid"**: lọc theo tháng, ô "Search assets", sắp xếp "Recent", 2 tab "Images"/"Uploads", nút "Upload media", danh sách hiển thị tên các ảnh đã tạo trước đó trong project [b01, t=660.8s].

Text layer: chọn font trong danh sách **Google Sans, Inter, Bebas Neue, Montserrat, Playfair Display, Cinzel** (còn có thể cuộn thêm); Size 80px; Weight bold; căn lề Left/Center/Right; Letter spacing 0px [b01, mục 2]. Có tính năng độ sâu (**depth**): toggle "Enable depth", thanh trượt "Depth offset" (đổi được từ -2 lên 34 rồi 12 để test), toggle "Flatten layer depth", nút "Save depth composite" — dùng để tạo hiệu ứng chữ/vật thể có chiều sâu giả lập 3D trên ảnh 2D [b01, t=725.8-744.4s].

Mỗi layer ảnh có thanh trượt riêng: **Opacity, Brightness, Contrast, Saturation, Blur** [b01, t=665.9-680.9s].

Quy trình thực tế đã quan sát: thêm layer ảnh nền (rừng có khủng long) và layer ảnh chân dung người, kéo/resize, dùng **Refine** để hòa trộn hai lớp thành một ảnh liền mạch, sau đó dùng **Inpaint** để chèn thêm dòng chữ tiêu đề đè lên ảnh; layer panel cuối cùng liệt kê Gallery Image, ảnh gốc, Refined Result, Text Layer, Inpaint Result [b35, t=396-453s]. Ghi chú: hai bước Refine và Inpaint tách biệt — Refine dùng để hòa trộn nhiều lớp thành một ảnh cohesion, Inpaint dùng riêng cho thêm/sửa chi tiết cục bộ (như chữ) sau khi đã có ảnh nền.

### 3.3 Mockup

URL dạng `labs.google/fx/tools/flow/project/<id>/tool/<id>` [b24]. Header: mũi tên quay lại, icon áo thun, tên "Mockup", nút **"Remix tool"**, các icon tim/ghim/chia sẻ/cờ, nút **"Done"** [b24, t=687.9s].

Panel trái "Canvas media" chứa ảnh nguồn (đã tải lên hoặc lấy từ project), nút **"Import Image"**. Danh sách **12 loại mockup** dựng sẵn dạng nút bấm: **laptop, phone, tv, shirt, hat, bag, pin, book, poster, window, billboard, mural**, cộng thêm **"+ custom mockup"** để nhập mô tả tự do [live, danh mục tool đọc từ DOM ngày 06/09/2026; xác nhận đầy đủ ở b24, t=699.7s; b35, t=235s]. Có toggle **Fast/Pro** và nút **"RESET SESSION"** ở cuối panel trái [b24, t=699.7s].

"Import Image" mở hộp thoại **Media Grid**: dropdown lọc theo ngày, ô "Search assets", sắp xếp "Recent", 2 tab "Images"/"Uploads", link "Upload media", nút chính "Add Media" [b24, t=697.1s].

Chọn "custom mockup" mở một ô nhập văn bản (placeholder "Describe your mockup...") và nút "CANCEL" [b24, t=782.3s]. Canvas trống ghi chữ mờ "MOCKUP WILL APPEAR HERE", chuyển sang số nhiều "MOCKUPS WILL APPEAR HERE" khi có nhiều biến thể đang sinh [b24, t=699.7-704.4s].

Prompt tùy chỉnh CHẤP NHẬN TIẾNG VIỆT trực tiếp, không cần dịch sang tiếng Anh — ví dụ đã dùng thật: "hiển thị trang web của tôi bên trong chiếc máy tính xách tay nó được đặt trên một chiếc bàn làm việc hiện đại và đảm bảo rằng nó là tâm điểm ở chính giữa của bức ảnh, hướng về phía trước" [b24, t=719.4s]. Kết quả: ảnh laptop bạc trên bàn gỗ, đúng như mô tả, màn hình laptop hiển thị chính xác website nguồn đã tải lên [b24, t=746.2s]. Dưới ảnh kết quả có nhãn rút gọn "✦ custom: <mô tả>...", tag **"FAST"**, và các icon refresh, download (tooltip "Save to gallery"), xóa, mũi tên xổ xuống [b24, t=746.2s].

Không quan sát được số credit cụ thể bị trừ trong lần thao tác này — chỉ có cảnh báo chung "This Tool may consume credits", nên phải xem là tốn credit cho tới khi đo được con số [b24, mục 3].

### 3.4 Converge

Tiêu đề lớn **"CONVERGE"**. Panel trái **"HISTORY STACK"** với nút "CLEAR ALL". Thanh công cụ trên canvas: **Sketch, Annotate, Fill, Dropper**. Panel phải **"AI SETTINGS"** (model mặc định **NANO BANANA PRO**), **"GUIDING PROMPT"** (placeholder "e.g., Refine edges, minimalist style..."), **"RENDER OUTPUT SETTINGS"** gồm **Style** (ví dụ "Macro 3D Studio Rendering") và **Aspect Ratio** ("Auto (Match Input)"), toggle **"CONTEXTUAL BACKGROUND"** (mặc định tắt), nút **"GENERATE RENDER"** [b35, t=629s].

Quy trình BẮT BUỘC hai bước: (1) vẽ phác thảo (sketch) rồi bấm **"Generate Vector Layer"** để chuyển nét vẽ tay thành vector sạch, chọn 1 trong nhiều biến thể vector được đề xuất; (2) chỉ sau đó mới bấm **"Generate Render"** với Style đã chọn để ra ảnh render 3D thực tế. Bỏ qua bước vector sẽ KHÔNG cho ra được bản render 3D [b35, mục 7, t=629-664s].

### 3.5 Video Resizer

Đo trực tiếp bằng ffprobe trên file tải về, mức bằng chứng cao nhất trong toàn bộ tài liệu này [live, số đo Video Resizer ngày 06/09/2026].

Danh sách đầy đủ **Output Ratio** (đọc từ DOM, đúng 6 mục, không hơn): **9:16, 16:9, 1:1, 4:5, 21:9, Custom**.

**Alignment** có 3 giá trị: **FILL** (phóng to cho đầy khung rồi cắt phần thừa, hệ số zoom hiện ngay trên khung), **FIT** (giữ nguyên toàn bộ khung hình, thêm viền đen, hệ số giữ 1.00x), **RESET** (trả về trạng thái ban đầu).

**Custom**: hai ô input number WIDTH và HEIGHT, giá trị mặc định 1080 và 1080, min = 1, max = 4096. Có dòng chữ tính sẵn "Ratio: X:Y (a.aa:1)" nhưng CHỈ cập nhật khi rời ô (blur), không cập nhật real-time khi đang gõ — dễ gây hoang mang tưởng chưa nhận giá trị mới.

**Phát hiện quan trọng nhất, ảnh hưởng trực tiếp tới chất lượng đầu ra**: ở chế độ Custom, người dùng gõ WIDTH và HEIGHT nhưng tool CHỈ LẤY TỈ LỆ giữa hai số, KHÔNG dùng đúng số pixel đã gõ. Ví dụ gõ 1440x1080 (tỉ lệ 4:3) ra kết quả thật 1280x960 — vẫn đúng tỉ lệ 4:3 nhưng không đúng số pixel đã nhập. **Chiều rộng đầu ra LUÔN LUÔN là 1280**, chiều cao = 1280 chia cho tỉ lệ đã chọn, bất kể nguồn đầu vào là 640px hay 1280px chiều rộng (đã loại trừ giả thuyết "gấp đôi nguồn" bằng phép thử độc lập: nạp nguồn 1280x1280 đổi sang 16:9 vẫn ra 1280x720 chứ không phải 2560x1440). Điểm CHƯA XÁC MINH: chưa thử nguồn rộng 1920px; nếu quy luật này giữ nguyên thì đưa clip 1080p vào Video Resizer sẽ bị HẠ XUỐNG 1280px chiều rộng, tức là MẤT độ phân giải — nên đo lại file đầu ra trước khi resize clip 1080p.

**Cạm bẫy đặt tên asset đã xác nhận**: tên file trong gallery ghi kích thước DANH NGHĨA (những gì người dùng gõ), không phải kích thước THẬT của file kết quả. Ví dụ đo bằng ffprobe:

| Tên asset trong gallery | Kích thước THẬT (ffprobe) |
|---|---|
| Resized_1440x1080_... | 1280 x 960 |
| Resized_2560x1080_... | 1280 x 540 |
| Resized_1080x1080_... | 1280 x 1280 |
| Resized_1080x1350_... | 1280 x 1600 |

Chỉ có TỈ LỆ là khớp giữa tên và file thật, số pixel trong tên luôn sai — phải tự ffprobe file thật mới biết chính xác.

Tool vừa đổi tỉ lệ vừa **UPSCALE** (640→1280 nếu nguồn nhỏ hơn 1280). Giữ nguyên 24fps, giữ nguyên audio AAC 48kHz stereo, giữ đúng thời lượng gốc.

Thao tác khác: sau khi nạp media, panel hiện "Replace Source" để đổi nguồn mà không cần làm lại từ đầu. Trình chọn media có thanh cắt đoạn (2 tay nắm đầu/cuối) và ô hiện thời điểm hiện tại, nghĩa là có thể cắt bớt clip trước khi đưa vào tool; có bộ lọc "Videos"/"Uploads", ô "Search assets", sắp xếp "Recent", nút "Upload media".

Xuất file: kết quả ghi NGƯỢC vào gallery của project, KHÔNG tự tải về máy. Muốn lấy file thật phải bắt URL ký tên dạng `flow-content.google/video/<id>?Expires=&KeyName=&Signature=` rồi curl. Cùng một `<id>` phục vụ cả `/image/<id>` (ảnh thumbnail) lẫn `/video/<id>` (file thật) nhưng chữ ký Signature khác nhau nên không dùng lại được giữa hai loại.

Đã đo được: **KHÔNG trừ credit** cho 2 lần chạy — tool xử lý phía client.

### 3.6 Shot Explorer

Panel trái **"SELECT IMAGE"**. Ba nhóm nút điều khiển góc máy: **"Perspective"** (overhead, side, back), **"Pan"** (left, right, up, down), **"Zoom"** (zoom in, zoom out, extreme detail, surprise me). Có nút **"RESET"** và toggle **Fast/Pro** [b35, t=601s].

Kết quả bên phải gắn nhãn đúng tên góc vừa bấm (side, back, zoom in...), kèm nút **EXPLORE**, refresh, download, delete. Quy trình: chọn một ảnh chân dung có sẵn trong project, mỗi lần bấm một nút Perspective/Pan/Zoom sẽ tạo ra một biến thể ảnh mới đúng góc máy đó, không cần viết prompt.

### 3.7 Simple Sketch

Khung vẽ tay bên trái, công cụ vẽ: mũi tên chọn, bút chì, hình vuông, hình tròn, chữ T (text), bảng màu, 2 cỡ nét, Undo/Redo, icon upload ảnh, icon xóa. Ô nhập prompt bên dưới + nút gửi; ảnh kết quả hiện bên phải kèm nhãn "FAST" [b01, t=603.4-618.4s; xác nhận lại nguyên vẹn ở b35, t=139-220s với nhãn "DRAW HERE" / "Images will appear here"].

Có thể vừa vẽ vừa viết prompt tiếng Việt trực tiếp, ví dụ: "một con quái vật màu xanh lá cây trong rừng rậm, hình ảnh thực tế, mang tính điện ảnh, sự kết hợp giữa khủng long và sinh vật quái vật, nhưng có nét dễ thương, ảnh chụp thật" [b35, t=169s]. Có thể tinh chỉnh thêm bằng cách khoanh vùng đỏ trên ảnh kết quả rồi nhập mô tả bổ sung (ví dụ thêm "...sinh vật này có các đốm màu đỏ") [b35, t=235s]. Panel dưới prompt còn có "Additional Instructions" (thu gọn) và toggle **FAST/PRO** [b01].

### 3.8 Style Portrait, Story Animator, Outfit & Env Switcher, Fashion Motion Lab

Xem mục 4 (đây là các ví dụ thật của tính năng Create Tool).

### 3.9 Các tool có tên trong yêu cầu nhưng CHƯA có thao tác thật ghi lại được trong nguồn đã xem

- **Scene Explorer**: chỉ xuất hiện trong danh mục Templates, chưa có video nào ghi lại thao tác chi tiết bên trong. [chưa xác minh]
- **Mask Magic**: chỉ có mô tả catalog "Perform selective image edits using segmentation" (Arden Schager, Google), chưa có frame thao tác thật. [chưa xác minh]
- **Grid Architect**: chỉ có mô tả catalog "Create image grids and extract individual images from them" (Henry Daubrez), chưa có frame thao tác thật. [chưa xác minh]
- **Whisk**: chỉ có mô tả catalog "Use images as prompts to visualize your ideas" (Google), chưa có frame thao tác thật. [chưa xác minh]
- **Style Writer**: chỉ có mô tả catalog "Turn your mood board into a style prompt" (Google), chưa có frame thao tác thật. [chưa xác minh]
- **Type Overlays**: chỉ xác nhận được là KHÔNG tốn credit (đo 1 lần) [live], chưa có frame mô tả giao diện chi tiết bên trong.

## 4. Tính năng "Create Tool" — tự tạo công cụ bằng ngôn ngữ tự nhiên

### Cách vào và luồng cơ bản

Vào từ Tools > Explore Tools > nút **"Create Tool"**, hoặc từ tab **"My Tools" > "Create New"**. Trang khởi tạo luôn ghi: *"Start building any creative tool you can dream by describing it below."* kèm 3 gợi ý mẫu đổi theo phiên bản (ví dụ đã thấy: "Image Filter, Time Stretcher, Voice Over" [b01]; "Style Morph, Image Filter, Voice Over" [b35]) [b01, t=749-770.6s; b35, t=664s].

Người dùng mô tả tool mong muốn bằng tiếng Việt tự nhiên trong một ô nhập lớn. Sau khi gửi, Flow **tự sinh ra một công cụ hoàn chỉnh** với: model mặc định (thường là Nano Banana Pro), tỉ lệ khung hình mặc định (ví dụ 1:1), một prompt phong cách mặc định do AI tự viết, và giải thích các lựa chọn đó bằng chat.

Giao diện tool vừa tạo: 2 tab trên cùng **"Tool"** / **"Edit"**; bên trong Tool có 2 tab con **"Preview"** / **"Code"**; panel phải cố định tên **"Tool Builder"** — đây chính là khung chat để tiếp tục chỉnh sửa tool bằng ngôn ngữ tự nhiên [b01, t=772.7-811.6s; b02, t=826.6s].

### Ví dụ thật 1 — Claymation Studio (biến ảnh bất kỳ thành phong cách claymation)

Prompt gốc của người dùng: *"Này, tôi muốn bạn xây dựng một công cụ cho phép tôi tải lên bất kỳ hình ảnh nào, và công cụ đó sẽ tự động chuyển nó sang phong cách hoạt hình đất sét"* [b01, t=772.7s].

Kết quả: Tool Builder tự đặt tên **"Claymation Studio"**, giải thích trong chat: dùng model 🍌 **Nano Banana Pro** làm mặc định "vì khả năng hiểu phong cách nghệ thuật rất tốt", gợi ý thử **Imagen 4** nếu muốn chi tiết cao hơn; tỉ lệ khung hình mặc định **1:1**; tự viết sẵn prompt phong cách trong ô "Mô tả phong cách" (style description): *"Chuyển đổi hình ảnh này sang phong cách hoạt hình claymation, chi tiết thủ công, kết cấu đất sét plasticine, ánh sáng studio stop-motion."* [b02, t=826.6-852.9s].

Giao diện Claymation Studio: khung "Đầu vào" (upload/chọn ảnh qua Media Grid), ô "Mô tả phong cách", nút "Chuyển sang Đất sét" (kèm icon lấp lánh, mờ đi khi chưa có ảnh), khung kết quả lớn ở giữa với nút "Tải xuống". Model AI dropdown ("🍌 Nano Banana Pro"), dropdown tỉ lệ khung hình ("1:1") [b02, t=826.6-843.4s].

### Ví dụ thật 2 — Story Animator (kịch bản tóm tắt → phim hoạt hình nhiều cảnh)

Giao diện 3 cột: cột trái "1. KỊCH BẢN & LỜI BÌNH" (2 ô nhập) và "2. THIẾT LẬP NHÂN VẬT" (dropdown **Phong cách**: Điện ảnh, Tả thực, Anime, Hoạt hình 3D, Tranh sơn dầu, Màu nước; nút chọn khung **Ngang/Dọc**; ô thêm tối đa 2 ảnh nhân vật), nút **"Phân tích & Tạo Phim"**; cột giữa là khu xem trước; cột phải vẫn là "Tool Builder" [b21, t=849s].

Quy trình thật: nhập kịch bản tóm tắt (ví dụ "Hai bé cún nấu trứng rán hành"), chọn phong cách Anime, tải 2 ảnh nhân vật, bấm "Phân tích & Tạo Phim" → công cụ TỰ CHIA kịch bản thành **tối đa 6 cảnh**, mỗi cảnh có mô tả hình ảnh chi tiết do AI tự viết (ví dụ Cảnh 1: "Cận cảnh hai chú cún con... mặc tạp dề đứng bếp nhỏ màu xanh và đỏ trong căn bếp gỗ"), rồi bấm **"Bắt đầu quay"** riêng cho từng cảnh để lần lượt tạo video 8 giây/cảnh. Tiến độ hiển thị dạng "x/6 cảnh hoàn tất" [b21, t=1026-1078s].

Lưu ý kỹ thuật ghi lại trong chính Tool Builder: nếu chỉ 1-2 ảnh nhân vật tham chiếu, khi tạo video cho một cảnh có thể CHỌN nhân vật nào phù hợp để AI giữ ngoại hình cho cảnh đó. Cấu trúc kịch bản khuyến nghị: tiêu đề "[Cảnh X]: [Tiêu đề cảnh]" gồm Bối cảnh (địa điểm, thời gian, ánh sáng), Hành động (nhân vật làm gì, cảm xúc), Ghi chú (góc máy nếu muốn).

### Ví dụ thật 3 — Style Portrait (3 phong cách chân dung từ 1 ảnh)

Prompt gốc: *"tôi muốn một ứng dụng cho phép tôi tải lên hình ảnh một người, và nó sẽ trả về cho tôi 3 bức chân dung khác nhau của người đó theo các phong cách khác nhau, 1. là phong cách hoạt hình dễ thương render 3d... pixar 2. là một bức chân dung biếm họa phóng đại... 3. tôi muốn một bức vẽ nét sạch để làm sách tô màu... tất cả đều phải giữ được nét đặc trưng/nhận dạng của người đó"* [b35, t=664s].

Kết quả: panel trái "ẢNH GỐC" (chọn ảnh chân dung), "PHONG CÁCH MỤC TIÊU" liệt kê 3 style: **Pixar Style, Biếm họa (Chi màu), Sách tô màu (Line art)**, nút lớn **"Bắt đầu chuyển đổi"**. Kết quả trả về 3 ảnh dưới tiêu đề "Kết quả chân dung", nút "Tải về tất cả" [b35, t=750-759s]. Có thể chỉnh sửa icon app riêng qua dialog "Edit Icon" (lưới icon hình khối bo tròn nhiều màu). Code sinh ra xem được ở tab Code, dùng React/TSX với thư viện nội bộ "flow-sdk" [b35, t=759s].

Chỉnh sửa lặp qua Tool Builder bằng các lượt chat nhỏ liên tiếp thay vì một prompt lớn: ví dụ thêm tính năng "khi nhấp vào ảnh đã tạo thì thấy to hơn, dễ so sánh với ảnh gốc" [b35, t=759s], sau đó đổi style "Biếm họa" từ nét bút chì sang biếm họa nhiều màu [b35, t=886-919s]. Đây là mẫu hình sử dụng chính của Tool Builder: lặp dần (iterative), không phải một lệnh hoàn chỉnh ngay từ đầu.

### Ví dụ thật 4 — Outfit & Env Switcher (đổi trang phục/bối cảnh hàng loạt, giữ nhân vật)

Tool này bị đổi tên nhiều lần qua các lượt chat: **Outfit Change → Outfit Persona → Outfit & Env Switcher** [b35, t=986s trở đi]. Prompt chỉnh sửa tiếng Anh gửi cho Tool Builder (trích, có phần bị cắt do cuộn khung chat): *"Change the app name to 'Outfit & Env Switcher'. Update the layout to precisely match the structure in image_4c73f9.jpg but translate all UI text to Vietnamese. Key structural changes required: 1. Aspect Ratio Sync: Force the system to automatically detect the aspect ratio of the 'Identity Source' image... and enforce that exact same aspect ratio onto all generated variations... 2. Left Sidebar (Cấu hình AI): Rename... Add an 'Aspect Ratio'..."* [b35, t=986s].

Giao diện cuối cùng "THIẾT KẾ BIẾN THỂ": 3 cột **OPTION 1/2/3**, mỗi cột có ô nhập **Outfit (Trang phục)**, **Environment (Bối cảnh)**, nút **RANDOM** riêng từng cột, nút **"TAO BIEN THE"** (Tạo biến thể) riêng từng cột, và nút lớn **"BATCH GENERATE ALL"** ở cuối để sinh đồng loạt cả 3. Thêm thanh trượt **"Độ tương đồng khuôn mặt"** đặt 90%. Aspect Ratio có 4 nút: **9:16, 3:4, 1:1, 16:9**. Mỗi ảnh kết quả có 2 nút riêng: **DOWNLOAD** và nút xóa (icon thùng rác đỏ) [b35, t=986-1034s].

Prompt yêu cầu bổ sung tính năng khác: *"Make sure the pose is consistent, all is identical except the clothes and environment. Also, add a randomize button for the prompts if I want more ideas. Furthermore, please add a 'Download' button and a 'Delete' button directly under each generated image."* [b35, t=1009s] — cho thấy có thể yêu cầu Tool Builder thêm từng nút UI cụ thể bằng lời, không cần biết code.

Khi bấm nút Random, các ô outfit/environment/lighting tự đổi sang gợi ý ngẫu nhiên bằng tiếng Việt (ví dụ "Trang phục cyberpunk neon" / "Khu vườn bí mật phong cách Zen" / "Ánh đèn neon xanh đỏ") [b35, t=1034s].

### Ví dụ thật 5 — Fashion Motion Lab

Tải ảnh người mẫu + ảnh trang phục vào 2 ô riêng biệt, sau đó tool tự tạo ra bộ ảnh với 8 góc chụp/tư thế khác nhau của người mẫu đang mặc đúng trang phục đó, giữ nhất quán trang phục qua các góc [b21, t=1250s].

### Nguyên tắc chung rút ra từ 5 ví dụ trên

1. Mô tả ban đầu càng cụ thể (số lượng đầu ra, tên style, ràng buộc giữ nguyên đặc điểm nhận dạng) thì Tool Builder tạo ra tool sát ý hơn ngay từ đầu.
2. Chỉnh sửa nên đi qua nhiều lượt chat nhỏ (đổi tên, thêm nút, đổi bố cục, đổi phong cách) thay vì cố nhồi hết vào một prompt.
3. Tool Builder có thể tự quyết định model và tỉ lệ khung hình mặc định; người dùng luôn có thể yêu cầu đổi lại bằng lời.
4. Kết quả sinh ra là code thật (React/TSX, dùng "flow-sdk"), xem được ở tab Code, không phải hộp đen.
5. Mọi tool tự tạo đều mang cảnh báo cố định ở cuối trang về khả năng tốn credit và về việc tool có thể sai/không an toàn nếu là tool remix từ người khác.

## 5. Tool cộng đồng đáng chú ý cho làm video (kèm tên tác giả)

Xem danh sách đầy đủ ở Mục 1 (Tab Community). Tóm tắt lại các tool trực tiếp phục vụ sản xuất video:

| Tool | Tác giả | Công dụng cho video |
|---|---|---|
| AI Subtitle Generator | Classic_Ai_Apps | Tự động tạo phụ đề từ giọng nói, xuất SRT hoặc nhúng cứng vào video |
| Character Persona Generator | MrRobotX | Sinh 22+ chân dung nhất quán từ 1 ảnh, dùng làm reference nhân vật đa góc cho video |
| LyricFlow | MAHENDER TOMAR | Sinh MV kèm audio chất lượng cao trực tiếp từ lời bài hát |
| Screen Script | Zach M | Soạn kịch bản định dạng chuẩn phim, có AI hỗ trợ |
| Director Camera & Path Vector Board | adcraftai | Vẽ quỹ đạo camera bằng brush, có tham số vật lý |
| GeoVisualizer | eteek | Nhận diện địa điểm trong media, sinh cú máy drone bay vòng quanh |
| Face Morph | Nuwan Shilpa Hennayake | Đổi biểu cảm khuôn mặt nhân vật giữa các khung hình |
| LuzRelighting | Dany | Đánh sáng lại cảnh bằng cách bấm chọn vị trí nguồn sáng |
| 8-Bit Quest | Trollceratops | Biến video thật thành phong cách game 8-bit điện ảnh |
| ComicGen Studio / Manga Architect Pro / B-2 Illustrator | Brinsley / Stormy / B2 | Chuyển cảnh quay hoặc ảnh thành truyện tranh/manga (dùng làm storyboard phong cách truyện tranh) |

## 6. Bảng "cần làm việc X thì dùng tool nào"

| Việc cần làm | Tool nên dùng |
|---|---|
| Biến nét vẽ tay thành ảnh render đẹp | Simple Sketch |
| Ghép ảnh vào bối cảnh có sẵn (laptop, áo, poster, billboard...) | Mockup |
| Chỉnh sửa ảnh nhiều lớp: thêm layer, chữ có chiều sâu, xóa nền, inpaint/outpaint | Image Editor |
| Xem lại một cảnh từ góc máy khác (trên cao, bên hông, zoom cực cận) mà không viết prompt | Shot Explorer |
| Chỉnh sửa vùng chọn cụ thể trên ảnh bằng phân vùng (segmentation) | Mask Magic |
| Vẽ phác thảo rồi render thành vật thể 3D studio-quality | Converge |
| Ghép nhiều ảnh thành lưới, hoặc tách 1 lưới ảnh thành từng ảnh riêng | Grid Architect |
| Dùng ảnh làm "prompt" trực quan để hình dung ý tưởng | Whisk |
| Rút phong cách từ một mood board thành prompt văn bản dùng lại được | Style Writer |
| Viết kịch bản, dựng dàn nhân vật, và vẽ storyboard nhiều cảnh cho một câu chuyện | Storyboard Studio |
| Đổi tỉ lệ khung hình video (dọc/ngang/vuông) không tốn credit | Video Resizer |
| Thêm chữ động (animated text) lên video không tốn credit | Type Overlays |
| Tạo phụ đề tự động từ giọng nói và xuất SRT | AI Subtitle Generator (Community, Classic_Ai_Apps) |
| Cần 20+ chân dung nhất quán của cùng một nhân vật từ 1 ảnh gốc | Character Persona Generator (Community, MrRobotX) |
| Sinh MV kèm nhạc trực tiếp từ lời bài hát | LyricFlow (Community, MAHENDER TOMAR) |
| Vẽ quỹ đạo di chuyển camera bằng tay, có vật lý | Director Camera & Path Vector Board (Community, adcraftai) |
| Có ý tưởng riêng, chưa có tool nào làm đúng ý (ví dụ: 3 phong cách chân dung cùng lúc, đổi trang phục/bối cảnh hàng loạt, phim hoạt hình nhiều cảnh từ kịch bản tóm tắt) | Create Tool (tự mô tả bằng tiếng Việt, dùng Tool Builder chỉnh sửa dần) |

## 7. Community Tools Market và Tools Community Gallery — ai tạo được, ai remix được

Trang chính thức duy nhất tìm được nói về việc tạo và quản lý Tool là "Create & manage Tools in Google Flow" (`https://support.google.com/flow/answer/17104535`, đọc 08/09/2026) [doc]. Trang này xác nhận:
- Có tồn tại **hạn ngạch (quota) hàng ngày** cho số Tool được tạo, nhưng không ghi con số cụ thể.
- Có thể **"share Tools publicly"** (chia sẻ Tool công khai), nguyên văn.
- KHÔNG dùng tên gọi "Community Tools Market" hay "Tools Community Gallery" ở bất kỳ đâu trên trang, và KHÔNG nói rõ việc tạo/remix Tool có bị giới hạn theo gói tài khoản (miễn phí hay trả phí) hay không.

Theo nguồn bên thứ ba (MindStudio, bài tổng hợp về Flow Tools, đọc 08/09/2026): mọi người dùng Flow, kể cả tài khoản miễn phí, đều **DÙNG** được Tool có sẵn trong thư viện cộng đồng; nhưng chỉ tài khoản trả phí (Google AI Plus, Pro, hoặc Ultra) mới **BUILD** (tạo Tool mới bằng Create Tool), **REMIX** (sao chép Tool người khác về sửa lại) và **SHARE** (phân phối Tool mình tạo) được [chưa xác minh, nguồn: mindstudio.ai/blog/what-is-google-flow-tools-custom-ai-workflows-no-code, đọc 08/09/2026]. Đây là khẳng định của MỘT nguồn thứ ba, KHÔNG có trang chính thức nào của Google xác nhận hay phủ định lại, nên chỉ dùng làm giả thuyết làm việc, không dùng làm căn cứ chắc chắn khi tư vấn cho người dùng.

Danh mục tool cụ thể trong tab "Community" đã liệt kê ở Mục 1 của file này vẫn giữ nguyên giá trị — đó là quan sát `[live]` trực tiếp trên DOM ngày 06/09/2026, độc lập với hai nguồn vừa nêu ở trên.

**Xác nhận thêm bằng phép đo `[live 08/09/2026]` khác, mở trực tiếp UI bằng Playwright trên tài khoản Pro**: tên gọi đúng của khu vực này là **"Tools from creators like you"** (heading thật trong tab Community), mô tả nguyên văn "Explore tools curated from the Google Flow Community. Try them out, get inspired, and create your own!", danh sách chia theo ba nhóm **Image, Video, Experimental**. Tab **"My Tools"** có heading **"Submit your tool to be featured"** kèm nút **"Create New"**, và chia hai mục con **"My creations"** và **"Tools shared with me"**. Phép đo này còn xác nhận thêm hai điểm: **chỉ gói trả phí mới tạo được tool** (khớp với giả thuyết của nguồn MindStudio ở trên, nay đã có `[live]` củng cố thêm chứ không chỉ dựa một nguồn thứ ba nữa), và **Flow Tools chỉ có trên bản web**, không có trên app di động.

## 8. Custom Prompt Expanders [chưa xác minh]

Đã tìm nhưng CHƯA thấy trang hỗ trợ chính thức nào của Flow nhắc tên "Custom Prompt Expanders" hay "Prompt Expander". Mọi mô tả dưới đây đến từ báo công nghệ bên thứ ba, gắn `[chưa xác minh]`, không phải "tính năng không tồn tại" — chỉ là chưa tự đọc được nguồn chính thức:

- Biến một câu lệnh ngắn thành một prompt đầy đủ chi tiết hơn ("convert a short instruction into a richer, fully formed prompt"), có sẵn nhiều preset dựng sẵn như **Action Figure, Film Noir, Cinematic**, và cho phép tạo kiểu mở rộng (custom expansion style) riêng [chưa xác minh, testingcatalog.com/google-flow-adds-nano-banana-editing-and-prompt-expander, bài đăng 28/09/2025].
- Một Expander đã áp dụng sẽ tác động đồng thời lên cả ba model nền của Flow: cách Veo 3 sinh video, cách Imagen 4 sinh ảnh minh hoạ, và cách Gemini xử lý prompt ngôn ngữ tự nhiên [chưa xác minh, vp-land.com/p/google-flow-s-custom-expander-feature-brings-consistency-to-ai-video-production, đọc 08/09/2026].
- Công dụng chính theo cả hai nguồn: giữ nhất quán phong cách hình ảnh qua nhiều clip trong cùng một dự án.

Hai nguồn trên độc lập với nhau và mô tả khớp nhau về cơ chế (ngắn thành dài, có preset, ảnh hưởng nhiều model), nên đáng tin hơn một nguồn đơn lẻ, nhưng vẫn CHƯA đạt mức `[doc]` vì chưa tự đọc được trang chính thức của Google.

## 9. Doodle, Object Removal, Camera Adjustment — tinh chỉnh video sau khi đã sinh

Nguồn: `blog.google/innovation-and-ai/models-and-research/google-labs/flow-refine-videos/`, đọc 08/09/2026 [doc], cộng nội dung hộp thoại changelog thật đọc trực tiếp trên tài khoản Pro ngày 08/09/2026 [changelog], ghi rõ riêng theo từng mục.

- **Doodle**: người dùng vẽ hoặc chú thích (annotate) trực tiếp lên một khung hình; Flow đọc hiểu nét vẽ tay và đưa ý đó vào khung hình cuối cùng, nguyên văn "Flow understands your doodles and incorporates them into your final frame." Dùng để chỉ đạo sáng tạo mà không cần gõ hết bằng chữ.
  - **Đường thao tác thật, theo changelog ngày 21/10/2025 [changelog]**: bấm icon edit trên một ảnh để vẽ chú thích lên ảnh đó. Dùng tốt kết hợp với **Nano Banana** và với chế độ **Doodle to Video**.
- **Object removal / insertion (thêm và xoá vật thể)**: cho phép "insert objects directly into videos or remove elements, without changing anything else." Blog ghi rõ tính năng xoá vật thể (object removal) là **thử nghiệm (experimental)**, đang rollout dần; blog không ghi ngày rollout hoàn tất tính tới lúc đọc 08/09/2026.
  - **Đường thao tác thật, theo changelog ngày 02/12/2025 [changelog]**: bấm icon bút chì trên video, chọn **Remove**, vẽ mask quanh vật thể cần xoá, có thể thêm prompt tuỳ chọn kiểu `remove the hat`, rồi bấm icon mũi tên để sinh. Hoạt động tốt nhất khi vật thể ít di chuyển trong khung hình.
  - **Chi tiết quan trọng cần nhớ khi chọn model hoặc viết prompt**: theo hướng dẫn prompt chính thức của Google Cloud (nguồn `cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1`, đọc 08/09/2026), chức năng thêm/xoá vật thể chạy trên nền **Veo 2** và **KHÔNG có âm thanh**, nguyên văn `Add/remove object (uses Veo 2, no audio)`. Nghĩa là dùng tính năng này sẽ MẤT toàn bộ âm thanh gốc của video, kể cả khi video gốc do Veo 3.1 sinh vốn có âm thanh kèm sẵn.
- **Camera adjustment (điều chỉnh camera)**: cho phép "adjust the camera position, orbit, or move the 'dolly' in any of your generated videos." Hoạt động tốt nhất trên các clip CHƯA có sẵn chuyển động camera từ trước (video gốc quay tĩnh).
  - **Đổi hạng tài khoản, theo changelog ngày 02/12/2025 [changelog]**: tính năng này TRƯỚC ĐÂY chỉ dành cho gói Ultra, nay đã **mở cho mọi hạng tài khoản**. Đừng dùng thông tin cũ "chỉ Ultra" cho tính năng này nữa.
- **Model nền cho ảnh dùng trong các thao tác tinh chỉnh này**: sinh ảnh dùng Imagen và Nano Banana cho người dùng miễn phí; Nano Banana Pro dành cho người trả phí, có thêm điều khiển cấp chuyên nghiệp như depth of focus, lighting, và color grading.

Blog không nói rõ Doodle và Camera adjustment có tốn credit hay không, và không nói backend model riêng cho hai tính năng này (chỉ nói rõ backend của object removal/insertion là Veo 2).

## 10. Maps Imagery Grounding — đang Private Preview, KHÔNG phải lỗi thiếu tính năng

Nguồn: `mapsplatform.google.com/maps-products/grounding/`, đọc 08/09/2026 [doc].

Tính năng cho phép chèn chủ thể do AI sinh vào bối cảnh địa lý có thật, dùng dữ liệu không gian địa lý của Google để giữ đúng thực tế, nguyên văn cho phép "seamlessly insert" chủ thể vào bối cảnh thật. Nguồn ảnh nền là **Street View**.

Tính năng hiện đang ở **Private Preview** — phải nộp đơn xin quyền truy cập qua form riêng, KHÔNG mở đại trà cho mọi tài khoản bất kể trả phí hay không. Trang không ghi rõ vùng khởi đầu cụ thể; theo mô tả tổng thể và đối chiếu với `mapsplatform.google.com/resources/blog/three-new-ways-to-build-with-real-world-imagery-and-ai/`, điểm khởi đầu là địa điểm tại Mỹ qua Street View.

**Điểm quan trọng cần nhớ**: trang này không hề nhắc tới Google Flow — Maps Imagery Grounding vận hành trong hệ sinh thái Gemini Enterprise Agent Platform, tách biệt khỏi Flow. Vì vậy **việc tài khoản Flow (kể cả gói Pro) không nhìn thấy tính năng này là ĐÚNG THIẾT KẾ, không phải lỗi thiếu tính năng hay lỗi tài khoản** — tính năng chưa từng được tích hợp đại trà vào Flow, và đang giới hạn ở diện xin duyệt trước cho một sản phẩm/API khác của Google. Không nên kết luận "Flow không có Maps Imagery Grounding" theo nghĩa phủ định vĩnh viễn; đúng hơn là "tính năng này chưa mở, và đang thuộc một preview riêng ngoài Flow" — lần sau gặp lại câu hỏi này thì tra cứu đúng chỗ (Maps Platform, không phải Flow support) trước khi kết luận.

## 11. Phím tắt, Archive, và Starter Projects — ba tính năng chỉ có tên trong changelog

Ba mục này từng chỉ xuất hiện đúng một lần trong toàn skill, ở dòng tiêu đề bảng changelog, không được giải thích ở đâu khác. Nay đã tìm thêm được bằng chứng, ghi rõ mức độ.

### Phím tắt (Keyboard Shortcuts)

Danh sách dưới đây đọc trực tiếp từ hộp thoại changelog ngày 29/04/2026 trên tài khoản Pro [changelog 08/09/2026]: Copy, Paste, Delete; phím mũi tên để di chuyển phần tử; Escape để thoát menu hoặc bỏ chọn; phím cộng và trừ để đổi cỡ ô lưới; phím `/` để nhảy tới thanh tìm kiếm.

Cùng ngày 08/09/2026, một phép đo khác đã tự fetch trang hỗ trợ chính thức `support.google.com/flow/answer/17069754` [doc] và đọc được bảng phím tắt Windows đầy đủ hơn nhiều (xem lại tại đây để không lặp): Del/Backspace xoá, `@` mở menu (+), Space xem trước, mũi tên trái/phải chuyển asset, mũi tên lên/xuống chuyển version, Ctrl+D tải xuống, Esc đóng chế độ sửa, Ctrl+C/Ctrl+V copy/paste, `u` hoặc Esc quay lại lưới, Enter vào chế độ sửa, Ctrl+G nhóm asset, `=`/`-`/`0` đổi cỡ lưới, Shift+G chuyển view, Shift+I lọc ảnh, Shift+V lọc video, Shift+U lọc upload, Ctrl+U tải lên, Ctrl+F focus tìm kiếm, Shift+mũi tên trái/phải chuyển khung hình video, `/` mở tìm kiếm. Trang này KHÔNG có bảng phím tắt Mac chi tiết, chỉ báo có tab riêng cho nền tảng khác mà nội dung không lấy được qua lần fetch này.

Về việc tìm bảng phím tắt NGAY TRONG giao diện Flow: agent đã tự tìm nhưng **chưa thấy** bảng phím tắt nào hiện ngay trên UI, và **chưa bấm thử nút "Product help"** để kiểm tra tiếp. Viết đúng hiện trạng: "chưa tìm thấy sau khi đã thử tìm trực tiếp trên UI", KHÔNG kết luận "Flow không có bảng phím tắt trong giao diện" — đường "Product help" còn chưa thử.

### Archive

Theo changelog ngày 29/04/2026 [changelog 08/09/2026]: chuột phải lên một mục media bất kỳ để chuyển nó vào thư mục archive của project; truy cập archive ở góc dưới bên trái màn hình.

Đối chiếu với quan sát `[live 08/09/2026]` trên sidebar một project thật: sidebar HIỆN TẠI không có mục nào tên "Archive" — sidebar chỉ có **All media, Images, Videos, Characters, Scenes, Uploads, Tools, Trash**. Ghi cả hai dữ kiện, không xoá vế nào: đường thao tác thật lấy từ changelog (chuột phải để archive, truy cập ở góc dưới trái) và việc sidebar project thật đang mở KHÔNG thấy mục "Archive" theo tên đó — có thể chức năng vẫn tồn tại dưới một lối vào khác (ví dụ ẩn trong menu chuột phải, chưa thử trực tiếp) chứ chưa đủ căn cứ để nói tính năng đã bị gỡ.

### Starter Projects [chưa xác minh đầy đủ]

Changelog ngày 21/08/2025 nói trên trang chủ Flow có nút "Add Starter Projects" [changelog]. Trên tài khoản đã có sẵn project (tài khoản Pro đang dùng để kiểm chứng), **KHÔNG thấy** nút này trên trang chủ [live 08/09/2026]. Giả thuyết hợp lý: nút chỉ hiện với tài khoản còn trống (chưa có project nào), nhưng giả thuyết này **CHƯA được thử** trên một tài khoản trống thật. Viết đúng hiện trạng: "không tìm thấy trên tài khoản đã có project, chưa thử với tài khoản trống" — không kết luận tính năng đã bị gỡ bỏ.

## 12. Ghi chú về nguồn và mức tin cậy

- Toàn bộ Mục 1 (danh mục ba tab) và Mục 3.5 (Video Resizer) dựa trên `[live]`, tức tự mở Flow đọc DOM và tự đo bằng `ffprobe` ngày 06/09/2026, mức bằng chứng cao nhất trong tài liệu này.
- Mục 3 và Mục 4 dựa trên nhiều video hướng dẫn độc lập (kênh "Non-tech làm AI" và các kênh khác), mỗi chi tiết đều kèm mã batch [bXX] và mốc giây gốc trong file để tiện tra lại nếu cần đối chiếu.
- Những tool không có bằng chứng thao tác thật (Scene Explorer, Mask Magic, Grid Architect, Whisk, Style Writer, Type Overlays) được gắn rõ [chưa xác minh] ở phần mô tả chi tiết; chỉ tên gọi và mô tả một dòng của chúng là chắc chắn (lấy từ catalog chính thức [live]).
- Giao diện Flow thay đổi khá nhanh (ví dụ tên tab Discover/Templates khác nhau giữa các video quay ở thời điểm khác nhau, số lượng model video từ 4 lên 5 mục tùy hạng tài khoản) — khi áp dụng tài liệu này, nên đối chiếu lại với giao diện thật tại thời điểm sử dụng, đặc biệt là số credit chính xác của từng Tool phụ vì phần này chưa đo được trực tiếp cho đa số tool ngoài Video Resizer và Type Overlays.
- Mục 7, 9, 10 đọc trực tiếp từ tài liệu chính thức (`[doc]`) hoặc từ hộp thoại changelog thật (`[changelog]`) ngày 08/09/2026, cộng phép đo `[live 08/09/2026]` mở UI thật bằng Playwright ở Mục 7 và Mục 11. Ngoại lệ gắn rõ `[chưa xác minh]`: một vế của Mục 7 (Community Tools Market/Gallery về phân quyền tạo/remix theo gói tài khoản — tuy đã có thêm bằng chứng `[live]` củng cố phần "chỉ trả phí mới tạo tool"), toàn bộ Mục 8 Custom Prompt Expanders, và phần Starter Projects trong Mục 11 (chưa thử trên tài khoản trống). Không tự suy diễn thêm ngoài nguyên văn các trang và hộp thoại đã đọc.
