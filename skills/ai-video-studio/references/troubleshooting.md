# Cạm bẫy và lỗi thường gặp — tra cứu nhanh

Gom tất cả lỗi và cạm bẫy đã ghi nhận được khi dùng Google Flow và các đường sản xuất video liên quan, để tra cứu khi gặp sự cố. Chú giải nguồn. `[live]` là tự mở giao diện và đo trực tiếp ngày 06/09/2026, mức cao nhất. `[changelog]` là đọc trang thay đổi chính thức của Google. `[bNN]` là xem khung hình video hướng dẫn kèm mốc giây, mức trung bình, và nếu thứ nhìn thấy là slide do tác giả video tự soạn thì đã ghi rõ. `[bên thứ ba]` là blog hoặc bài đánh giá, mức thấp nhất, luôn kèm tên nguồn và ngày. Mục chỉ dựa lời kể mà không thấy trên màn hình được gắn "chỉ nghe nói".

---

## 1. Lỗi khi sinh video trong Flow

| Lỗi | Dấu hiệu | Nguyên nhân (nếu biết) | Cách xử lý |
|---|---|---|---|
| Clip mờ hoặc nhân vật biến dạng | Hình bị blur, tỷ lệ cơ thể sai | Mô tả cảnh nhồi quá nhiều chi tiết vào một prompt | Đơn giản hóa mô tả, tách thành nhiều clip ngắn hơn thay vì gộp hết vào một cảnh [b22, slide tổng kết do tác giả video tự soạn, chưa tự đo lại]. |
| Voice không gen hết câu | Lời thoại bị cắt cụt giữa chừng | Lời thoại vượt quá giới hạn xử lý thực tế của model | Giới hạn tối đa khoảng 10 giây lời thoại, trung bình 2 dòng thoại mỗi lượt tạo [b22, slide tổng kết do tác giả video tự soạn, chưa tự đo lại]. |
| Audio lệch hình | Tiếng nói không khớp cử động miệng/hành động | Đoạn lời thoại quá dài để model đồng bộ | Chia lời thoại thành đoạn ngắn, generate từng đoạn thay vì một lần dài [b22, slide tổng kết do tác giả video tự soạn, chưa tự đo lại]. |
| Nhân vật trong video không khớp Character đã lưu | Video ra người khác hẳn dù đã tạo, gán giọng, điền Character Info công phu cho Character đó ngay trước đó cùng phiên | Chưa rõ; nghi là Flow không tự áp dụng Character đã lưu nếu không kéo/gắn nó vào prompt bằng nút "+" | Luôn kiểm tra kỹ nhân vật trong video kết quả; chủ động gắn ảnh Character vào prompt qua Asset Picker thay vì chỉ mô tả bằng chữ [b23]. |
| Hàng đợi do nhu cầu cao | Banner toàn site: "Flow is currently experiencing high demand, affecting video generation. Requests may need to be retried at a later time." Agent trả lời đã "lên lịch và đang chờ xử lý" thay vì render ngay | Tải hệ thống cao | Thử lại sau vài phút; Flow có chính sách hoàn credit cho request thất bại: "AI Credits will be refunded for any failed requests." [live, tự đọc banner trên DOM ngày 06/09/2026; b22]. |
| Lỗi khác đã gặp trực tiếp | "Chunk upload failed: 400" khi build custom Tool | — | Agent tự sửa bằng validate dữ liệu chặt hơn, kiểm tra lại kết quả FFmpeg, quản lý bộ nhớ [b21]. |
| Asset tham chiếu biến mất | Ảnh tham chiếu không còn thấy trong Asset Picker giữa phiên làm việc dài, lọc theo tab hay tìm tên đều không ra | Chưa rõ | Dùng ảnh thay thế, không cố tìm lại [b17]. |
| Tỉ lệ khung hình hiển thị sai trên icon editor | Chọn 16:9 nhưng icon trang editor hiện "9:16" | Nghi là icon mặc định giao diện, chưa chắc phản ánh đúng file thật | Kiểm tra tỉ lệ thật của file (ffprobe) thay vì tin icon, [chưa xác minh, b23]. |
| Storyboard Studio không tự sinh hết các cảnh | Có kịch bản đầy đủ nhưng chỉ ảnh cảnh đầu được tạo | Công cụ chờ lệnh riêng cho từng cảnh, không tự động hoá toàn bộ | Phải yêu cầu lặp lại "tạo ảnh storyboard số X nốt nhé" cho từng cảnh một [b06, mục 7]. |
| Converge không ra được bản render 3D | Bấm "Generate Render" nhưng không có kết quả hoặc kết quả sai | Bỏ qua bước bắt buộc đầu tiên | Phải bấm "Generate Vector Layer" trước để có vector sạch, chọn 1 biến thể, RỒI mới bấm "Generate Render" [b35 t=629-664s]. |
| Agent trả lời bằng tiếng Anh dù hỏi tiếng Việt | Cùng một hội thoại, Agent bất chợt chuyển ngôn ngữ trả lời | Chưa rõ | Không phải lỗi nghiêm trọng nhưng cần đọc kỹ nội dung Agent xác nhận trước khi Approve, vì có thể hiểu sai ý đã hỏi [b22 t=1354s]. |

---

## 2. Cạm bẫy về credit

- **"Tool không tốn credit" là khẳng định SAI một phần.** Mọi tool trong Explore Tools, kể cả tool do Google làm, đều có cảnh báo cố định: *"Google Flow can make mistakes, so double check it. This Tool may consume credits."* Chỉ hai tool đã đo được thực sự KHÔNG trừ credit vì xử lý phía client: **Video Resizer** và **Type Overlays**. Mọi tool khác gọi lại model sinh ảnh/video nền (Nano Banana, Imagen 4, Omni Flash...) nên phải giả định CÓ khả năng tốn credit cho tới khi tự đo được con số cụ thể [live, danh mục tool đọc từ DOM ngày 06/09/2026].
- **Tool cộng đồng (remix từ người khác) vừa có thể sai vừa vẫn tốn credit** — cảnh báo thêm: *"This app was created by another person and may be inaccurate or unsafe. Report unsafe content."* [b35 t=326s].
- **"Veo 3.1 Lite [Lower Priority] = 0 credit" chỉ dành cho gói Ultra, không phải Pro.** Tài khoản Pro theo thiết kế không bao giờ được cấp mục này (đo `[live]` chỉ thấy 4 model, không có mục Lower Priority) — không phải lỗi quan sát. Ngay cả người đã trả tiền Ultra cũng có trường hợp báo với Google là không thấy option này (hai thread hỗ trợ 20/05/2026 và 13/07/2026), khả năng đang rollout dần theo khu vực/tài khoản [live, bảng giá đo trực tiếp trên tài khoản ngày 06/09/2026; changelog.md].
- **360p KHÔNG đúng nửa giá 720p như tài liệu hỗ trợ diễn đạt "khoảng một nửa".** Đo thực tế: 4 và 7 (4 giây), 5 và 10, 6 và 12, 7 và 15 — chỉ ba cặp sau đúng nửa, cặp 4 giây lẽ ra 3,5 nhưng Flow làm tròn lên 4 [live, bảng giá đo trực tiếp trên tài khoản ngày 06/09/2026].
- **Credit KHÔNG cộng dồn sang tháng/ngày sau** ở mọi gói, kể cả free 50 credit/ngày. AI credit KHÔNG khả dụng ở Nhật Bản [tài liệu chính thức Google, đọc ngày 06/09/2026 qua công cụ tóm tắt trung gian nên thấp hơn một mức so với [live]].
- **Ảnh (Image mode) hiện "0 credit" trước khi sinh trên mọi lần quan sát**, nhưng đây chỉ là mẫu hình lặp lại chưa được `[live]` đo trực tiếp xác nhận độc lập (live chỉ đo credit video) — cẩn trọng với trường hợp độ phân giải cao hoặc upscale ảnh [chưa xác minh đầy đủ].
- **Luôn đọc dòng "Generating will use N credits" TRƯỚC khi bấm gửi** — đây là cách rẻ nhất và an toàn nhất để biết chi phí thật của thao tác đang định làm, áp dụng cho mọi model, mọi tool.

---

## 3. Cạm bẫy về giao diện

- **Tên asset trong Video Resizer ghi kích thước DANH NGHĨA, không phải kích thước THẬT của file kết quả.** Ví dụ tên "Resized_1440x1080_..." nhưng file thật đo bằng ffprobe ra 1280×960. Chỉ có TỈ LỆ là khớp, số pixel trong tên luôn sai — phải tự ffprobe file thật mới biết chính xác [live, số đo Video Resizer ngày 06/09/2026].
- **Custom width/height trong Video Resizer chỉ lấy TỈ LỆ, không lấy đúng số pixel đã gõ.** Chiều rộng đầu ra luôn cố định về 1280px (đã loại trừ giả thuyết "gấp đôi nguồn" bằng phép thử độc lập), chiều cao = 1280 chia tỉ lệ. Đưa clip 1080p vào tool này có nguy cơ bị hạ xuống 1280px, tức mất độ phân giải — nên đo lại file đầu ra trước khi resize clip có độ phân giải cao [live, số đo Video Resizer ngày 06/09/2026; chưa xác minh với nguồn 1920px].
- **Ô "Ratio: X:Y" trong Custom chỉ cập nhật khi rời ô (blur), không real-time khi đang gõ** — dễ gây hoang mang tưởng chưa nhận giá trị mới [live, số đo Video Resizer ngày 06/09/2026].
- **Đổi Base Voice/mô tả giọng mới nhưng nhãn preview card vẫn hiển thị mô tả CŨ kế thừa từ giọng gốc** (ví dụ đặt tên "giọng nam trầm" dựa trên base Aoede nhưng nhãn vẫn ghi "Female, breezy, mid pitch"), không tự cập nhật theo mô tả mới [b23 t=340s].
- **Backdrop/Media Grid có thể chặn thao tác tự động hóa**: khi một agent ngoài (Claude in Chrome) điều khiển Flow, prompt có lúc không submit được ở lần bấm đầu tiên, phải chụp lại màn hình xác định đúng nút gửi (mũi tên "→") rồi thử lại [b17 t=623s].
- **Sidebar Images/Videos/Uploads không hiện ngay từ đầu** — chỉ xuất hiện sau khi đã tạo ra ảnh/video hoặc tải file lên lần đầu trong project đó, dễ tưởng nhầm là thiếu tính năng [b01; b05].
- **Số tab/số model hiển thị phụ thuộc thời điểm và hạng tài khoản, không phải lỗi**: Explore Tools từng chỉ có 2 tab (Discover/My Tools), nay `[live]` xác nhận đúng 3 tab (My Tools, Community, Templates). Dropdown model video có 4 mục trên Pro, có thể thấy mục thứ 5 (Lower Priority) chỉ trên Ultra. Số thẻ mẫu Character dao động 4-6 tùy phiên bản [live, danh mục tool đọc từ DOM ngày 06/09/2026; changelog.md].
- **Video dài hơn 10 giây không chỉnh sửa được trong editor** — hiện cảnh báo *"Videos longer than 10s can't be edited. Trim to 10s or under to edit."* kèm nút "Trim Automatically"; cần cắt về đúng 10 giây trở xuống trước khi vào editor chỉnh tiếp [b22 t=1382s, t=1424s].
- **Toggle "Approve, do not ask again" trong Agent mặc định TẮT** — nếu vô tình bật lên, Agent sẽ tự tạo nội dung và tự tốn credit trên toàn project mà không hỏi xác nhận từng lần nữa; nên để mặc định "Always" khi chưa quen luồng làm việc [b01 t=209.6s; b22 t=1405s].

---

## 4. Cạm bẫy về ngôn ngữ

- **Giọng tiếng Việt trong Flow đều "lơ lớ".** Chính Agent/Gemini xác nhận bằng chữ trên màn hình: *"Tính năng tạo lời thoại và giọng nói trong các mô hình video của Google Flow (như Omni Flash) hiện tại chỉ hỗ trợ và tối ưu hóa cho tiếng Anh. Khi bạn nhập lời thoại bằng tiếng Việt, hệ thống tự động dịch hoặc chuyển hướng sang tiếng Anh..."* [b12 t=571.7s]. Mọi voice có sẵn (kể cả mặc định như Aoede) đều là giọng nước ngoài cố đọc tiếng Việt, nghe không tự nhiên [b16; b17].
  - Cách khắc phục đã dùng thật: (1) tạo video KHÔNG lồng tiếng trong Flow, lồng tiếng riêng bằng TTS tiếng Việt chuyên dụng (FPT AI, ElevenLabs) rồi ghép ở Remotion/CapCut; (2) chỉ thêm phụ đề tiếng Việt bằng công cụ dựng phim ngoài [b12 t=585.8s; b16 t=512s; b17 t=643s].
- **Chữ không phải Latin render sai, đặc biệt là bất kỳ ngôn ngữ nào ngoài tiếng Anh khi model tự sinh chữ trên khung hình.** Kiểm thử bên thứ ba có phương pháp (22 prompt, mỗi prompt chạy 2 lần) đo được với tiếng Nhật: chỉ 11/46 ký tự hiragana đọc được, chữ Hán nhiều nét thất bại nhất quán. Kết quả này khớp với quan sát độc lập cho tiếng Việt: dấu thanh điệu đúng nhưng THỨ TỰ CỤM TỪ sai [bên thứ ba: jxp.com/gemini-omni/blog/gemini-omni-review, 21/05/2026, kiểm thử 22 prompt mỗi prompt chạy 2 lần; chưa ai trong nhóm tự lặp lại].
- **Tiếng Việt bị đảo thứ tự cụm từ** khi hiển thị dạng chữ trên khung hình — quan sát khớp với phát hiện review độc lập ở trên; nên kiểm tra kỹ chữ hiển thị sau khi sinh thay vì tin ngay.
- **Yêu cầu giữ đủ dấu tiếng Việt phải ghi rõ trong prompt.** AI có xu hướng bỏ dấu khi tự sinh chữ hiển thị trên màn hình nếu không ràng buộc tường minh — mẹo rút ra từ một chuỗi automation dài: "All Vietnamese text must have FULL diacritical marks" [b17 t=637-870s].
- **Gõ tự động (agent/browser automation kiểu giả lập gõ phím) có thể làm MẤT DẤU tiếng Việt.** Đây là lỗi kỹ thuật của cách nhập liệu, không phải lỗi nội dung prompt. Cách sửa: đổi sang "inject prompt bằng JS" (chèn thẳng giá trị vào ô nhập) thay vì gõ từng ký tự [b04 t=651.0s].
- **Tuân thủ câu lệnh phủ định chỉ khoảng 80%** theo cùng review độc lập nói trên — tránh dựa hoàn toàn vào ràng buộc dạng "không được..." mà không kiểm tra lại kết quả [bên thứ ba: jxp.com/gemini-omni/blog/gemini-omni-review, 21/05/2026, kiểm thử 22 prompt mỗi prompt chạy 2 lần; chưa ai trong nhóm tự lặp lại].

---

## 5. Cạm bẫy khi viết prompt

- **Xuống dòng (Enter) bị Flow hiểu thành NHIỀU lệnh riêng biệt**, sinh dư ảnh/video ngoài ý muốn. Luôn viết prompt thành MỘT ĐOẠN LIỀN MẠCH. Cạm bẫy này được nhấn mạnh độc lập ở ít nhất 3 nguồn khác nhau [b05, ghi chép xem frame video hướng dẫn #7; b16; b17]. Muốn cấu trúc nhiều khối rõ ràng (nhân vật/bối cảnh/lời thoại/lưu ý) vẫn có thể dùng dấu `#` đầu dòng trong CÙNG một đoạn không xuống dòng cứng [b12].
- **Từ "storyboard" dễ bị AI/Flow hiểu nhầm** thành "tạo nhiều clip video rời theo từng panel" thay vì đúng ý là "một ảnh lưới tĩnh chứa nhiều panel". Phải ép rõ chế độ "Image" và yêu cầu tường minh "tạo đúng 1 ảnh" [b16 t=463-501s, t=f_0090-f_0092].
- **Không nói rõ "xuất file để tải về" thì AI có thể chỉ trả lời bằng link xem online**, không phải file tải thật — phải ghi tường minh yêu cầu xuất file, kèm định dạng cụ thể (PDF, .xlsx...) [b18 t=930-942s].
- **Trần 4 lượt sửa trước khi trôi.** Theo review độc lập có phương pháp: "The reliable ceiling is 4 turns. Turn 5 is where drift begins" — sau 4 lượt chỉnh sửa liên tiếp trên cùng một nội dung, chất lượng có xu hướng trôi dạt/giảm dần; nên chốt lại hoặc bắt đầu lại từ prompt gốc thay vì tiếp tục vá thêm [bên thứ ba: jxp.com/gemini-omni/blog/gemini-omni-review, 21/05/2026, kiểm thử 22 prompt mỗi prompt chạy 2 lần; chưa ai trong nhóm tự lặp lại].
- **Độ dài thoại/đoạn nên ngắn**: mỗi cảnh video AI giới hạn 5-10 giây để tránh giật/lag hoặc AI xử lý sai — lặp lại độc lập ở nhiều nguồn (b08: "mỗi cảnh tối đa 5-10 giây"; b06: "mỗi cảnh 10 giây, voiceover 25-35 từ"). Thoại nên dưới 8 giây, 12-15 từ để khẩu hình không lệch [bên thứ ba: snubroot/Veo-3-Prompting-Guide v5.0, 22/07/2025; cộng b08 và b06 là khung hình video hướng dẫn].
- **Giới hạn ký tự khác nhau theo từng ô nhập** — luôn nhìn số đếm hiển thị trực tiếp trên UI thay vì đoán: Sample Dialogue (Google Flow voice) tối đa 120 ký tự; UGC Character prompt tối đa 1000; UGC Image tối đa 18000 [b03 mục 3].
- **Chống biến dạng nhân vật/sản phẩm cần ràng buộc tường minh, không mặc định AI tự giữ đúng**: ví dụ "Retain the details of the dryer, do not alter the product's appearance" (chống méo sản phẩm) [b03]; "IDENTICAL character design... do NOT change face, hair, outfit, or art style" (chống đổi nhân vật giữa cảnh) [b17]. Với hội thoại nhiều nhân vật, phải ghi thêm ràng buộc rõ chống gán nhầm lời thoại: "Tuyệt đối không được nói sai lời thoại của nhân vật... Hãy kiểm soát tuyệt đối và thật chặt chẽ nhé!" [b12].
- **Đọc số bằng giọng nói (dictation) có thể bị ghi thành chữ thay vì số**, ví dụ "hai mươi phần trăm" thay vì "20%" — kiểm tra lại nội dung trước khi gửi nếu nhập liệu bằng giọng nói [b32 t=420s].
- **Tên nhân vật/model do AI gợi ý trong text có thể không khớp tên AI thực sự chọn khi generate** (ví dụ script gợi ý "Soren Mercer" nhưng UI chọn "Soren Kael") — luôn kiểm tra tên thật đã dùng, đừng tin hoàn toàn vào mô tả text [b04].
- **Mỗi cảnh khi dùng Frames to Video (Start/End) cần đúng 2 ảnh, không phải 1** — ảnh trạng thái đầu cảnh và ảnh trạng thái cuối cảnh, để Flow tự nội suy chuyển động giữa hai ảnh; thiếu một trong hai thì không nội suy được [b05 t=170.3s].
- **Prompt mơ hồ kiểu "làm cái banner đẹp" cho kết quả không kiểm soát được** — nên nêu cụ thể kích thước, tông màu, phong cách, dòng chữ chính, vị trí logo ngay từ prompt đầu [b41 t=379-401s].

---

## 6. Lỗi ở các đường khác

### Remotion (qua Claude Code)
- `"Composition with ID ... not found"` — cache hot-reload cũ vẫn dính tham chiếu đã xóa; sửa bằng khởi động lại server Remotion Studio [b26 t=622s].
- `"ReferenceError: ... is not defined"` khi file âm thanh đặt tên không khớp code gọi (code gọi `boing.wav` nhưng file thật tên `sfx_boing.wav`) — kiểm tra lại tên file thực tế khớp với code [b08 t=379s].
- `OffthreadVideo` bị đứng hình khi phát trực tiếp trong Remotion Studio dù render cuối vẫn đúng — dùng `OffthreadVideo` cho bản render cuối, dùng `Video` cho preview trực tiếp [b08].
- `"Failed to render final transparent video with explicit yuva444p10le pixel format"` — Remotion không tự bật kênh alpha cho ProRes 4444 nếu thiếu cả hai cờ `--pixel-format=yuva444p10le` và `--image-format=png` cùng lúc [b39 t=369.2s].
- Dán ảnh trực tiếp vào khung chat Claude Code KHÔNG tạo ra file thật trên máy — không có cách trích xuất thành file, phải upload file thật thay vì paste [b08 t=213s].
- CLI hỏi tương tác (interactive TUI) không nhận input qua pipe (`echo "n" | command`) do dùng raw mode — phải tìm flag tường minh qua `--help` [b09].
- Tên thư mục có dấu tiếng Việt hoặc khoảng trắng làm lệch chuẩn hóa Unicode NFC/NFD, khiến `cd` thất bại; CLI `create-video` từ chối tên thư mục có ký tự non-ASCII — scaffold trong thư mục tạm rồi di chuyển nội dung qua [b09].
- Cờ `--no-git`/`--no-tailwind` không có tác dụng đầy đủ, dự án vẫn tự sinh `.git`/`.gitignore`/`.prettierrc` và vẫn cài tailwind [b09].

### Gemini Notebook (NotebookLM)
- `"NotebookLM can't answer this question. Try rephrasing it..."` xảy ra khi gõ trực tiếp yêu cầu tạo infographic vào khung chat thay vì dùng nút chức năng riêng trong Studio — phải dùng đúng nút chức năng, gõ chat không hoạt động [b45].
- Yêu cầu xuất PDF/Excel lần đầu chỉ trả link xem trực tuyến thay vì file tải về thật — phải yêu cầu lại rõ ràng "xuất file tải về" mới ra file thật [b18 t=942s].
- Infographic sinh ra KHÔNG chỉnh sửa trực tiếp được trong NotebookLM — phải tải ảnh rồi đưa vào Canva (Magic Layers, Edit image) để tách lớp và sửa từng phần [b45].
- Lỗi chính tả thật đã gặp trên infographic do NotebookLM sinh: thiếu từ trong tiêu đề, cột bị cắt chữ — luôn đọc lại kỹ nội dung chữ trước khi dùng [b45 t=486.7-490.5s].

### VMEG (dịch đa ngôn ngữ + lip sync)
- Best Practices cho Lip Sync (ghi nguyên văn trên UI): chỉ một khuôn mặt trong khung, hạn chế lắc đầu, mặt nhìn thẳng camera, đủ sáng, nói tốc độ tự nhiên, video tối thiểu 360px — vi phạm các điều này làm giảm độ chính xác lipsync [b10 t=684s].
- Transcript tự động phiên âm sai tên riêng: "Claude" bị ghi thành "Clock" — kiểm tra lại transcript trước khi dùng làm phụ đề chính thức [b11 t=886s].
- Không có bảng giá credit cố định công bố cho từng thao tác ngoài dòng "Need/Remaining" hiện trước khi submit; chỉ Transcription có công thức rõ (6 credit/phút) — luôn đọc dòng Need trước khi bấm submit.

### OpenMusic AI / Suno
- `"The upstream API service timed out and no results were returned..."` khi tạo nhạc thất bại — thử lại sau [b30 t=520s].
- Bộ lọc tìm kiếm trên Suno có thể trả "No songs found" nếu chồng quá nhiều điều kiện lọc — nới bớt điều kiện lọc [b30 t=307s].
- Bản nhạc preview trên Suno chỉ nghe được 1 phút đầu, cần nâng cấp gói mới nghe được bản đầy đủ [b30].

### Canva (qua Claude connector và độc lập)
- `"không thể truy cập file ảnh từ domain này"` khi dùng ảnh xuất Canva ở nơi khác — dùng trực tiếp Canva export URL thay vì tải về rồi dùng lại [b41 t=601s].
- Claude loay hoay không upload được ảnh riêng qua connector — upload ảnh lên Canva trước rồi mới thao tác qua Claude [b41 t=616s].
- Tải ảnh qua Claude+Canva connector chỉ ra file PNG tĩnh, không mở được như file Canva chỉnh sửa được như kỳ vọng [b43 t=670.6s].
- Gemini dùng lệnh `@Canva` nhiều lần trong ngày có thể bị chặn: *"I'm sorry, but it looks like you've reached your Canva plan's monthly AI limit..."* [b43].
- Giới hạn ký tự Brand Voice: 500/500 (dễ dùng hết nếu mô tả dài) [b43 t=513s].
- Prompt campaign nhập bằng giọng nói bị ghi thành chữ thay vì số (xem thêm Mục 5) [b32 t=420s].
- Website tự sinh (Pomelli) có thể giữ nguyên placeholder chưa thay (`"[YOUR LINK HERE]"`) nếu không kiểm tra kỹ trước khi dùng [b32 t=369s, t=397s].

---

## 7. Lỗi môi trường trên máy Windows

Trên Windows, console mặc định dùng bảng mã **cp1252**, không phải UTF-8. Khi script Python in tiếng Việt (có dấu) ra `stdout`/`stderr`, Python ném `UnicodeEncodeError` và script dừng đột ngột — dù logic script hoàn toàn đúng.

**Đã vá trong toàn bộ script của skill này** (`scripts/config.py`, `assemble_video.py`, `generate_audio.py`, `generate_image.py`, `generate_video.py`, `pipeline.py`, `upload_video.py`, `write_script.py`): mỗi file ép `stdout`/`stderr` sang UTF-8 ngay đầu file bằng `sys.stdout.reconfigure(encoding="utf-8")` và `sys.stderr.reconfigure(encoding="utf-8")`, đặt trong khối `try` với `except Exception: pass` để không làm script dừng nếu môi trường không hỗ trợ `reconfigure`. Nhờ vậy script chạy được ngay mà không cần người dùng tự set biến môi trường `PYTHONIOENCODING` trước khi gọi.

Nếu viết thêm script mới cho skill này trên Windows, áp dụng đúng mẫu vá này ở đầu file trước khi in bất kỳ chữ tiếng Việt nào ra console.

---

## Ghi chú khi dùng file này

- Giao diện Flow thay đổi khá nhanh theo thời gian (số tab, số model, số thẻ mẫu Character đều từng đổi trong vài tháng gần đây) — khi một mục ở đây có vẻ không khớp với giao diện thật đang thấy, ưu tiên tin vào giao diện thật tại thời điểm dùng, đặc biệt là số credit chính xác vì phần này biến động nhiều nhất.
- Trước khi khẳng định một tính năng của Flow có tồn tại hay không, tự bao lâu, hay cho hạng tài khoản nào, mở `changelog.md`, và nếu cần thì mở thẳng `https://flow.google.com/changelogs`, trước — giao diện chỉ nói lên tài khoản đang dùng thấy gì, changelog mới nói lên tính năng có tồn tại không và từ khi nào.
- Mục nào chỉ dựa một nguồn `[bNN]` duy nhất, chưa có `[live]` hay nguồn thứ hai xác nhận lại, đã được giữ nguyên nhãn cảnh báo gốc ("chưa xác minh", "chỉ nghe nói") khi trích dẫn lại ở trên — không nên nâng cấp độ tin cậy của các mục này khi áp dụng vào việc thật.

## 8. Ghép clip Google Flow vào Remotion

Mục này đến từ một lần tự dựng video 10 phút thật ngày 06/09/2026, không phải suy đoán.

| Dấu hiệu | Nguyên nhân | Cách xử lý |
|---|---|---|
| Render chết giữa chừng, log ghi `Compositor error: No frame found at position 8192` | **CHƯA XÁC ĐỊNH ĐƯỢC.** Xem phần dưới bảng | Đổi `<OffthreadVideo>` sang `<Video>` là cách đã chạy được ngay `[live]` |
| Đã mã hoá lại clip mà vẫn chết | Mã hoá lại không phải nguyên nhân | Vẫn nên mã hoá lại cho sạch, nhưng đó không phải cách chữa |
| Khung hình đứng im sau giây thứ 10 | Clip Flow chỉ dài 10 giây còn cảnh dài 60 tới 75 giây | Nhân bản sẵn clip bằng `ffmpeg -stream_loop`, đừng dùng `<Loop>` của Remotion |

Ba chi tiết đã đo được, hữu ích khi chuẩn bị clip:

1. Clip Flow xuất ra có `time_base=1/12288`, một mốc thời gian không thường gặp. Đây là
   nghi phạm đầu tiên nhưng **không phải** nguyên nhân thật.
2. Lệnh chuẩn hoá đã chạy thật và cho ra đúng 300 khung ở 30fps:
   `ffmpeg -i in.mp4 -an -c:v libx264 -pix_fmt yuv420p -r 30 -g 30 -keyint_min 30 -sc_threshold 0 -crf 20 out.mp4`
3. Lệnh nhân bản cho đủ dài một cảnh, đã chạy thật và cho ra 2.700 khung, 90 giây:
   `ffmpeg -stream_loop 8 -i in.mp4 -an -c:v libx264 -r 30 -t 90 out.mp4`

Kèm một cạm bẫy về quy trình. Tôi mất ba lần thử mới tìm ra nguyên nhân, vì hai lần đầu
đều sửa thứ dễ nghi nhất rồi tưởng đã xong. Khi một thay đổi không làm hết lỗi, hãy nói
thẳng là nó không phải nguyên nhân, đừng cộng dồn nhiều thay đổi rồi nhận công cho cái
cuối cùng.


**Đính chính quan trọng về nguyên nhân.** Lỗi trên là có thật và đã lặp lại ba lần
liên tiếp, ở khung 120 rồi khung 15 hai lần. Đổi sang `<Video>` thì render chạy hết
và sản phẩm được dựng bằng bản đó. Nhưng sau khi giao xong, tôi quay lại cô lập
nguyên nhân bằng **năm phép thử đối chứng, và cả năm đều chạy được** với chính
`<OffthreadVideo>`: clip Flow trong composition tối giản, clip do ffmpeg sinh,
composition thật với concurrency mặc định, composition thật với concurrency bằng 1,
và cả trường hợp clip ngắn hơn cảnh.

Nghĩa là **không chứng minh được `OffthreadVideo` có lỗi**, và lỗi hiện không tái
hiện được. Ba giả thuyết từng tin đều bị bác: không phải `time_base=1/12288` của clip
Flow, không phải `<Loop>`, không phải `OffthreadVideo`.

Bài học đi kèm, đáng nhớ hơn cả bản thân lỗi: khi sửa liên tiếp nhiều thứ rồi lỗi
biến mất, **cái sửa cuối cùng không đương nhiên là nguyên nhân**. Muốn quy trách
nhiệm thì phải đổi ngược lại đúng một biến và xem lỗi có quay về không. Tôi đã bỏ
qua bước đó và kết luận sai, kể cả khi đã tự gắn nhãn suy luận.

## 9. Sinh clip trong Flow bằng tự động hoá

| Dấu hiệu | Nguyên nhân | Cách xử lý |
|---|---|---|
| Gõ prompt vào ô nhập rồi bấm sinh, màn hình hiện `The agent failed. Please try again.` | Ô nhập có một **chip `Agent` bật sẵn**, prompt bị định tuyến vào khung chat Agent chứ không vào bộ sinh cổ điển | Bấm tắt chip `Agent`. Khi tắt đúng, chip cấu hình sẽ hiện dạng `Video · 720p · 10s · x1` `[live]` |
| Agent hỏng thì có mất credit không | Không | Đối chiếu sổ giao dịch trước và sau: số dư giữ nguyên, không phát sinh dòng nào `[live]` |
| Tải nhầm clip khi lấy hàng loạt | **Thư viện Flow xếp ngược thứ tự sinh**, clip sinh đầu tiên nằm cuối danh sách | Trích một khung hình của từng clip rồi tự nhìn để gán đúng vai trò, đừng tin thứ tự hiển thị `[live]` |

**Mâu thuẫn về trạng thái mặc định của chip `Agent`, giữ cả hai vế.** Phép đo `[live]` lần đầu (dòng đầu bảng trên) thấy chip `Agent` BẬT sẵn khi vào ô nhập. Một phép đo `[live 08/09/2026]` khác, mở project bằng Playwright trên cùng hạng tài khoản Pro, lại thấy nút `Agent` ở trạng thái KHÔNG pressed ngay khi vừa mở project. Hai phép đo live ở hai thời điểm cho kết quả khác nhau, nên kết luận đúng là: **trạng thái mặc định của chip `Agent` không ổn định, hoặc phụ thuộc vào từng project/phiên bản giao diện tại thời điểm mở**, không phải một trong hai lần đo bị sai. Cách xử lý an toàn không đổi bất kể trạng thái mặc định là gì: luôn tự đọc trạng thái chip trước khi bấm sinh, và triệu chứng nhận biết khi bị định tuyến nhầm vào Agent vẫn là thông báo `The agent failed. Please try again.`

## 10. Điều kiện chạy và giới hạn vùng

Nguồn: `https://support.google.com/flow/answer/16353333`, đọc 08/09/2026 [doc], trừ khi ghi nguồn khác.

- Flow chỉ chạy được ở vùng được hỗ trợ. **VPN KHÔNG mở khoá được vùng chưa hỗ trợ** — đổi IP không đổi được việc tài khoản có được cấp quyền dùng Flow hay không.
- Nên dùng trình duyệt nhân Chromium (Chrome hoặc Edge).
- Cần từ 18 tuổi trở lên VÀ đã qua xác minh tuổi (age verification), không chỉ tự khai tuổi.
- Ở khu vực **EEA, Thuỵ Sĩ, và Anh**: Gemini Omni **không sửa (edit) và không nối dài (extend) được video TẢI LÊN** (uploaded video). Video do chính model của Flow SINH RA thì vẫn sửa và nối dài được bình thường ở các vùng này — ranh giới nằm ở nguồn gốc của video (tải lên vs do model sinh), không phải Omni bị chặn hoàn toàn tính năng sửa video ở các vùng đó [doc, `ai.google.dev/gemini-api/docs/omni`, đọc 08/09/2026].
- Video tải lên (upload) để dùng trong Scenebuilder/Editor: tối đa **60 giây và 1GB**, định dạng chấp nhận `.mov`, `.mp4`, `.avi`, `.wmv` [doc, `support.google.com/flow/answer/16935718`, đọc 08/09/2026]. Cùng trang còn ghi thêm hai ràng buộc chưa từng có trong skill: video dài hơn 30 giây BẮT BUỘC phải cắt còn 30 giây ngay trong Flow trước khi dùng tiếp, và khi sửa bằng Gemini Omni Flash chỉ chọn được tối đa MỘT đoạn 10 giây của video để sửa mỗi lần.

**Về credit khi sinh thất bại.** Trang điều kiện dùng chính thức (16353333) đã đọc toàn trang và KHÔNG có dòng nào nói lượt sinh thất bại có mất credit hay không. Dòng hiện có ở Mục 1 của file này ("Flow có chính sách hoàn credit cho request thất bại...") KHÔNG dựa vào trang tài liệu này — nó dựa vào bằng chứng `[live]`: tự đọc nguyên văn banner cảnh báo hiển thị ngay trên giao diện Flow ngày 06/09/2026 ("AI Credits will be refunded for any failed requests.") cộng với đối chiếu sổ giao dịch trước/sau khi Agent lỗi ở Mục 9 (số dư giữ nguyên, không phát sinh dòng nào). Bằng chứng `[live]` này đứng độc lập với tài liệu chính thức, không bị tài liệu chính thức phủ định, nhưng cần nói rõ ràng nó không đến từ trang hỗ trợ — để khi trang hỗ trợ cập nhật sau này (hoặc khi ai đó nghi ngờ) thì biết cần đối chiếu lại đúng chỗ, không lấy nhầm làm chính sách văn bản chính thức.

## 11. Sinh giọng đọc hàng loạt bằng API TTS

Trong 11 lần gọi liên tiếp có **2 lần hỏng ngay lần đầu**, chạy lại lần hai thành công ngay,
không cần đổi nội dung `[live]`. Đây là lý do hàm gọi TTS bắt buộc phải có retry.

Cần phân biệt hai thứ hay bị gộp làm một. Giọng tiếng Việt **trong giao diện Flow** được
ghi nhận là nghe lơ lớ. Còn giọng tiếng Việt qua **API TTS của Gemini** thì khác hẳn: một
đoạn 127 từ cho máy nghe lại và chép ra chữ đạt **độ khớp 100%** `[live]`. Nếu cần lời đọc
tiếng Việt chuẩn, hãy đi đường API rồi ghép, đừng dùng giọng trong Flow.
