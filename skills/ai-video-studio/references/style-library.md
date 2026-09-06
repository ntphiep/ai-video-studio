# Style Library — bắt và nhân bản style video bất kỳ

Tài liệu này trả lời bốn câu hỏi: mô tả một style bằng khung nào, quy trình
clone style một video/kênh có sẵn ra sao, tên gọi CHÍNH XÁC mà từng công cụ
dùng cho style của nó, và có sẵn khối prompt cho những style phổ biến nào để
dùng ngay. Không lặp lại nội dung đã có ở
[prompt-library.md](prompt-library.md) (khung 9 mục cho prompt ảnh và video,
khung 5 thành phần riêng cho prompt dạng trợ lý, negative prompt,
camera và ánh sáng, chống lỗi tiếng Việt) — file đó vẫn là nguồn cho
cấu trúc câu prompt nói chung.

---

## 1. Hai bộ khung mô tả style

Khi cần "bắt" (capture) một style bất kỳ để tái tạo lại bằng AI, có hai khung
phân tích khác nhau tùy loại nội dung.

### Khung A — Flow Style Writer (6 mục)

Đây là công cụ "Style Writer" có sẵn trong Google Flow (tab Templates, tác
giả Google, mô tả nguyên văn "Turn your mood board into a style prompt"):
đưa vào một frame hoặc ảnh mẫu, công cụ trả về một bản tóm tắt style (Style
Summary) chia làm 6 mục cố định. Dữ liệu dưới đây lấy từ một lần chạy thật
tool Style Writer trên Flow ngày 05/09/2026 (đưa 1 frame anime vào tool,
chép nguyên văn kết quả trả về). Người chạy là người điều phối phiên, agent
soạn file này chép lại kết quả đó chứ không tự chạy tool.

| Mục | Mô tả cái gì |
|---|---|
| **Visual Style** | Trường phái/kỹ thuật hình ảnh tổng thể: hoạt hình hay người thật, mức độ chi tiết, kỹ thuật vẽ/dựng hình (cel-shaded, digital painting, 3D render...). |
| **Composition** | Bố cục khung hình: vị trí chủ thể, tỉ lệ khung (dọc/ngang), độ sâu lớp cảnh (foreground/background), mức độ zoom vào chủ thể. |
| **Attitude** | Cảm xúc/năng lượng tổng thể toát ra từ cảnh: vui tươi, trầm lắng, căng thẳng, ấm áp... |
| **Colors** | Bảng màu chủ đạo, độ tương phản, các màu nhấn (accent) và bối cảnh màu (sáng/tối). |
| **Lighting** | Nguồn sáng (mấy nguồn, từ đâu), kiểu đổ bóng (mềm/cứng), quy ước ánh sáng theo trường phái (vd hoạt hình truyền thống dùng bóng đổ viền cứng). |
| **Camera** | Góc máy, khoảng cách ống kính, độ sâu trường ảnh (depth of field), cảm giác lens tạo ra (thân mật, xa cách, sử thi...). |

Ví dụ output thật (Flow Style Writer, đưa vào 1 frame anime, trích nguyên văn tiếng Anh):

> **Visual Style:** "This aesthetic is defined by high-fidelity anime production values featuring crisp cel-shaded character rendering and detailed illustrative backgrounds. It blends modern digital painting techniques with traditional hand-drawn character design."
>
> **Composition:** "A centered subject in a vertical portrait orientation creates a strong focal point, while the layered background provides environmental context through depth. The framing remains tight on the upper torso to emphasize action and expression."
>
> **Attitude:** "The scene radiates a vibrant and wholesome energy, capturing a moment of energetic focus and quiet, industrious confidence. It conveys the warmth and communal spirit of a bustling outdoor night event."
>
> **Colors:** "The palette uses warm tones of crimson and amber against dark surroundings, creating a vivid and inviting nighttime atmosphere. High-contrast saturated accents in the background lanterns provide a festive variety of hues."
>
> **Lighting:** "Multiple ambient light sources from hanging lanterns create a soft facial glow, complemented by sharp rim lighting that defines the character's silhouette. Hard-edged shadows follow traditional animation conventions to create form."
>
> **Camera:** "An eye-level perspective and tight close-up framing use a shallow depth of field to transform distant lights into soft bokeh circles. The lens choice feels intimate and personal, focusing entirely on the subject's immediate activity."

Cách dùng: copy nguyên 6 đoạn này (hoặc rút gọn còn các cụm từ khóa chính)
dán thẳng vào ô prompt của Flow khi tạo video mới. Đây chính là "Style
Summary" mà quy trình clone ở mục 2 sẽ dùng. Ngoài lần chạy thật này, kho
49 file vision (b01-b49) chưa từng ghi lại thao tác chi tiết nào khác bên
trong Style Writer, chỉ có mô tả một dòng trong catalog chính thức của Flow
(xem Tự soát nguồn).

### Khung B — 7 tiêu chí clone thiết kế

Khung này đến từ việc hỏi Claude "để bắt chước một dạng thiết kế nào đó thì
cần phân tích bao nhiêu tiêu chí" trong quy trình dựng video bằng Remotion
(nguồn là bản trích transcript của phiên làm việc, nay không còn trên đĩa, không phải file
trong skill). Câu trả lời là 7 nhóm: **màu sắc, typography/chữ, layout/grid,
hình dạng, hình ảnh, chuyển động, cảm xúc**.

- Màu sắc: bảng màu chủ đạo, màu nhấn, độ bão hòa.
- Typography: font chữ, độ đậm nhạt, cách sắp chữ (kerning, tracking).
- Layout/grid: cách chia bố cục, canh lề, tỉ lệ khung.
- Hình dạng: đường nét, bo góc, hình khối đặc trưng.
- Hình ảnh: phong cách minh họa/ảnh chụp, mức độ chi tiết.
- Chuyển động: kiểu animation, tốc độ, easing.
- Cảm xúc: tông cảm xúc tổng thể mà thiết kế truyền tải.

### Khi nào dùng khung nào

- **Khung A (Flow, 6 mục)**: hợp với cảnh quay thật (live-action) hoặc
  animation có bối cảnh/nhân vật/ánh sáng thật sự (anime, 3D, claymation...),
  tức bất cứ khi nào có "cảnh" để mô tả camera và lighting.
- **Khung B (7 tiêu chí)**: hợp với motion graphics, đồ họa 2D phẳng, UI/UX,
  infographic, nơi không có "máy quay" hay "ánh sáng vật lý", mà quan trọng
  là màu, chữ, layout, chuyển động của các thành phần đồ họa.

---

## 2. Quy trình clone style một video/kênh bất kỳ

Có hai đường để lấy được một khối mô tả style dùng lại được. Chọn đường A nếu
làm việc trực tiếp trên Flow với video mẫu sẵn có; chọn đường B nếu cần
nghiên cứu sâu một trường phái (style) trước khi dựng, đặc biệt hợp với
motion graphics/Remotion.

### Đường A — Clone qua Flow Style Writer

Ràng buộc quan trọng nhất: giữ nguyên đúng **6 mục đầu ra** của Style Summary
(Visual Style, Composition, Attitude, Colors, Lighting, Camera) xuyên suốt
quy trình, không tự gộp hay bỏ bớt mục nào.

1. Trích 1 (hoặc vài) frame tiêu biểu từ video mẫu bằng ffmpeg, ví dụ:
   `ffmpeg -i input.mp4 -vf "select='eq(n,100)'" -vframes 1 frame.png`
2. Đưa frame đó vào công cụ Style Writer trong Flow.
3. Lấy Style Summary, giữ nguyên đủ 6 mục, không rút gọn xuống dưới 6 mục.
4. Copy nguyên văn (hoặc rút gọn thành 3-4 cụm từ khóa mỗi mục, vẫn giữ đủ
   6 nhãn mục) vào prompt tạo video mới trên Flow.
5. Test bằng model rẻ/free trước (xem mẹo credit ở prompt-library.md),
   ưng ý mới render bản chất lượng cao.
6. Với dự án nhiều cảnh, có thể chuyển sang tool **Story Sketch** ("Create
   storyboards that follow any visual style") để giữ style nhất quán qua
   nhiều panel thay vì lặp Style Writer cho từng cảnh. [chưa tự sinh thử].

### Đường B — Nghiên cứu style trước rồi mới dựng (hợp Remotion/motion graphics)

Quy trình này đúc kết từ cách một kênh dựng video "Vox style" (collage
cut-out) bằng Claude Code + Remotion, không đi qua Flow/Veo.

1. **Định nghĩa style bằng công cụ nghiên cứu tổng hợp** (không hỏi thẳng
   Claude trước), vì công cụ tìm kiếm tổng hợp real-time tốt hơn cho việc
   liệt kê các biến thể của một trường phái. Prompt mẫu (nguyên văn từ
   transcript gốc):
   > "bạn có biết gì về vox style không, tổng hợp tất cả những cái kỹ thuật vox style hiện có và các cái ảnh video minh họa"

   Sau khi chọn được nhánh style ưng ý, đào sâu thêm:
   > "tôi muốn tìm hiểu thêm về kiểu collage cut out này"

2. **Yêu cầu đóng gói thành một prompt định hình phong cách**, đây là bước
   quan trọng nhất, biến kết quả nghiên cứu thành một khối prompt dùng lại
   được nhiều lần:
   > "nếu như mô tả cho một AI hiểu được về cách làm và style thì tôi nên mô tả phong cách collage cut out như thế nào. Thì bạn hãy tạo một prompt định hình phong cách đó được hay không."

   Kết quả thực tế (Perplexity, cho một video Nokia dạng explainer) là một
   khối prompt tiếng Việt đầy đủ, đã bổ sung vào mục 4 (hàng "Collage
   cut-out kiểu Vox, bản đầy đủ").

3. Đưa prompt đó cho Claude Code (không phải Claude thường), kèm giải thích
   ngắn gọn về style, để Claude tự tìm hiểu thêm rồi bắt tay dựng:
   > "giải thích về cái collage cut out, vox style là một cái dạng style như thế nào, như thế nào và mình bảo nó là bạn tự tìm hiểu để hiểu thêm về vox style kỹ thuật collage cut out này nhé."
   >
   > "mình muốn bạn dựng một cái video Remotion theo theo cái style này, dùng các cái nguồn ảnh có sẵn để có thể tải về và lấy ảnh liên quan và làm."

4. **Cách khác, tổng quát hơn, cho bất kỳ dạng thiết kế nào** (đây là nguồn
   của Khung B ở mục 1): hỏi thẳng Claude tiêu chí phân tích, nguyên văn:
   > "để có thể bắt chước một dạng thiết kế nào đó thì chúng ta cần phải phân tích bao nhiêu tiêu chí và đó là những tiêu chí gì?"

   Sau khi có 7 tiêu chí, yêu cầu Claude tạo tiếp **một prompt phân tích
   chuẩn hóa** để lần sau chỉ cần đưa ảnh mẫu là chạy được ngay (không phải
   soạn lại câu hỏi mỗi lần), rồi tiếp tục yêu cầu Claude tạo **prompt tạo
   ảnh giữ nguyên style** đã phân tích, để dùng lặp lại nhiều lần mà không
   phải mô tả lại từ đầu.

### Vòng lặp "giáo viên - học sinh"

Cả hai đường trên đều dùng chung một nguyên tắc sửa: **không đưa hết ý tưởng
ngay từ đầu**. Đưa mô tả ban đầu, để AI (Claude hoặc Flow Agent) tự trình bày
cách nó hiểu và tự dựng một bản nháp trước, rồi mới sửa dần từng điểm một,
giống một giáo viên để học sinh làm thử trước khi chỉnh. Thực tế của quy
trình clone Vox style mất khoảng **5 vòng sửa** mới ra bản ưng ý, mỗi vòng chỉ
sửa một hoặc vài điểm cụ thể:

- Vòng 1: yêu cầu tách nền nhân vật, bo viền giấy trắng nhạt, đa dạng hóa animation giữa các cảnh (thay vì lặp lại một kiểu).
- Vòng 2: đổi nền sang dạng giấy (paper texture) cho có cảm giác thủ công; đổi cách hiển thị text (catchy hơn, chỉ hiện phần highlight, không hiện caption cơ bản); phóng to nhân vật, cho chuyển động tại chỗ (low-key).
- Vòng 3: tăng cỡ chữ, đưa text vào khu vực giữa/gần element; tăng cỡ icon; thêm hiệu ứng âm thanh phù hợp.
- Vòng 4: tăng độ khó bố cục, mỗi cảnh có 2-5 element tách rời, trượt chồng lên nhau đúng vị trí kịch bản.
- Vòng 5: element to hơn nữa, hiển thị rõ ràng hơn.

Sau vòng cuối, yêu cầu Claude tự phân tích lại toàn bộ phong cách kết quả và
đóng gói thành skill, để lần sau chỉ cần đưa audio + script là chạy tự động.
Nguyên tắc chung nên áp dụng ở mọi vòng: luôn yêu cầu AI **confirm lại ý
tưởng/cách hiểu trước khi thực thi**, để phát hiện hiểu sai sớm thay vì phải
sửa sau khi đã dựng xong.

---

## 3. Danh sách tên style CHÍNH XÁC theo từng công cụ

Mỗi công cụ AI dùng một bộ tên style riêng, không dùng chung một từ vựng.
Đây là kho tra cứu để gõ ĐÚNG tên style mà giao diện công cụ đó hiểu, thay vì
đoán hoặc dịch nghĩa. Toàn bộ mục này lấy từ quan sát UI/video hướng dẫn (kho
49 file vision b01-b49, đối chiếu catalog Flow [live] ngày 06/09/2026), tức
style **do người khác chạy, agent chỉ quan sát và ghi lại**, KHÔNG phải
agent này tự sinh thử. Toàn bộ style ở mục này đánh dấu **[chưa tự sinh
thử]**, khác với 4 style đã render thật liệt kê ở mục 4.

| Công cụ | Trường chọn | Tên/giá trị CHÍNH XÁC trên giao diện |
|---|---|---|
| NotebookLM Video Overview | Choose visual style (10 lựa chọn) | Auto-select, Custom, Classic, Whiteboard, Kawaii, Anime, Watercolor, Retro print, Heritage, Paper-craft |
| NotebookLM Video Overview | Format | Cinematic (New!), Explainer, Brief |
| NotebookLM Audio Overview | Format | Deep Dive (mặc định), Brief, Critique, Debate |
| NotebookLM Audio Overview | Length | Short / Default / Long |
| NotebookLM Infographic | Style (bản Việt, lần 1) | Đất sét, Báo chí, Hướng dẫn, Lưới Bento, Gạch (còn cuộn che, tác giả nói có tới 10 style) |
| NotebookLM Infographic | Style (bản Anh, lần 1) | Auto-select, Kawaii, Clay, Sketch Note, Anime, Editorial |
| NotebookLM Infographic | Style (bản Việt, lần 2) | Tự động chọn, Ghi chú phác thảo, Kawaii, Chuyên nghiệp, Có tính khoa học, Anime |
| NotebookLM Infographic | Style (bản Anh, lần 2) | Auto-select, Sketch Note, Kawaii, Professional, Scientific, Anime |
| NotebookLM Infographic | Orientation / Level of detail | Landscape, Portrait, Square / Concise, Standard, Detailed (nhãn "BETA") |
| Google Flow — Story Animator | Dropdown "Phong cách" | Điện ảnh, Tả thực, Anime, Hoạt hình 3D, Tranh sơn dầu, Màu nước |
| Google Flow — Storyboard Studio | Style | Realistic (mặc định), Claymation |
| UGC Character (UGCVideo.ai) | Look Vibe | 90s Style, Casual Style, Glam Style, Gym Style, Office Style, Street Style, Y2K Style |
| Suno / OpenMusic | Thể loại (chip chọn nhanh) | Country, Folk, Rock, Blues, Cổ điển, Disco, Funk, cộng nút "Thêm >" |

Ghi chú Infographic: 4 phiên bản tên style xuất hiện ở 4 video khác nhau,
khả năng do Google cập nhật giao diện theo thời gian hoặc lệch Anh/Việt, cần
đối chiếu lại UI thật trước khi đưa vào skill chính thức.

**Style Writer, Story Sketch, Converge** không dùng dropdown cố định mà nhận
style dưới dạng đầu vào tự do: Style Writer nhận một mood board/frame ảnh
bất kỳ rồi xuất Style Summary văn bản (Khung A ở mục 1); Story Sketch mô tả
nguyên văn "Create storyboards that follow any visual style"; Converge có ô
**Style** dạng văn bản tự do trong panel "RENDER OUTPUT SETTINGS" (ví dụ giá
trị quan sát được "Macro 3D Studio Rendering"), quy trình bắt buộc vẽ phác
thảo rồi bấm "Generate Vector Layer" trước, sau đó mới bấm "Generate Render",
bỏ qua bước vector sẽ không render được.

**Brand Kit (Claude/AI Studio)** không phải style cố định của một công cụ mà
là style thương hiệu tự định nghĩa: yêu cầu Claude liệt kê bảng màu (hex),
typography rule, visual style guide, và "5 câu mô tả phong cách hình ảnh"
sẵn sàng dán vào prompt AI. Ví dụ Brand Kit Red Bull: "Dark dramatic
backgrounds, high-contrast lighting, action photography, motion blur, neon
glow effects in red and yellow, wide-angle or low-angle shots". Khai báo
brand/style này một lần ở đầu phiên để AI áp dụng nhất quán cho các lần sau.

---

## 4. Thư viện style (khối prompt mẫu dùng ngay)

Bảng dưới cung cấp khối prompt mẫu tiếng Anh dùng được ngay, theo đúng công
thức đã verify:

```
[Tên style đầy đủ]: [cảnh + hành động], [chất liệu/kết cấu đặc trưng],
[kiểu ánh sáng của style], [đặc điểm chuyển động của style].
```

Ghép thêm phần chủ thể/hành động cụ thể của video mình vào chỗ "[cảnh +
hành động]" trước khi dùng. Cột "Ghi chú" đánh dấu rõ **Đã tự sinh thử** (có
clip/ảnh thật do phiên này render ra) hoặc **[chưa tự sinh thử]** (khối
prompt do agent soạn hoặc trích nguyên văn từ nguồn khác, chưa từng chạy qua
Flow hay bất kỳ model video/ảnh nào trong các phiên này).

### Live action

| Tên style | Khối prompt mẫu | Dấu hiệu nhận ra | Ghi chú |
|---|---|---|---|
| Cinematic 35mm | `Cinematic 35mm film look: [cảnh + hành động], shot on 35mm film with fine natural grain, anamorphic lens flare, shallow depth of field, warm color grade with lifted blacks, slow deliberate dolly movement.` | Grain mịn, flare lens ngang, DOF nông, màu ấm hơi ám vàng | [chưa tự sinh thử] |
| Documentary 16mm vintage | `Documentary 16mm vintage: [cảnh + hành động], grainy 16mm film texture with light flicker and dust specks, muted desaturated color grade, natural available light only, handheld observational camera with slight drift.` | Nhiễu hạt to, ám vàng/xanh rêu, rung máy nhẹ tự nhiên | **Đã tự sinh thử 05/09/2026** — `flow_style_doc16mm_360p.mp4`, frame thật có viền khung phim, ám vàng, bụi trong luồng sáng |
| Handheld vlog | `Handheld vlog realism: [cảnh + hành động], natural skin texture, slightly shaky handheld camera, on-camera flash or natural window light, casual eye-level framing, natural motion blur on quick moves.` | Rung tay rõ, góc mắt thường, ánh sáng tự nhiên không dàn dựng | [chưa tự sinh thử] |
| Phim noir | `Film noir: [cảnh + hành động], harsh venetian-blind shadow patterns, high contrast black and white, low-key single-source lighting, dramatic low angle, slow ominous camera creep.` | Tương phản cao, bóng kẻ sọc, đen trắng hoặc gần như đơn sắc | [chưa tự sinh thử] |
| Golden hour realism | `Golden hour realism: [cảnh + hành động], realistic skin texture, warm low-angle sunlight with long soft shadows, natural lens flare, gentle handheld or slow tracking movement.` | Ánh sáng vàng cam xiên góc thấp, bóng dài mềm | [chưa tự sinh thử] |
| ASMR macro | `ASMR macro close-up: [cảnh + hành động], extreme macro lens, crisp tactile texture detail, soft diffused studio lighting, ultra slow motion, clean minimal background, satisfying crisp sound cues.` | Cực cận, chi tiết bề mặt rõ, chuyển động rất chậm | [chưa tự sinh thử] |

### Animation 2D

| Tên style | Khối prompt mẫu | Dấu hiệu nhận ra | Ghi chú |
|---|---|---|---|
| Anime cel-shaded | `Japanese anime cel-shaded animation: [cảnh + hành động], crisp cel-shaded rendering with visible line art, flat color blocks with hard-edged shadows, warm ambient glow light source, expressive large anime eyes, smooth 2D animation movement.` | Nét viền rõ, mắt to biểu cảm, tô màu phẳng, bóng đổ viền cứng | **Đã tự sinh thử 05/09/2026** — ra clip 360x640 |
| Hand-drawn flat illustration | `Hand-drawn flat illustration: [cảnh + hành động], flat vector shapes with soft rounded edges, limited warm color palette, even soft lighting with no hard shadows, gentle draw-on stroke-by-stroke reveal animation.` | Hình khối phẳng bo tròn, không đổ bóng gắt, nét vẽ hiện dần | [chưa tự sinh thử] |
| Webtoon/comic | `Webtoon comic style: [cảnh + hành động], bold black outline linework, halftone or flat cel color fill, panel-style composition, dramatic speed lines on fast motion, punchy high-contrast lighting.` | Viền đen dày, có ô panel, hiệu ứng tốc độ | [chưa tự sinh thử] |
| Kinetic typography | `Kinetic typography motion graphics: [chữ/số + nội dung xuất hiện], bold sans-serif type, high-contrast flat color blocks, sharp graphic lighting with no realistic shadow, punchy snap-in and bounce text animation timed to beat.` | Chữ to bật vào theo nhịp, màu phẳng tương phản cao | **Đã tự sinh thử 05/09/2026** — `flow_kinetic_type_vn_916.mp4`, chữ tiếng Việt đủ dấu, nhưng **thứ tự cụm từ không đúng yêu cầu**, xem `troubleshooting.md` mục 4 |
| Draw-on animation | `Draw-on stroke animation: [cảnh + hành động], hand-drawn linework building up stroke by stroke, flat minimal color fill added after outline completes, soft even lighting, deliberate steady drawing-reveal motion (not fade or slide).` | Nét vẽ hiện dần hoàn thiện tranh, không phải fade/slide | [chưa tự sinh thử], đúc kết từ quy trình Remotion |
| Collage cut-out kiểu Vox (bản rút gọn 4 thành phần) | `Vox-style paper collage: [cảnh + hành động], cut-out photo elements with thin white paper border and soft drop shadow, textured paper background, warm editorial color grade, elements sliding and layering in one at a time with varied motion per scene.` | Ảnh cắt viền giấy trắng, nền giấy có vân, nhiều lớp chồng | [chưa tự sinh thử] |
| Collage cut-out kiểu Vox (bản đầy đủ, nguyên văn tiếng Việt từ Perplexity) | `"Tạo một video theo phong cách collage cutout documentary, giống một bài explainer hiện đại. Toàn bộ cảnh được dựng bằng các mảng ảnh cắt nền sạch, chồng lớp rõ ràng, có cảm giác thủ công như giấy cắt và scrapbook editorial. Giữ chủ thể tách biệt rõ khỏi background, dùng texture giấy nhẹ, mép cắt gọn nhưng có chút thô tự nhiên, bóng đổ mềm, và độ sâu bằng nhiều lớp foreground, midground, background. Chuyển động camera chậm và tinh tế, chủ yếu là pan, zoom, parallax, slight shake nhẹ kiểu documentary, không rung mạnh. Mỗi cảnh phải rõ ý, ít chi tiết thừa, ưu tiên khả năng đọc hình nhanh. Chèn text highlight, label, arrow, line, map callout hoặc annotation khi cần. Màu sắc tối giản, tương phản tốt, hơi editorial, có cảm giác báo chí, tài liệu, thông tin trực quan. Nhịp dựng ngắn, mạch lạc, thiên về storytelling, giống video giải thích của Vox."` | Cùng dấu hiệu như bản rút gọn, nhưng có thêm callout/annotation, nhịp dựng ngắn kiểu báo chí | [chưa tự sinh thử], nguồn Perplexity (xem mục 2 Đường B) |

### Animation 3D

| Tên style | Khối prompt mẫu | Dấu hiệu nhận ra | Ghi chú |
|---|---|---|---|
| 3D Pixar feature look | `3D Pixar-style animated feature: [cảnh + hành động], soft stylized 3D character rendering with expressive exaggerated features, warm cinematic three-point lighting, rich saturated color palette, smooth fluid character animation with clear anticipation and follow-through.` | Nhân vật 3D bo tròn dễ thương, ánh sáng ba điểm ấm, màu bão hòa | **[chưa tự sinh thử]** — có gửi lên Flow 05/09/2026 nhưng bị chặn vì kèm tỉ lệ 1:1, chưa chạy lại ở 16:9, không có clip nào được sinh ra |
| Stop-motion claymation | `Handmade stop-motion claymation: [cảnh + hành động], clay figures with visible fingerprints and felt textures, miniature handcrafted set, tactile warm studio lighting, slight stop-motion jitter between frames.` | Vân tay trên đất sét, vải nỉ, rung nhẹ giữa khung hình | **Đã tự sinh thử 05/09/2026** — ra clip 360x640 khác biệt rõ so với anime |
| Low-poly | `Low-poly 3D render: [cảnh + hành động], faceted geometric low-polygon models, flat-shaded surfaces with visible triangular facets, simple gradient sky lighting, smooth minimal camera pan.` | Bề mặt đa giác góc cạnh, tô màu phẳng theo mặt | [chưa tự sinh thử] |
| Isometric diorama | `Isometric diorama render: [cảnh + hành động], clean isometric camera angle, miniature diorama scale with soft toy-like materials, bright even studio lighting, subtle looping idle animation.` | Góc isometric cố định, cảm giác mô hình thu nhỏ | [chưa tự sinh thử] |

### Đồ họa / kỹ thuật

| Tên style | Khối prompt mẫu | Dấu hiệu nhận ra | Ghi chú |
|---|---|---|---|
| Motion graphics số liệu | `Data-driven motion graphics: [số liệu/thống kê xuất hiện], bold flat geometric shapes and icons, high-contrast brand color blocks, sharp digital graphic lighting, numbers counting up with snappy easing and icon bounce accents.` | Số đếm chạy, icon nảy, màu khối phẳng tương phản | [chưa tự sinh thử] |
| Infographic động | `Animated infographic: [dữ liệu/so sánh xuất hiện], clean flat vector icons and charts, minimal 2-3 color palette, even flat lighting with no shadow, elements building in sequentially with smooth slide and fade.` | Biểu đồ/icon xuất hiện tuần tự, màu tối giản | [chưa tự sinh thử] |
| Whiteboard explainer | `Whiteboard explainer animation: [cảnh + hành động], simple black marker line-drawing on white background, minimal flat color fill, flat even lighting, hand-drawing-in-progress reveal motion with visible drawing hand or pen tip.` | Nét vẽ marker đen trên nền trắng, có hiệu ứng tay vẽ | [chưa tự sinh thử] |
| Glitch/datamosh | `Glitch datamosh aesthetic: [cảnh + hành động], RGB channel split and pixel-sorting artifacts, harsh digital noise overlay, flickering high-contrast neon lighting, jarring stutter cuts and frame-repeat glitches.` | Lệch kênh màu RGB, nhiễu số, giật khung hình | [chưa tự sinh thử] |
| Retro VHS | `Retro VHS aesthetic: [cảnh + hành động], analog tape noise and tracking lines, soft chromatic bleed, warm low-fidelity color grade with crushed blacks, slight tape-warp jitter and scan-line flicker.` | Nhiễu băng từ, đường quét ngang, màu bệt kiểu cũ | [chưa tự sinh thử] |
| Oversimplified/Casually Explained (flat cartoon, nguyên văn) | `"A hand-drawn 2D flat illustration in the style of Oversimplified / Casually Explained YouTube channel. Stick figure character with a perfect white circle head, two simple round dot eyes, a thin straight or slightly curved mouth line, stick body and limbs with bold black outlines (2-3px). Flat colors with NO gradients, NO highlights, NO depth shading. ALL elements outlined in dark near-black (#1C1C1C). Background is a simple flat landscape scene: solid sky blue (#7ECFE0) top half, solid grass green (#5AB033) bottom half. Color palette: muted cartoon: sky blue, grass green, earthy brown, flat gray, white, sandy beige. Art style: naive flat cartoon, hand-drawn digital, deadpan humor aesthetic. Scene text in ALL CAPS handwritten bold font (Permanent Marker style), black, top-center of frame. 16:9 landscape format, widescreen YouTube thumbnail ratio. Clean simple composition, lots of negative space in sky area. NO photorealism, NO 3D rendering, NO anime style, NO Disney style. [THÊM MÔ TẢ SCENE CỤ THỂ Ở ĐÂY]"` | Đầu tròn trắng tuyệt đối, mắt chấm tròn, viền đen dày 2-3px, không gradient/shading | [chưa tự sinh thử], nguyên văn do Claude soạn để tái dùng nhiều lần cho một kênh YouTube |
| Vintage motorsport poster (illustration, nguyên văn) | `"A vintage European motorsport poster in the style of 1960s-1970s Italian and French Grand Prix art. A sleek Formula 1 or GT racing car, Ferrari red or cobalt blue, captured mid-corner at high speed, motion blur on the wheels, low camera angle. Background features an iconic European circuit: winding mountain road, cobblestone town, or coastal cliffside at golden hour. Bold retro typography with the race name in large sans-serif or slab-serif font, subtle grid lines and geometric shapes as decorative elements. Color palette: deep red, ivory, navy blue, gold, with a slightly faded, screen-printed texture. Cinematic, dramatic lighting. Poster format, vertical orientation. High detail, painterly illustration style blending realism with graphic design."` | Xe đua mid-corner mờ chuyển động, chữ retro slab-serif, màu đỏ/ngà/navy/vàng kim, vân in lụa bạc màu | [chưa tự sinh thử], do Google Flow Agent tạo rồi xuất sang Canva |

---

## 5. Ràng buộc giữ style ổn định giữa nhiều clip

Khi một video/project gồm nhiều clip, style dễ bị "trôi" giữa các clip nếu
mô tả lại từ đầu mỗi lần. Hai nguyên tắc để giữ ổn định:

1. **Chuẩn hóa 2-3 lighting descriptor cho cả project** và dùng lại đúng
   những từ đó ở mọi clip (ví dụ luôn dùng "golden hour, soft rim light,
   film grain" thay vì đổi cách mô tả ánh sáng mỗi clip), tránh việc màu
   sắc/độ tương phản nhảy lung tung giữa các clip trong cùng video.
2. **Dùng lại đúng một khối style** (một trong các khối ở mục 4, hoặc Style
   Summary lấy từ Khung A) làm nền cố định cho toàn bộ project, và **mỗi lần
   chỉ đổi một biến**, camera hoặc hành động hoặc bối cảnh, không đổi nhiều
   biến cùng lúc. Đổi nhiều biến một lúc là nguyên nhân phổ biến khiến clip
   sau trông như một style khác hẳn clip trước.

---

## Tự soát nguồn

- Khung A (6 mục Flow Style Writer) và ví dụ output tiếng Anh: **chạy thật
  tool Style Writer trong phiên 05/09/2026**, đưa 1 frame anime vào và chép
  nguyên văn kết quả. Người chạy là người điều phối phiên, agent soạn file
  này chép lại chứ không tự thao tác. Đối chiếu bản tổng hợp Flow Tools từ 49 báo cáo xem frame và
  bản tổng hợp Google Flow từ 49 báo cáo xem frame (49 file vision + catalog Flow [live] 06/09/2026):
  Style Writer không có bằng chứng thao tác chi tiết nào khác ngoài lần chạy
  thật này, nên quy trình 6 mục vẫn chỉ dựa trên một lần chạy duy nhất.
- Khung B (7 tiêu chí clone thiết kế) và các prompt nguyên văn ở mục 2 (câu
  hỏi Perplexity, câu yêu cầu đóng gói "prompt định hình phong cách", câu
  hỏi Claude về tiêu chí phân tích, 5 vòng sửa Vox style): đúc kết từ phụ đề
  tự động tiếng Việt của kênh "Non-tech làm AI" trên YouTube, xử lý trong một
  phiên làm việc trước, bản trích tạm nay không còn trên đĩa. Phụ đề tự động
  có lỗi phiên âm ở vài chỗ, đã giữ nguyên văn và không tự diễn giải thêm.
  Vì nguồn gốc là phụ đề chứ không phải khung hình, mức bằng chứng ở đây là
  `[bên thứ ba, chỉ nghe nói]`, thấp hơn phần trích từ khung hình.
- Mục 3 (danh sách tên style theo từng công cụ) trích từ bản tổng hợp prompt từ 49 báo cáo xem frame
  mục 4, tổng hợp từ 49 file quan sát khung hình (`b01`-`b49`) đối chiếu
  catalog Flow qua bản tổng hợp Flow Tools từ 49 báo cáo xem frame và bản tổng hợp Google Flow từ 49 báo cáo xem frame ([live],
  06/09/2026). Toàn bộ style ở mục 3 đánh dấu [chưa tự sinh thử] vì đây là
  quan sát UI/video hướng dẫn, không phải lần agent này tự vận hành công cụ.
- Bốn style đánh dấu **Đã tự sinh thử 05/09/2026** ở mục 4 là **anime
  cel-shaded**, **stop-motion claymation**, **documentary 16mm vintage** và
  **kinetic typography** (kèm cảnh báo về thứ tự cụm từ). Bằng chứng là bốn
  file MP4 trong `output\` (`flow_style_anime_360p.mp4`,
  `flow_style_claymation_360p.mp4`, `flow_style_doc16mm_360p.mp4`,
  `flow_kinetic_type_vn_916.mp4`), số đo bằng `ffprobe`, dấu hiệu thị giác
  đọc trực tiếp từ frame trích bằng `ffmpeg`. Khối prompt trong bảng là bản
  chuẩn hóa theo khung 9 mục ở `prompt-library.md`, không phải chuỗi ký tự y hệt đã
  gửi lên Flow; prompt gốc nằm trong `prompt-library.md` và lịch sử phiên
  Flow. Ngược lại, **3D Pixar feature look** đã gửi lên Flow cùng ngày
  nhưng **bị tầng validation chặn** vì kèm tỉ lệ 1:1, không có clip nào
  được sinh ra, nên vẫn đánh dấu [chưa tự sinh thử].
- Hai prompt nguyên văn mới thêm ở mục 4 ("Oversimplified/Casually
  Explained" và "Vintage motorsport poster") cùng bản đầy đủ tiếng Việt của
  "Collage cut-out kiểu Vox": chép nguyên văn từ bản tổng hợp prompt từ 49 báo cáo xem frame mục
  1.2 (khung hình b25, b26, b41), KHÔNG phải agent này tự chạy qua model
  ảnh/video nào, đánh dấu [chưa tự sinh thử].
- Mọi style còn lại trong bảng mục 4 (cinematic 35mm, handheld vlog, phim
  noir, golden hour, ASMR macro, hand-drawn flat, webtoon, draw-on, collage
  cut-out bản rút gọn, low-poly, isometric, motion graphics số liệu,
  infographic, whiteboard, glitch, VHS): khối prompt do agent này tự soạn
  dựa trên công thức chung và dấu hiệu thị giác đặc trưng đã biết của từng
  style, chưa chạy thử qua Flow hay bất kỳ model video nào, đánh dấu rõ
  [chưa tự sinh thử] trong bảng.
- Công thức 5 phần, chuẩn hóa lighting descriptor, "1 biến/lần iterate":
  đã có sẵn ở `prompt-library.md` trong cùng thư mục, dẫn lại nguyên tắc
  chứ không trích lại nguồn gốc (xem mục "Tự soát nguồn" của file đó).
