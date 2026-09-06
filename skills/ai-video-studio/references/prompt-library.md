# Thư viện prompt và kiến thức viết prompt — tổng hợp từ 49 file vision (b01–b49)

Nguồn: 49 báo cáo quan sát khung hình, mã b01 đến b49 (quan sát bằng thị giác trên khung hình video, không phải suy luận trừ khi ghi rõ). Ký hiệu `[bNN t=...s]` chỉ mã báo cáo nguồn và mốc thời gian. Prompt được chép NGUYÊN VĂN, giữ nguyên ngôn ngữ gốc, không sửa chính tả của tác giả gốc; chỗ bị cắt trên màn hình ghi rõ "(bị cắt)".

---

## 1. THƯ VIỆN PROMPT NGUYÊN VĂN

### 1.1 Tạo nhân vật (character)

**Google Flow — nhân vật hiệp sĩ trung cổ** [b01 t=424.6s], công cụ: Google Flow (New Character), mục đích: tạo nhân vật hyperrealistic, kết quả: tạo thành công, dùng làm nhân vật xuyên suốt phần còn lại video.
> "tôi muốn bạn tạo ra một nhân vật siêu thực (hyperrealistic) về một hiệp sĩ thời trung cổ, hãy đảm bảo rằng khuôn mặt của anh ấy được nhìn thấy rõ ràng" (có thể bị cắt cuối câu)

**Google Flow — Edit Voice cho nhân vật hiệp sĩ** [b01 t=469s], công cụ: Google Flow (Edit Voice dialog).
> Name: "linh thời trung cổ"
> Voice Performance: "giọng nam lính thời trung cổ, khoảng 25 tuổi, có giọng Anh trầm từ thời trung cổ"

**Google Flow — nhân vật mẹ chồng (tiếng Việt thô)** [b12 t=227s], công cụ: Google Flow, bị cắt trên frame:
> "Tạo nhân vật mẹ chồng ở độ tuổi U60, mẹ chồng miền Bắc, hiện đại, mặc đồ san[g trọng nhưng mà khó tính]"

**Google Flow — cùng nhân vật, sau khi bấm nút "Format" (Flow tự viết lại tiếng Anh chi tiết)** [b12 t=236-240s], kết quả: ảnh chân dung chuyên nghiệp, đây là ví dụ mẫu rất tốt về cấu trúc prompt ảnh chân dung chuyên nghiệp (xem thêm mục 2):
> "Medium studio shot of a sophisticated 60-year-old Northern Vietnamese woman with a stern, authoritative expression. She has sharp, calculating eyes, a subtle frown reflecting a demanding personality, and elegantly styled dark hair in a classic short perm with a jade hairpin. She wears a luxurious high-collared charcoal silk velvet Ao Dai with intricate silver embroidery and a strand of premium pearls. Her posture is perfectly symmetrical, centered, and forward-facing. Captured with a Hasselblad H6D-100c and a 50mm lens. The skin is rendered with biological realism, featuring natural textures. Clamshell lighting with a bottom silver reflector creates a luminous glow. The composition is a head and shoulders shot with clear headroom, ensuring the character's full head is entirely within the frame and not cropped by the top border against a seamless, solid white background."

**Google Flow — mẫu prompt full-body triptych có sẵn (placeholder chuẩn của Flow, dùng làm khung tham khảo)** [b12 t=286-289s, b21 t=790s]:
> "Full-body triptych, three distinct views: front facing, 3/4 side view, and back view. High resolution, flat studio lighting, consistent anatomical proportions across all views, solid white background. [DESCRIBE BODY AND OUTFIT]"

**Google Flow — nhân vật con dâu** [b12 t=219-227s]:
> "Tạo hình một cô con dâu Việt Nam ở độ tuổi 26 tuổi, trang phục lịch sự, hiện đại, không mặc áo dài nhé. Trẻ đẹp, thông minh nhưng không quá hiền lành và không dễ bắt nạt"

**Google Flow — bối cảnh bếp (background)** [b12 t=209.9s, bị cắt]:
> "Tạo bối cảnh một ngôi nhà hiện đại ở Việt Nam, khu vực nhà bếp. trên bàn ăn cơm có đầy đủ món ăn như mo[n ăn Việt]"

**Google Flow — voice mẹ chồng, Customize Performance + Sample Dialogue** [b12 t=132.6s, t=147.6s], mẹo: mô tả rõ tuổi, giới tính, tính cách, sắc thái giọng bằng tiếng Việt:
> Customize Performance: "Giọng tiếng Việt 100% của một người mẹ tuổi 60 ở Việt Nam. Người mẹ khó tính, giọng nói sẽ hơi đanh đá, chua ngoa một chút. Nói tiếng Việt tự nhiên"
> Sample Dialogue: "À, cô thi giỏi rồi, nhà tôi thật vô phúc khi có đứa con dâu như cô"

**Claude → Google Flow — Character Reference Prompt "Linh" (semi-realistic illustration)** [b16 t=71s–f_0072], công cụ: Claude soạn, dán vào Google Flow Characters, mục đích: nhân vật xuyên suốt phim ngắn deepfake-awareness, đây là mẫu prompt character sheet rất đầy đủ (multi-view + art style):
> "...semi-realistic illustration style, stylized but emotionally expressive. Long straight black hair loosely tied or flowing. Soft oval face, natural makeup, warm brown eyes that convey curiosity and vulnerability. Wearing an oversized light gray t-shirt, casual home setting.
> Sitting on bed at night, face illuminated by cold blue smartphone glow from below, background is dark bedroom with a small bedside lamp.
> Art style: semi-realistic digital illustration, clean linework, subtle cel-shading, cinematic color grading — cool blue tones dominant with warm amber accent. Similar to modern webtoon or animated short film style.
> Full character reference sheet: front view, 3/4 view, close-up face expression (neutral → shocked → alert). White background panels."

**Google Flow — nhân vật mèo vàng Việt Nam** [b21 t=705s]:
> "Tạo nhân vật chú mèo vàng Việt Nam background là khu nông thôn"

**Google Flow — Character Info (mô tả tính cách để Agent giữ tính cách xuyên suốt)** [b21 t=782s]:
> "Mô tả tính cách nhân vật để khi nhân vật đi vào video sẽ có tính cách !!"

**Google Flow — chuyển nhân vật người thật sang 2D, giữ đặc điểm** [b21 t=805s], mẹo giữ nét nhận dạng khi đổi phong cách:
> "Tạo cho tôi phiên bản 2D của cô gái này, giữ nguyên đường nét gương mặt, tóc, trang phục, để nền trắng, high resolution . cô ấy không niềng răng nha" (chép đúng dấu cách thừa và dấu chấm)

**Google Flow Agent — voice mới cho video quảng cáo (giọng nam trầm)** [b23 t=340s, t=366s]:
> Name: "giọng nam trầm"
> Voice Performance: "tôi muốn nó là giọng nói có âm sắc trầm phù hợp với một người đàn ông gốc Phi từ 20 đến 30 tuổi"
> Character Info (optional): "nhân vật này bình tĩnh, điềm đạm và đĩnh đạc"

**Story Animator (Flow tool tự build) — mèo con nấu ăn (bối cảnh + hành động)** [b21 t=1026s, t=1354s]:
> "Hai bé cún nấu trứng rán hành" (KỊCH BẢN & LỜI BÌNH, lời bình = "None")
> AI tự sinh mô tả từng cảnh chi tiết (xem mục 1.7 Storyboard).

**Google Flow Agent — mèo nấu ăn (agent mode)** [b22 t=1354s]:
> "Tôi muốn tạo video AI mô tả bé mèo nấu ăn"
> "Cần biết là tạo món gì chứ nhỉ? nấu món hàu nướng mỡ hành đi"
> "Tạo video nấu cá om xì dầu"

### 1.2 Tạo ảnh (image generation, không phải nhân vật)

**Google Flow Agent — 3 ảnh cây theo 3 phong cách** [b01 t=178.6–201.5s], công cụ: Google Flow Agent, kết quả: thành công, 0 credit:
> "Tôi muốn bạn tạo ba hình ảnh khác nhau về một cái cây theo ba phong cách nghệ thuật: hình đầu tiên là phong cách 3D, hình thứ hai là phong cách anime 2D, và hình thứ ba là phong cách hoạt hình đất sét (claymation)"

**Google Flow — ghép nhân vật + trang phục (multi-image "ingredients")** [b01 t=140.9s], 3 ảnh đính kèm (chân dung + áo + quần):
> "Make this character wearing this outfit with a white background"

**Google Flow / KOL AI — ghép nhiều ảnh nguyên liệu (Ingredients-style), 5 ảnh đính kèm** [b20 t=549-553s]:
> "The girl in image 1 wearing exactly the tank top in image 2 and exactly pants in image 3, wearing exactly glasses in image 4. Place her in a suitable background with the outfit and posing exactly like image 5"

**MASTER IMAGE GENERATION PROMPT — style "Oversimplified/Casually Explained" (Claude soạn để tái sử dụng nhiều lần)** [b25 t=364s], công cụ: Claude, dùng được cho Midjourney/DALL-E/SD/Ideogram, mục đích: chuẩn hoá 1 style cố định cho toàn bộ loạt ảnh YouTube, có chỗ trống `[THÊM MÔ TẢ SCENE CỤ THỂ Ở ĐÂY]` để tái sử dụng — đây là mẫu KHUNG STYLE PROMPT rất đáng tham khảo:
> "A hand-drawn 2D flat illustration in the style of Oversimplified / Casually Explained YouTube channel. Stick figure character with a perfect white circle head, two simple round dot eyes, a thin straight or slightly curved mouth line, stick body and limbs with bold black outlines (2-3px). Flat colors with NO gradients, NO highlights, NO depth shading. ALL elements outlined in dark near-black (#1C1C1C). Background is a simple flat landscape scene: solid sky blue (#7ECFE0) top half, solid grass green (#5AB033) bottom half. Color palette: muted cartoon — sky blue, grass green, earthy brown, flat gray, white, sandy beige. Art style: naive flat cartoon, hand-drawn digital, deadpan humor aesthetic. Scene text in ALL CAPS handwritten bold font (Permanent Marker style), black, top-center of frame. 16:9 landscape format, widescreen YouTube thumbnail ratio. Clean simple composition, lots of negative space in sky area. NO photorealism, NO 3D rendering, NO anime style, NO Disney style. [THÊM MÔ TẢ SCENE CỤ THỂ Ở ĐÂY]"

**Perplexity → prompt định hình phong cách "Collage cutout documentary" (Vox style)** [b26 t=294s], mục đích: dùng làm style cố định cho video Nokia/kinh doanh dạng explainer, đây là ví dụ prompt-mô-tả-style bằng tiếng Việt rất chi tiết:
> "Tạo một video theo phong cách collage cutout documentary, giống một bài explainer hiện đại. Toàn bộ cảnh được dựng bằng các mảng ảnh cắt nền sạch, chồng lớp rõ ràng, có cảm giác thủ công như giấy cắt và scrapbook editorial. Giữ chủ thể tách biệt rõ khỏi background, dùng texture giấy nhẹ, mép cắt gọn nhưng có chút thô tự nhiên, bóng đổ mềm, và độ sâu bằng nhiều lớp foreground, midground, background. Chuyển động camera chậm và tinh tế, chủ yếu là pan, zoom, parallax, slight shake nhẹ kiểu documentary, không rung mạnh. Mỗi cảnh phải rõ ý, ít chi tiết thừa, ưu tiên khả năng đọc hình nhanh. Chèn text highlight, label, arrow, line, map callout hoặc annotation khi cần. Màu sắc tối giản, tương phản tốt, hơi editorial, có cảm giác báo chí, tài liệu, thông tin trực quan. Nhịp dựng ngắn, mạch lạc, thiên về storytelling, giống video giải thích của Vox."

**Simple Sketch (Flow tool) — quái vật màu xanh lá** [b35 t=169s, t=235s], công cụ: Simple Sketch (vẽ tay + prompt):
> "một con quái vật màu xanh lá cây trong rừng rậm, hình ảnh thực tế, mang tính điện ảnh, sự kết hợp giữa khủng long và sinh vật quái vật, nhưng có nét dễ thương, ảnh chụp thật" (sửa thêm sau: "...sinh vật này có các đốm màu đỏ")

**Simple Sketch — hộp trong suốt** [b01 t=618.4s]:
> "một chiếc hộp trong suốt"

**Claymation Studio (tool tự build) — prompt style mặc định do AI tự viết** [b02 t=852.9s], dùng làm mẫu tham khảo prompt chuyển ảnh sang claymation:
> "Chuyển đổi hình ảnh này sang phong cách hoạt hình claymation, chi tiết thủ công, kết cấu đất sét plasticine, ánh sáng studio stop-motion."

**Canva/ChatGPT — ảnh banner "ĐIỀU KHIỂN NÃO AI"** [b27 t=649s]:
> "Background gradient tím đậm sang xanh điện. Chữ in hoa bold màu trắng outline đen: ĐIỀU KHIỂN NÃO AI! bên trái chiếm 60% diện tích. Bên phải icon não người kết hợp circuit board phát sáng màu tím/xanh neon có hiệu ứng glow. Góc dưới trái text nhỏ Claude Opus 4.8 | nontech làm AI. Năng lượng cao màu sắc rực rỡ bắt mắt."

**Canva connector (qua Claude) — Instagram post Red Bull flavor launch** [b43 t=624s], dùng lại y nguyên trên cả Gemini và Canva AI trực tiếp:
> "@Canva Create an Instagram post for a Red Bull new flavor launch. Bold headline 'NEW FLAVOR' text, can centered, dark background, neon glow effects, 1:1 format - follow brandkit and add logo"

**Gemini (Canva) — Instagram post cà phê mới** [b43 t=722.8s]:
> "@Canva Create an Instagram post for a new coffee product launch. Include a bold title text 'NEW ARRIVAL', a short tagline below, soft warm lighting on the product, minimalist background, slight bokeh effect, square format 1:1"

**Google Flow Agent — poster đua xe cổ điển** [b41 t=307s], kèm lệnh xuất sang Canva:
> "A vintage European motorsport poster in the style of 1960s-1970s Italian and French Grand Prix art. A sleek Formula 1 or GT racing car — Ferrari red or cobalt blue — captured mid-corner at high speed, motion blur on the wheels, low camera angle. Background features an iconic European circuit: winding mountain road, cobblestone town, or coastal cliffside at golden hour. Bold retro typography with the race name in large sans-serif or slab-serif font, subtle grid lines and geometric shapes as decorative elements. Color palette: deep red, ivory, navy blue, gold, with a slightly faded, screen-printed texture. Cinematic, dramatic lighting. Poster format, vertical orientation. High detail, painterly illustration style blending realism with graphic design."
> Kèm dòng lệnh riêng: "Create on Canva and give me the canva link"

### 1.3 Tạo video (video generation từ text hoặc ảnh)

**UGCVideo.ai (Kling-3.0) — máy sấy tóc, thao tác + hành động chi tiết** [b03 t=310.3s, mở rộng t=313.5s], kết quả: tạo thành công, mẹo khoá chi tiết sản phẩm quan trọng:
> "A young Asian woman with long wavy black hair sits at a wooden vanity table in a bright, minimalist room. She is wearing a soft pink blouse and holding a pink Gaabor hair dryer close to her face. She gently tilts her head to the side and smiles warmly at the camera, then slowly lifts the hair dryer and runs it through her hair in a smooth, natural arc — her hair flowing softly in the warm air. She lowers the dryer slightly, glances at it with a satisfied expression, then brings it back up near her cheek, rotating her wrist slightly to show the rose-gold detail on the dryer nozzle. Natural morning light filters through sheer white curtains behind her. The movement is slow, graceful, and effortless. Skincare bottles and a potted green plant are softly blurred in the background. No text, no dialogue. Cinematic, warm-toned, lifestyle beauty aesthetic. Vertical 9:16 format."
> Bổ sung ràng buộc sản phẩm (rất quan trọng, chống méo chi tiết sản phẩm): "...Retain the details of the dryer, do not alter the product's appearance. Ensure 100% representation of the dryer."

**Google Flow — talking video có lời thoại (khoá toàn bộ yếu tố nhận dạng)** [b03 t=333.9s], đây là mẫu cấu trúc rất chuẩn cho "nhân vật nói theo lời thoại":
> "Tạo video mà nhân vật nói theo lời thoại dưới đây. Lời thoại: "Mình vừa tìm được một chiếc máy sấy tóc của Gaabor mà phải nói là nhìn đẹp hơn hẳn so với tầm giá." Ngôn ngữ nói: Tiếng Việt 100%. Nhân vật: Chính xác ở ảnh số 1 với giọng nói chính xác được đính kèm. Nhân vật chỉ nói, biểu cảm gương mặt và tay phù hợp, không có text hiển thị. Mắt nhìn thẳng vào camera. Không chuyển cảnh, giữ nguyên video chỉ là nhân vật nói. Giữ nguyên các yếu tố sau — mọi thứ giống chính xác như ảnh số 1: Hình dáng khuôn mặt / Tỷ lệ khuôn mặt / Kết cấu da / [bị cắt]"

**UGC Ad Video script (kiểu quảng cáo có hành động + thoại xen kẽ)** [b03 t=346.4-397.9s]:
> "Cô gái cầm máy sấy tóc Gaabor màu hồng, nhìn camera nói: "Ủa sao tóc mình mượt thế này?? Bí kíp là cái máy sấy Gaabor này nè! Nhỏ xíu mà mạnh cực kỳ, sấy cái vèo là khô luôn, không cần ngồi chờ như ngồi thiền nữa!" Cô bật máy lên, sấy tóc, mỉm cười tự nhiên. Zoom vào sản phẩm màu hồng dễ thương. Cô vuốt mái tóc bóng mượt, nói: "Màu hồng dễ thương, có nozzle tạo kiểu, giá mềm mà chất xịn. Chị em ơi mua đi đừng hỏi!" Thumbs-up tự tin vào camera. Ánh sáng ấm, phong cách UGC tự nhiên."

**Yêu cầu tự nhiên ngôn ngữ (người dùng nói với Claude, Claude tự viết script)** [b03 t=443.5-472.2s], mẫu câu lệnh ngắn gọn để agent tự động hoá:
> "Làm UGC cho sản phẩm máy sấy tóc Gabor, tôi sẽ tải ảnh đính lên, thông điệp Máy sấy tóc khô nhanh mà không bị xù tóc, tóc vẫn mềm mượt siêu thích, dùng character Thiên Hương Vũ, TikTok 9:16"

**Text/Voice-over-to-Video (Ingredients AI, dạng "Create a video base on the voice over")** [b20 t=169-333s, t=502-531s], công thức 2 phần: Voice Over + Note mô tả phong cách:
> "Create a video base on the voice over:
> Voice Over: I almost lost 100,000 miles and didn't even know it. KrisFlyer miles expire. 3 years no activity. Gone. I had 6 weeks left.
> Note: Realistic Video, show the shock and viral. Text animation with eye-catching in the middle"

**Frame-to-video tiếng Việt, chủ đề nha khoa (chuyển động mô tả bằng động từ)** [b20 t=531s]:
> "Chuyển động từ ảnh 1 sang ảnh 2 theo dạng xương bị tan biến và để lộ hàm nướu thối"

**Cinematic prompt chi tiết kèm ảnh nhân vật tham chiếu ("PERSON REFERENCE SHEET")** [b20 t=602-608s], mẫu prompt điện ảnh đầy đủ: hành động + camera + ánh sáng + âm thanh + thời lượng + tỉ lệ khung hình:
> "The disabled man lying prone on the wooden board on the gravel road — his one arm begins a slow, trembling drag forward. Each movement costs him enormously. Fingers scrape and bleed against rough stones. Body inches forward, shaking with exhaustion. Camera at ground level, slow tracking shot from the side. Harsh natural light, dust rising. Sound: scraping wood on gravel, labored breathing, distant wind. 6 seconds. Cinematic 9:16."

**UGC Video — animation video từ nhân vật 2D + voice-over, cấu trúc "No talk, only reaction"** [b21 t=828s, t=843s]:
> "Tạo video animation để mô tả nội dung hội thoại, nhân vật tương tác sẽ là cô gái trong ảnh 1.
> Voice Over:
> Nói đơn giản: Remotion là cách duy nhất để Claude thực sự tạo video thay mình, không phải chỉ gợi ý làm.
> No talk, only reaction and interaction. Show scense base on voice over . Logo Remotion ở image 2. Keep style 2D"

**Google Flow — hội thoại 3 người trong 1 khung hình (bản đầy đủ nhất, có khoá nhân vật + khoá bối cảnh + khoá lời thoại)** [b12 t=683-732s], đây là mẫu cấu trúc block hoá đầy đủ nhất trong toàn bộ kho dữ liệu để kiểm soát hội thoại nhiều nhân vật:
> "#Nhân vật: Mẹ chồng, con dâu, con trai như 3 nhân vật được đính kèm. Giữ nguyên trang phục, quần áo, tính chất gương mặt, tóc tai, độ dài tóc, tỷ lệ gương mặt.
> #Tạo một đoạn hội thoại giữa 3 người trong 1 khung hình lần lượt như sau:
> #Bối cảnh: 3 nhân vật đều đang ngồi vào bàn ăn cơm và chuẩn bị ăn cơm. Giữ nguyên bối cảnh như ở ảnh đính kèm 1
> #Lời thoại của các nhân vật: Mẹ chồng - bà Nga: "Tối muộn mới về, nhà cửa thì không chịu dọn, cô có coi cái nhà này là gia đình không?" Con dâu - chị Linh: "Mẹ, con ra ngoài là để đi làm kiếm tiền về nuôi cái nhà này mà mẹ"
> #Lưu ý: - Nói tiếng Việt 100%, nói tự nhiên, biểu đạt cảm xúc dựa trên lời nói tiếng Việt. Toàn bộ lời thoại cần đúng như nội dung ở trên. - Tuyệt đối không được nói sai lời thoại của nhân vật, ví dụ như nhân vật này nói lời thoại của nhân vật kia. Hãy kiểm soát tuyệt đối và thật chặt chẽ nhé!"

**Google Flow — video quảng cáo Skool (mô tả tình huống tự nhiên trong bối cảnh)** [b23 t=537s]:
> "tạo một video quảng cáo giới thiệu về trang skool của tôi được xuất hiện trong 1 chiếc máy tính xách tay một cách tự nhiên trong văn phòng tại nhà hiện đại, với nhân vật đang nói chuyện với máy quay về cách anh ấy có thể tiết kiệm nhiều thời gian và tiền bạc hơn bằng cách theo dõi trang skool này và nhận được những thông tin thú vị về AI mới nhất, hãy đảm bảo anh ấy cũng dễ dàng nhấp vào liên kết trong tiểu sử để biết thêm thông tin"

### 1.4 Tạo storyboard

**Gemini — vai trò đạo diễn phim (mở đầu quy trình storyboard)** [b06 t=62.5s]:
> "Tôi muốn bạn đóng vai trò như một đạo diễn phim truyện thật thụ, tôi sẽ đưa cho bạn kịch bản, tôi cần bạn xem, đọc, góp ý và đưa ra chi tiết lời thoại, bối cảnh"

**Google Docs — "SKILL: ĐẠO DIỄN NỘI DUNG & HỌA SĨ STORYBOARD (FULL WORKFLOW)"** [b06 t=7.2s, t=26.7s], cấu trúc skill mẫu, chia giai đoạn rõ ràng, ràng buộc thời lượng:
> "#1. Vai trò (Role)" / "#2. Quy trình làm việc (Workflow)" / "##GIAI ĐOẠN 1: Phát triển kịch bản (Scriptwriting)" gồm "Đầu vào", "Đầu ra", "Yêu cầu thời lượng & Lời bình (Strict Timing): Mỗi cảnh sẽ có thời lượng chuẩn là 10 giây. Lời bình (Voiceover) của mỗi cảnh phải được viết với độ dài từ 25 đến 35 từ để đảm bảo khớp thời gian đọc thực tế trong vòng tối đa 10s." và "Bảng kịch bản phải có các cột: Cảnh, Thời lượng (10s), Hình ảnh (Visual), Âm thanh (Audio), Voiceover chính xác theo từng nhân vật."

**Google Docs "Storyboard Image Animation Prompt" — prompt hệ thống dài để nối storyboard thành phim (Dạng 2: Có lời thoại)** [b06 t=38.7s, t=39.5-41.4s], đây là MẪU PROMPT HỆ THỐNG QUAN TRỌNG NHẤT cho tác vụ "storyboard → video liền mạch", gồm nhiều đoạn ràng buộc riêng biệt:
> "Tạo một chuỗi video điện ảnh từ tất cả các khung hình trong bảng phân cảnh, đồng thời duy trì sự nhất quán hoàn hảo của nhân vật trong mọi cảnh. Bạn cần phải giữ nguyên các đặc điểm khuôn mặt, kiểu tóc, trang phục, tỷ lệ cơ thể, tuổi tác và diện mạo tổng thể trong suốt video."
> "Hoạt họa từng khung hình trong bảng phân cảnh như một cảnh riêng biệt với chuyển động tự nhiên, tương tác môi trường thực tế và chuyển động máy quay mượt mà. Sử dụng các chuyển động máy quay điện ảnh nhẹ nhàng như lia máy chậm, quay theo dõi, lia máy tinh tế và thu phóng mềm mại. Đảm bảo tính liên tục và thu phóng mềm mại giữa các cảnh liên tiếp để mỗi cảnh chuyển tiếp tự nhiên sang cảnh tiếp theo."
> "Giữ nguyên phong cách hình ảnh trong ảnh tham chiếu (Web Cartoon), ánh sáng chất lượng cao, môi trường chi tiết, độ sâu trường ảnh mềm mại và hoạt họa nhân vật thực tế. Cây táo, phong cảnh xung quanh, điều kiện thời tiết và các yếu tố môi trường phải duy trì nhất quán về mặt hình ảnh trong suốt câu chuyện."
> "Tạo chuyển tiếp tự nhiên giữa các cảnh bằng cách sử dụng hiệu ứng mờ dần điện ảnh, cắt khớp, chuyển động môi trường hoặc chuyển động máy quay liên tục mượt mà. Tránh các đoạn cắt đột ngột, nháp nháy, thay đổi nhân vật hoặc sự không nhất quán về phong cách."
> "Lời thoại được nói bằng ngôn ngữ được viết trong storyboard. Ngôn ngữ lời thoại: Tiếng Anh."
> "Đồng bộ hóa thời gian lồng tiếng chính xác với các sự kiện xảy ra trong mỗi cảnh. Sử dụng giọng kể chuyện ở voice tham chiếu. Đảm bảo lời thoại hiển thị chính xác theo nội dung và ngôn ngữ đã có trên storyboard."
> "Đồng bộ hóa thời gian hiệu ứng âm thanh chính xác với các sự kiện xảy ra trong mỗi cảnh. Thêm các âm thanh môi trường tinh tế như tiếng chim hót, tiếng lá xào xạc, tiếng gió nhẹ, tiếng suối chảy xa, âm thanh thiên nhiên, tiếng mưa (nếu có) và tiếng côn trùng buổi tối trong các cảnh đêm. Các hiệu ứng âm thanh dựa theo tiết tấu và nội dung của storyboard."
> "Cuối cùng, biên tập tất cả các cảnh đã tạo thành một bộ phim điện ảnh chất lượng cao duy nhất với chuyển tiếp âm thanh liền mạch, hiệu chỉnh màu sắc nhất quán, chuyển cảnh mượt mà, lời kể được đồng bộ hóa, thiết kế âm thanh cân bằng và chất lượng kể chuyện chuyên nghiệp. Kết quả cuối cùng sẽ tạo cảm giác như một phim ngắn hoạt hình hoàn chỉnh chứ không phải là một tập hợp các đoạn phim riêng lẻ."

**Lệnh ngắn điều khiển từng cảnh storyboard (lặp lại nhiều lần)** [b06 t=37.6-89.1s]:
> "Tạo cảnh 1" / "Tạo cảnh 2" / "tôi cần bạn tạo ảnh storyboard cho cảnh số 2 theo hướng dẫn prompt đã đưa ra từ đầu" / "tạo ảnh storyboard số 12 nốt nhé"

**Claude → Google Flow — sửa lỗi hiểu nhầm "storyboard" (rất quan trọng, cạm bẫy phổ biến)** [b16 t=f_0090, f_0092]:
> "ko, tôi muốn storyboard chỉ cần như thế này, Tạo ảnh, chứ ko phải tạo video. tạo đúng 1 ảnh kèm các chú thích sản xuất và lời thoại"
> "không, tôi muốn bạn lên google flow chọn chế độ tạo để ảnh và tạo storyboard đó. ngoài ra thì tôi muốn câu lệnh prompt bạn tạo cần đảm bảo giữ đúng tính chất nhân vật, không được biến đổi. Nếu tạo ảnh hoặc video thì đều cần gắn dính kèm nhân vật character vào để đảm bảo độ chính xác tuyệt đối"

**Google Flow — prompt tạo 6-panel storyboard sheet** [b17 t=670s]:
> "Create a 6-panel storyboard sheet for VỊ CÀ PHÊ CỦA R[ừng]..." (bị cắt do khung code hẹp)

**Story Animator — mô tả từng cảnh do AI tự sinh (mẫu output storyboard chi tiết)** [b21 t=1055-1064s]:
> Cảnh 1: "Cận cảnh hai chú cún con (một Golden Retriever và một Corgi) mặc tạp dề đứng bếp nhỏ màu xanh và đỏ trong căn bếp gỗ"
> Cảnh 2: "bên cạnh đang dùng một chiếc dao đồ chơi nhựa để giả thái hành lá trên thớt gỗ. Cả hai vẫn mặc tạp dề như cảnh 1."
> Cảnh 3: "trứng vàng tươi và hành xanh hòa quyện vào nhau. Biểu cảm của hai chú cún rất tập trung và đáng yêu."
> (tiếp tục Cảnh 4-6, xem chi tiết trong báo cáo quan sát khung hình mã b21)

### 1.5 Tạo MV / âm nhạc

**Suno / OpenMusic — mô tả bài hát ban đầu (Song Description)** [b30 t=137-227s]:
> "Một bài hát catchy và trendy, nói về một cô gái mạnh mẽ dứt ra khỏi cuộc tình toxic và ngày càng hoàn thiện bản thân, dẫn đến thông điệp yêu bản thân trước khi yêu bất kỳ ai. Họ sẽ yêu bạn như cái cách bạn yêu bạn, Funk" (chữ "Funk" thêm cuối như tag thể loại)

**OpenMusic — yêu cầu viết lại lời (Tối ưu hóa)** [b30 t=?]:
> "Tôi muốn đoạn mở đầu catchy hơn, đánh thẳng vào thực tại nhiều cô gái nhìn người yêu mà hành xử, nhưng vẫn hát bay bổng hơn chứ ko như văn nói, làm cho nó hoa mỹ hơn với từ ngữ mỹ miêu hơn nhưng vẫn gần gũi và chân thành"

**Claude Project "Chuyên gia viết chuẩn hoá prompt" — hướng dẫn cấu trúc lời bài hát** [b30 t=381s], mẫu cấu trúc nhạc theo tag:
> Cấu trúc thẻ: `[Chorus]`, `[Bridge]`, `[Outro / Final Chorus]`; ghi chú "Cuối bài: ghi 1-2 dòng Production Note gợi ý cảm giác âm nhạc cho từng phần (tempo, energy level)."; `[TONE & STYLE]` mô tả cảm xúc tổng ("Tự tin, sáng khoái, có chút 'sass'...")

**Câu mẫu test giọng khi huấn luyện Voice AI** [b30]:
> "Từ nốt thấp nhất tôi có thể tìm thấy, lên tận bầu trời"

### 1.6 Landing page và infographic — ngoài phạm vi làm video, chỉ tham khảo cách viết prompt

Skill này không dùng để tạo landing page/web app hay infographic; hai ví dụ dưới đây giữ lại thuần tuý để tham khảo CÁCH VIẾT PROMPT (cấu trúc yêu cầu, mẹo HARD RULES, khung Persona/Context/Objective), không phải để dùng trực tiếp cho làm video.

**AI Studio (Gemini) — rebrand website mẫu bằng prompt có HARD RULES** [b37 t=356-419s], mẹo rút ra: quy tắc "HARD RULES: chỉ được đổi X, KHÔNG được đổi Y" là kỹ thuật chống AI "dọn dẹp" quá tay khi refactor giao diện có sẵn:
> "... HARD RULES: Do NOT remove, simplify, or slow any animation or interaction... change ONLY text, brand[ing]... background, and the accent color." (trích đoạn, bị cắt do cuộn)

**NotebookLM — infographic từ nội dung tài liệu, kèm mẫu câu gợi ý phong cách** [b40 t=251.3s, b29 t=319.1s]:
> "tu noi dung "Khoa hoc va Thuc hanh hoc Tung hung" tao cho toi 1 infographic, chu de anime nhe"
> Gợi ý phong cách chuẩn của Google: "Sử dụng chủ đề màu xanh dương và làm nổi bật 3 số liệu thống kê chính."

### 1.8 Sửa ảnh (image editing)

**Google Flow — chất liệu khối (image edit đơn giản)** [b01 t=64.4s]:
> "Change the cube to clear glass"

**Google Flow — thay nhân vật bằng ảnh chip đính kèm** [b01 t=84.4s]:
> "Change the character to [Model A]" (chip đính kèm ảnh)

**Google Flow — làm đẹp hơn (chỉnh nhẹ)** [b21 t=807s]:
> "làm cho cô gái xinh hơn chút"

**Canva (qua Claude) — xoá nút text đặt sai** [b32 t=369s]:
> "Xóa bỏ nút ở phía trên bên phải hiển thị chữ "Your Link here""

**Claude/Canva connector — chỉnh design_id có sẵn, mô tả ý định rõ ràng bằng field riêng** [b41 t=482s]:
> `design_id: "DAHLDMZzETc"`, `user_intent: "Edit text content and replace girl image with summer fashion image"`

### 1.9 Điều khiển camera (camera control chi tiết)

**Template "UNIVERSAL BUILD VIDEO PROMPT" — cấu trúc camera cố định + timelapse + ASMR audio** [b05 t=147-190s], đây là mẫu điều khiển camera CỰC KỲ chi tiết cho video kiến trúc/xây dựng dạng ASMR timelapse, có 2 loại camera block cố định và di chuyển:
> "EXACT OPENING FRAME: Camera: FIXED — mounted at 20 meters height, 15 meters from the giant tree, 0° horizontal tilt. [...]"
> "📷 Lens: 24mm FIXED 0° / 15m horizontal / 20m height | Color: [...] | Timelapse: 8x | ASMR Audio: Rotary hammer drill on hardwood — a powerful vibrating bore sound, [...]"
> "CAMERA CHANGES FOR THE FIRST TIME: The camera has dropped to the forest floor base of the tree trunk, 70° upward tilt. [...]"
> "DIRECT CONTINUATION: The camera swi[ngs] slowly to the left — moving from the below-trunk position to a left-side profile position: 1.8 meters height, 20 meters from..."
> Mẹo cấu trúc: mỗi Scene có cặp **START IMAGE PROMPT** và **FINISH IMAGE PROMPT** (2 ảnh/cảnh để Flow nối thành video, không phải 1 ảnh), và mỗi cảnh chia thành nhiều "SUB-FRAME A/B/C" nối tiếp nhau theo mốc thời gian (0:00-0:02, 0:02-0:04...).

**Google Flow — camera slow tilt trong storyboard-to-video cà phê** [b17 t=637-870s]:
> "Camera: slow upward tilt from tree roots to canopy, then to medium two-shot of the characters. Soft breeze moves the leaves gently."
> Biến thể khác cùng bộ nhân vật: "Camera: slow close-up of falling leaf → pan to dark fertile soil in CO TU's hand → wide shot of both characters in the lush coffee forest."

**Ingredients/cinematic — camera ground level tracking** [b20 t=602-608s]:
> "Camera at ground level, slow tracking shot from the side."

### 1.10 Prompt hệ thống / persona / meta-prompt (system prompt, prompt-engineering-prompt)

**NotebookLM Instructions — persona giáo viên lịch sử cho học sinh 16 tuổi** [b18 t=624-649s]:
> "Bạn là một giáo viên ảo dành cho học sinh trung học 16 tuổi. Hãy giải thích các nội dung một cách rõ ràng, hiện đại và lôi cuốn, sử dụng các ví dụ thực tế cùng ngôn từ đơn giản nhưng không được trẻ con. Các câu trả lời của bạn cần phải có tính tổ chức, súc tích và mang tính sư phạm, giúp khuyến khích sự tò mò, tư duy phản biện và việc học hỏi một cách thực chất."

**NotebookLM Custom instructions — "kỹ sư prompt chuyên gia" (chỉ dựa trên tài liệu chính thức, chống bịa đặt)** [b38 t=375.3-465.3s], đây là MẪU META-PROMPT (prompt để tạo prompt) rất đầy đủ, có cấu trúc ràng buộc đánh số và định dạng đầu ra cố định:
> "Hãy đóng vai là một kỹ sư prompt chuyên gia về các công cụ, API, mô hình AI và các nền tảng có tài liệu hướng dẫn chính thức. Nhiệm vụ của bạn là tạo ra các prompt được tối ưu hóa cao, mang tính kỹ thuật và đáng tin cậy, luôn dựa DUY NHẤT vào tài liệu chính thức được cung cấp trong các nguồn tài nguyên đã truyền tải.
> CÁC QUY TẮC BẮT BUỘC:
> 1. Trước khi tạo ra bất kỳ prompt nào, hãy tham khảo và phân tích kỹ lưỡng toàn bộ tài liệu kỹ thuật có sẵn.
> 2. Không bao giờ được tự bịa ra các tính năng, tham số, lệnh hoặc hành vi nào không được ghi chép rõ ràng trong tài liệu hướng dẫn.
> 3. Trong trường hợp có bất kỳ thông tin nào bị thiếu trong tài liệu hướng dẫn, hãy thông báo rõ ràng rằng thông tin đó không được ghi chép chính thức.
> 4. Luôn áp dụng các phương pháp hay nhất (best practices) được mô tả trong tài liệu chính thức.
> 5. Đối với mỗi prompt được tạo ra: giải thích những tham số nào đã sử dụng, tại sao phù hợp nhất, tác động kỳ vọng, và cảnh báo hạn chế đã ghi chép.
> 6. Cấu trúc từng câu trả lời theo định dạng: Mục tiêu của yêu cầu / Chiến lược được sử dụng / Các tham số đã chọn / Prompt cuối cùng đã tối ưu hóa.
> 7. Prompt cuối cùng phải: cực kỳ rõ ràng, có tính cụ thể cao, giảm thiểu sự mơ hồ, tối đa hóa chất lượng đầu ra, tuân thủ chính xác cú pháp đã được ghi chép, sẵn sàng để sử dụng ngay.
> 8. Không bao giờ sử dụng kiến thức từ suy diễn, kinh nghiệm cá nhân hoặc các giả định. Mọi câu trả lời phải được dựa trên cơ sở duy nhất là tài liệu kỹ thuật được cung cấp.
> 9. Khi có nhiều hơn một phương pháp tiếp cận khả thi trong tài liệu hướng dẫn: hãy so sánh các tuỳ chọn đó..." (bị cắt)

**NotebookLM — yêu cầu tạo prompt cho use case cụ thể (dùng khung 5 thành phần)** [b38 t=525.3s], kết quả trả về minh hoạ đúng khung **Persona / Context / Objective / Constraints / Few-shot**:
> Yêu cầu: "Hãy tạo một prompt để xây dựng một trợ lý AI có khả năng đảm nhận việc chấm bài kiểm tra môn Toán học cho học sinh năm thứ nhất của trường trung học phổ thông (lớp 10)."
> Kết quả 5 thành phần: Persona = "Chuyên gia Giáo viên Toán học cấp THPT"; Context = bài kiểm tra Toán lớp 10; Objective = phân tích, chấm điểm, phản hồi (dùng động từ hành động mạnh); Constraints = áp dụng Chain of Thought ("Hãy suy nghĩ từng bước một"), quy định đối tượng đọc, cấu trúc đầu ra rõ ràng (Điểm, Lỗi sai, Nhận xét); Few-shot = 1 cặp mẫu đầu vào-đầu ra chuẩn.

**Claude — Brand Kit Document prompt (tiếng Việt, dạng điền chỗ trống)** [b43 t=285s], mẫu prompt XÂY BỘ NHẬN DIỆN THƯƠNG HIỆU để tái sử dụng cho nhiều ảnh AI:
> "Tôi muốn bạn tạo một Brand Kit Document đầy đủ cho thương hiệu của tôi.
> Thông tin thương hiệu:
> - Tên thương hiệu: [tên] / - Ngành: [...] / - Đối tượng mục tiêu: [...] / - Giá trị thương hiệu: [...] / - Màu sắc chủ đạo: [hex code hoặc mô tả] / - Font chữ: [...] / - Phong cách hình ảnh: [...] / - Tone of voice: [...]
> Hãy tạo Brand Kit Document bao gồm:
> 1. Bảng màu chi tiết với hex codes và cách phối màu
> 2. Typography rules (font, size, weight cho từng loại nội dung)
> 3. Visual style guide (mô tả chi tiết kiểu ảnh phù hợp)
> 4. 5 câu mô tả phong cách hình ảnh — sẵn sàng để paste vào AI prompt
> 5. Những gì KHÔNG nên có trong ảnh thương hiệu
> 6. Ví dụ 3 prompt mẫu để tạo ảnh đồng nhất thương hiệu
> Format output dạng document rõ ràng, tôi sẽ lưu lại và dùng dài lâu."

### 1.11 Đóng gói quy trình thành Skill / automation (meta-workflow)

**Claude — yêu cầu tạo skill "automate-ugc-video" (rule cứng do người dùng tự đặt ra)** [b04 t=614.4s, t=621.0s]:
> "Trao đổi với tôi trước nhé, mình không muốn chọn asset lưu sẵn vì như thế mình phải thao tác. Mình muốn bạn tự mình tải lên hoặc fetch link. Mình sẽ gửi link hoặc ảnh, bạn có nhiệm vụ cần hỏi mình trước là hình thức mình muốn đưa.
> Ngoài ra vì có khá nhiều ngôn ngữ, nên prompt tạo bạn cần quán triệt là nói bằng ngôn ngữ nào do mình lựa chọn.
> Mình muốn bạn tạo thành 1 bộ skill, tên là automate ugc video để sau này mình đưa link hoặc ảnh sản phẩm cùng insight, bạn tự tạo content và chọn nhân vật phù hợp."

**Claude — yêu cầu workflow storyboard/video/MV end-to-end (4 giai đoạn nối tiếp)** [b16 t=f_0058-f_0060], mẫu prompt điều phối nhiều công cụ (Google Flow + Remotion) trong 1 lệnh:
> "Trao đổi với nhau nhé, tôi muốn bạn dựa trên skill tôi đưa dưới đây, input khi tôi đưa idea vào, bạn tự khai triển thành một câu chuyện ngắn tầm 30s, sau đó tạo prompt định hình nhân vật và bối cảnh liên quan => lên google flow, tạo project mới và tạo nhân vật.
> Sau đó quay trở lại claude, tiếp tục phân tích tạo idea storyboard rồi lại lên google flow tạo ảnh storyboard,
> xong quay lại claude, tạo prompt video từ storyboard và lên google flow tạo video hoàn chỉnh từ cái storyboard đó.
> Cuối cùng dùng remotion ghép toàn bộ video từ google flow bạn vừa làm, thành 1 câu chuyện hoàn chỉnh, cắt bớt các khoảng thừa, dừng quá lâu, chèn hiệu ứng phù hợp nếu cần
> skill dựa vào |" (bị cắt)

**Claude — mô tả insight yêu cầu ngắn, để Claude tự viết voice-over + tạo video vox-style mascot** [b08 t=237-252s]:
> "tốt, giờ tôi muốn như thế này. Tôi đưa cho bạn đoạn voice tiếng Việt, bạn nhận audio, phân tích timestamps, tạo 1 video với phong cách trên. Lưu ý mỗi cảnh chỉ được tối đa 5 - 10 giây. Không được quá dài. Cần có độ chuyển động liên tục. Giữa các phân cảnh thì thay đổi đa dạng kiểu hiển thị, ảnh video, text nguệch ngoạc xen kẽ. Hãy cho nhân vật sticker bay lung tung, chuyển động sinh động phù hợp với kịch bản được chứ"

**Claude Code — tạo LUT màu tuỳ chỉnh (.cube) từ mô tả cảm xúc** [b39 t=748.9s, t=753.3s]:
> "Tạo cho tôi 1 file .cube chỉnh màu sắc kiểu ma mị, chuyện ma bí ẩn"
> "đây là màu ảnh gốc, tôi cần màu ảnh rõ màu xanh lá cây hơn, sáng hơn, có chiều sâu hơn"

---

## 2. CẤU TRÚC PROMPT HIỆU QUẢ (rút ra từ các prompt thật ở trên)

Từ việc đối chiếu hàng chục prompt thật thành công (không bị lỗi, được người dùng chấp nhận) so với các prompt bị chê/phải sửa lại, có thể rút ra khung cấu trúc chung sau, theo đúng thứ tự các thành phần nên xuất hiện:

1. **Vai trò/Nhiệm vụ (Role/Task)** — câu mở đầu nói rõ AI phải LÀM GÌ, ở dạng động từ hành động ("Tạo...", "Create...", "Animate this storyboard into..."). Ví dụ `[b06 t=62.5s]` "đóng vai trò như một đạo diễn phim", `[b38]` "Hãy đóng vai là một kỹ sư prompt chuyên gia...".
2. **Chủ thể/Nhân vật (Subject)** — mô tả nhân vật chính, luôn ưu tiên gắn kèm ảnh tham chiếu thay vì chỉ mô tả chữ khi công cụ hỗ trợ (`[b01]` "Change the character to [Model A]" dùng chip ảnh; `[b17]` "IDENTICAL character design: CHAU (...) — do NOT change face, hair, outfit, or art style").
3. **Bối cảnh/Bố cục (Scene/Setting)** — địa điểm, thời gian, ánh sáng. Ví dụ `[b17]` "Camera: slow upward tilt from tree roots to canopy... Soft breeze moves the leaves gently."
4. **Hành động/Chuyển động (Action/Motion)** — mô tả tuần tự theo thời gian, dùng động từ cụ thể, tránh mô tả tĩnh. Ví dụ `[b20]` "his one arm begins a slow, trembling drag forward. Each movement costs him enormously."
5. **Lời thoại/Voice-over (Dialogue)** — nếu có, tách hẳn thành khối riêng có nhãn rõ ("Lời thoại:", "Voice Over:"), ghi rõ ngôn ngữ nói và độ dài giới hạn theo giây (`[b03]` "Lời thoại: ... Ngôn ngữ nói: Tiếng Việt 100%"; `[b06]` "mỗi cảnh 10 giây, voiceover 25-35 từ").
6. **Camera/Kỹ thuật quay (Camera)** — góc máy, lens, chuyển động máy quay, dùng thuật ngữ điện ảnh (pan, tilt, tracking shot, rack focus). Nên đặt SAU hành động, làm khối riêng có nhãn 📷/Camera: (`[b05]`).
7. **Phong cách hình ảnh/Art style (Style)** — mô tả chất liệu, bảng màu, ánh sáng, so sánh với phong cách nổi tiếng đã biết ("giống phim Shaun the Sheep", "giống Vox", "Oversimplified / Casually Explained"). Đặt gần cuối, có thể tách thành 1 câu cố định tái sử dụng nhiều lần cho toàn bộ dự án (`[b25]` MASTER PROMPT có style cố định + chỗ trống mô tả scene).
8. **Ràng buộc/Negative constraints (Restrictions)** — liệt kê rõ điều KHÔNG được làm, dùng từ khoá mạnh ("Do NOT", "Tuyệt đối không được", "CRITICAL", "HARD RULES"). Đây là kỹ thuật xuất hiện lặp lại nhiều nhất trong kho dữ liệu để chống lỗi nhân vật biến dạng, chống AI tự "dọn dẹp" quá tay khi sửa web có sẵn (`[b37]` mục 5 HARD RULES), chống lẫn lộn lời thoại giữa các nhân vật (`[b12]`).
9. **Định dạng đầu ra (Format/Aspect ratio/Length)** — tỉ lệ khung hình, thời lượng, định dạng file, luôn đặt ở cuối câu như một "tag" ngắn ("Vertical 9:16 format.", "6 seconds. Cinematic 9:16.", "16:9 landscape format").

Khung tổng quát (không phải mọi prompt đều cần đủ 9 mục, nhưng thứ tự trên là thứ tự xuất hiện phổ biến nhất trong các prompt thành công):
> [Vai trò/Nhiệm vụ] → [Chủ thể + ảnh tham chiếu] → [Bối cảnh] → [Hành động theo trình tự] → [Lời thoại (nếu có), tách khối riêng, ghi rõ ngôn ngữ] → [Camera] → [Phong cách hình ảnh] → [Ràng buộc/Negative constraints] → [Định dạng đầu ra]

Khung "5 thành phần chuyên nghiệp" cho prompt dạng trợ lý/persona (không phải ảnh/video), theo đúng thuật ngữ NotebookLM tự đưa ra `[b38 t=555-573s]`, dựa theo tiêu chuẩn Google Cloud được nhắc tới trong nguồn:
> **Persona** (vai trò) → **Context** (bối cảnh/đầu vào) → **Objective** (mục tiêu, dùng động từ hành động mạnh) → **Constraints** (định dạng & giới hạn, có thể yêu cầu Chain-of-Thought bằng câu "Hãy suy nghĩ từng bước một") → **Few-shot** (ví dụ mẫu đầu vào-đầu ra chuẩn)

Mẫu cấu trúc riêng cho prompt REBRAND/SỬA sản phẩm có sẵn (website, design template...), rút từ `[b37]`, `[b41]`:
> Đánh số từng mục cần sửa (1. BRAND, 2. HERO, 3. COPY, 4. COLOR...) → mục cuối cùng luôn là "HARD RULES" liệt kê rõ cái KHÔNG được đụng tới → nêu rõ chỉ đổi "text, branding, background, và accent color" chẳng hạn, để khoanh vùng phạm vi sửa.

Mẫu cấu trúc riêng cho prompt hội thoại nhiều nhân vật, rút từ `[b12]`:
> `#Nhân vật:` (khoá đặc điểm ngoại hình từng người, dẫn chiếu ảnh đính kèm) → `#Bối cảnh:` (khoá không gian, dẫn chiếu ảnh đính kèm) → `#Lời thoại của các nhân vật:` (từng dòng có tên nhân vật + câu thoại trong ngoặc kép) → `#Lưu ý:` (khoá ngôn ngữ 100%, cấm gán nhầm câu thoại giữa các nhân vật)

Mẫu cấu trúc "2 ảnh mỗi cảnh" cho công cụ ảnh-thành-video (Google Flow dạng Start/End), rút từ `[b05]`:
> Mỗi Scene = **START IMAGE PROMPT** (trạng thái đầu cảnh) + **FINISH IMAGE PROMPT** (trạng thái cuối cảnh) → Flow tự nội suy chuyển động giữa 2 ảnh. Bên trong mỗi ảnh lại có thể chia nhỏ theo "SUB-FRAME A/B/C" theo mốc giây, để mô tả chuyển động máy quay/hành động rất dài mà vẫn nhất quán logic thời gian.

---

## 3. XỬ LÝ NGÔN NGỮ

### 3.1 Viết prompt tiếng Việt, thoại không phải tiếng Anh

- **Luôn ghi rõ tường minh ngôn ngữ nói trong prompt**, không để mặc định — cụm chuẩn thấy lặp lại nhiều lần: "Ngôn ngữ nói: Tiếng Việt 100%." `[b03]`, "Nói tiếng Việt 100%, nói tự nhiên, biểu đạt cảm xúc dựa trên lời nói tiếng Việt." `[b12]`, "Giọng nói dùng tiếng Việt miền Bắc chuẩn, không lơ lớ, nói tự nhiên." `[b17]`.
- **Google Flow / Omni Flash các giọng có sẵn đều là giọng nước ngoài đọc tiếng Việt** nên bị lơ lớ, không tự nhiên — đây là hạn chế THẬT của công cụ, không phải do prompt viết sai `[b16 mục 7, b12 mục 6]`. Giải pháp 2 bước đã dùng thực tế: (1) tạo video KHÔNG lồng tiếng trong Flow, (2) lồng tiếng riêng bằng TTS tiếng Việt chuyên dụng (FPT AI, ElevenLabs) rồi ghép ở bước Remotion `[b16 t=f_0114]`.
- **UGCVideo.ai cũng gặp vấn đề tương tự**: nền tảng hợp thị trường tiếng Anh hơn, giọng tiếng Việt thiếu tự nhiên/cảm xúc `[b03 mục 7, chỉ nghe nói]`.
- **Cạm bẫy thao tác gõ tự động (agent/browser automation) làm MẤT DẤU tiếng Việt** khi dùng kiểu "type action" (giả lập gõ phím) — đây là lỗi kỹ thuật quan sát thực tế, không phải lỗi prompt `[b04 t=651.0s]`. Giải pháp đã áp dụng: đổi sang "inject prompt bằng JS" (chèn thẳng giá trị vào ô nhập) thay vì gõ từng ký tự.
- **Mẹo "kiểm soát tuyệt đối, thật chặt chẽ"**: khi có hội thoại nhiều nhân vật, phải ghi thêm câu ràng buộc rõ ràng chống AI gán nhầm lời thoại giữa các nhân vật: "Tuyệt đối không được nói sai lời thoại của nhân vật, ví dụ như nhân vật này nói lời thoại của nhân vật kia. Hãy kiểm soát tuyệt đối và thật chặt chẽ nhé!" `[b12 t=366.7-381.7s]`.
- **Nút "Format" của Google Flow**: gõ mô tả ngắn gọn tiếng Việt rồi bấm "Format" để Flow tự viết lại thành prompt tiếng Anh chi tiết, chuyên nghiệp hơn (kèm thông số máy ảnh, ánh sáng) — cách hay để không phải tự dịch tay `[b12 mục 7]`.
- **All Vietnamese text must have FULL diacritical marks**: khi yêu cầu chữ tiếng Việt hiển thị TRÊN màn hình (không phải lời thoại), phải ghi rõ ràng buộc giữ đủ dấu, vì AI có xu hướng bỏ dấu khi tự sinh chữ `[b17 t=637-870s]`.

### 3.2 Viết chữ hiển thị trên màn hình (on-screen text)

- Cần tách rõ 2 loại: (a) lời thoại nhân vật nói ra miệng, và (b) chữ overlay/caption hiển thị trên khung hình — 2 loại này có thể khác ngôn ngữ nhau và cần khai báo riêng.
- Prompt storyboard hệ thống của `[b06]` quy định: "Đảm bảo lời thoại hiển thị chính xác theo nội dung và ngôn ngữ đã có trên storyboard" — tức là chữ hiển thị PHẢI khớp với bảng kịch bản gốc, không để AI tự diễn giải lại.
- Với các trợ lý viết bài đăng (LinkedIn, YouTube script...), việc kèm hashtag, icon (✅, 🔗) và CTA cuối bài trực tiếp trong prompt kết quả giúp nội dung sẵn sàng đăng luôn, không cần biên tập thêm `[b27 t=532-562s]`.

### 3.3 Giọng đọc AI (TTS) bị "lơ lớ" và cách khắc phục

- Cú pháp tag cảm xúc trong ô Text-to-Speech: dùng ngoặc vuông `[Happy]`, `[chuckles]` chèn vào giữa câu để tạo sắc thái giọng `[b10 t=337s, t=339s]`.
- Cú pháp ngắt nghỉ kiểu ElevenLabs: thẻ `<break time="0.5s"/>` chèn vào script để tạo khoảng nghỉ khi đọc `[b46 Video2 mục 6]`.
- Cú pháp nhãn cảm xúc kiểu `{ }` thấy trong công cụ TTS khác: `{ lo lắng }Tối qua bạn ngủ không đủ giấc à?` `[b47 t=598.3s]`.
- Nên chọn đúng "Original Language" thay vì để Auto Detect nếu biết chắc ngôn ngữ nói, đỡ tốn token xác định ngôn ngữ `[b10 mục 7, chỉ nghe nói]`.
- Lip Sync: các cạm bẫy kỹ thuật làm giảm độ chính xác lipsync được chính UI liệt kê: nhiều khuôn mặt trong khung hình, đầu lắc nhiều, góc nghiêng che mặt, ánh sáng yếu/nhấp nháy, nói quá nhanh, video độ phân giải dưới 360px `[b10 t=684s]`.
- Timestamp tính theo tỷ lệ ký tự (character ratio) chỉ đạt độ chính xác 80-90%, dễ gây lệch caption ở đoạn dài; muốn 100% chính xác nên dùng Whisper local: `pip install openai-whisper` rồi `whisper "audio.mp3" --word_timestamps True --output_format json` `[b46 Video2 mục 6]`.

---

## 4. STYLE — danh sách phong cách theo từng công cụ (tên gọi chính xác công cụ dùng)

### 4.1 NotebookLM — Video Overview
Choose visual style (10 lựa chọn, cuộn ngang): **Auto-select, Custom, Classic, Whiteboard, Kawaii, Anime, Watercolor, Retro print, Heritage, Paper-craft** `[b34 t=139.2s]`.
Format: **Cinematic (New!), Explainer, Brief** `[b34 t=127.4s]`. Một bản khác (b38) chỉ thấy: Auto-select, Custom, Classic, Whiteboard, Kawaii, Anime (có thể cuộn thêm) `[b38 t=764.4s]`.

### 4.2 NotebookLM — Audio Overview
Format: **Deep Dive (mặc định), Brief, Critique, Debate** `[b34 t=169.2s]`. Length: **Short / Default / Long** `[b34]`.

### 4.3 NotebookLM — Infographic
Ghi nhận NHIỀU bộ style khác nhau xuất hiện ở các video khác nhau (khả năng do Google cập nhật/đổi tên qua thời gian, hoặc do giao diện Anh/Việt khác nhau — cần đối chiếu khi dùng thật):
- `[b29 t=319.1s]` (tiếng Việt): **Đất sét, Báo chí, Hướng dẫn, Lưới Bento, Gạch** (còn bị cuộn che, tác giả nói qua lời có tới "10 phong cách").
- `[b38 t=690.1s]` (tiếng Anh): **Auto-select, Kawaii, Clay, Sketch Note, Anime, Editorial** (có thể cuộn thêm).
- `[b40 t=194.6s]` (tiếng Việt): **Tự động chọn, Ghi chú phác thảo, Kawaii, Chuyên nghiệp, Có tính khoa học, Anime** (bị cắt mép).
- `[b45 t=122-152s]` (tiếng Anh): **Auto-select, Sketch Note, Kawaii, Professional, Scientific, Anime**.
Choose orientation: **Landscape / Portrait / Square**. Level of detail: **Concise / Standard / Detailed (nhãn "BETA")**.

### 4.4 Google Flow — Story Animator (tool tự build trong Explore Tools)
Dropdown "Phong cách": **Điện ảnh, Tả thực, Anime, Hoạt hình 3D, Tranh sơn dầu, Màu nước** `[b21 t=849s, t=1026s]`.

### 4.5 Google Flow — Storyboard Studio
Style: ít nhất 2 giá trị quan sát được: **Realistic** (mặc định trong modal Welcome) và **Claymation** `[b06 t=61.5-62.5s]`.

### 4.6 Google Flow — Explore Tools (danh mục "Image", tên chính xác từng tool cộng đồng/Google)
**Simple Sketch, Scene Explorer, Mockup, Image Editor, Shot Explorer, Mask Magic, Converge, Grid Architect, Shader Effects, Type Overlays, pixelBento, Poster Designer, Video Sketch, Transition Machine, Weirdcore, Video Resizer, Character X-Ray, Style Writer, Storyboard Studio, Prompt Tree, Story Sketch, Datamosh, 3D Model Visualizer, Scout360, Ribbit, Whisk, Pose Text, 3D Face Swap** `[b35 t=104-133s]`.

### 4.7 Google Flow — New Character (thẻ mẫu tính cách nhân vật)
**The Familiar, The Eccentric, The Wicked, The Fantastical** (b01); bản mở rộng 6 thẻ ở b06: **The Eccentric, The Professional, The Wildcard, The Familiar, The Wicked, The Fantastical**.

### 4.8 Google Flow — giọng nói mẫu (Base Voice)
**Callirrhoe** (Female, easy-going, mid pitch), **Charon** (Male, informative, lower pitch), **Despina** (Female, smooth, mid pitch), **Enceladus** (Male, breathy, lower pitch) `[b01 t=465-498.8s]`. Các giọng khác thấy tên riêng: Aoede, Achird Custom, Callirrhoe Custom, Achernar `[b06, b16]`. **Cảnh báo: viết đúng chính tả tuyệt đối** — API trả lỗi 400 nếu sai dù chỉ một ký tự trong tên giọng đọc.

### 4.9 Suno / OpenMusic — thể loại nhạc (chip chọn nhanh, giống nhau ở cả hai nền tảng)
**Country, Folk, Rock, Blues, Cổ điển, Disco, Funk** (+ nút "Thêm >" để mở rộng) `[b30 t=137s]`.

### 4.10 UGC Character (UGCVideo.ai) — Look Vibe
**90s Style, Casual Style, Glam Style, Gym Style, Office Style, Street Style, Y2K Style** `[b03 t=395s]` (một số tên bị cắt chữ trên UI gốc).

### 4.11 Claude/AI Studio — style ảnh minh hoạ do người dùng tự đặt tên trong Brand Kit
Không phải style cố định của công cụ mà là style thương hiệu tự định nghĩa theo khuôn Brand Kit Document (xem mục 1.10): ví dụ Red Bull = "Dark dramatic backgrounds, high-contrast lighting, action photography, motion blur, neon glow effects in red and yellow, wide-angle or low-angle shots" `[b43 t=268s]`.

---

## 5. CẠM BẪY KHI VIẾT PROMPT

### 5.1 Cách diễn đạt (dễ bị hiểu nhầm)
- **Từ "storyboard" bị AI/Flow hiểu nhầm thành "tạo nhiều clip video rời"** thay vì đúng ý người dùng là "1 ảnh lưới tĩnh chứa nhiều panel" — phải ép rõ chế độ ("chọn chế độ tạo ẢNH") và số lượng ("tạo đúng 1 ảnh") `[b16 t=f_0090-f_0092]`.
- **Không nói rõ "xuất file để tải về" thì AI có thể chỉ trả lời bằng link xem online**, không phải file tải thật — phải ghi tường minh "xuất trực tiếp thành file hoàn chỉnh để tải về", nêu rõ định dạng (PDF, .xlsx) `[b18 t=930-942s]`.
- **Câu mơ hồ như "Làm cái banner đẹp"** cho kết quả không kiểm soát được — nên nêu cụ thể kích thước, tông màu, phong cách, dòng chữ chính, vị trí logo `[b41 t=379-401s]`.
- **AI "không thể thấy màn hình" người dùng** khi thao tác qua API kết nối (ví dụ Canva connector) — không nên nói kiểu "làm như màu kia", "kiểu đó đó" mà phải mô tả rõ ý tưởng bằng chữ `[b41 t=390s]`.
- **Khai báo brand/style 1 lần ở đầu phiên làm việc** để AI nhớ và áp dụng nhất quán cho toàn bộ các lần tạo sau, không cần lặp lại mỗi lần `[b41 t=390s]`.

### 5.2 Xuống dòng (line breaks)
- **Không được xuống dòng khi gõ prompt cho Google Flow (qua agent tự động)** — nếu xuống dòng, hệ thống hiểu thành NHIỀU lệnh riêng biệt và tạo ra quá nhiều ảnh/video ngoài ý muốn. Đây là mẹo được host nhấn mạnh 2 lần trong `[b16 t=f_0100]` và lặp lại ở `[b17 Insight 3, t=867s]`: "Luôn yêu cầu Claude tạo prompt thành một đoạn văn liền mạch, không xuống dòng."
- Ngược lại, khi cần cấu trúc nhiều khối rõ ràng (nhân vật/bối cảnh/lời thoại/lưu ý), có thể dùng dấu `#` đầu dòng để đánh dấu từng khối trong CÙNG một đoạn không xuống dòng cứng `[b12 t=633.7-650.9s]`.

### 5.3 Độ dài (length)
- **Giới hạn ký tự khác nhau theo từng ô nhập của từng công cụ** — cần để ý số đếm hiển thị trực tiếp trên UI: UGC Character prompt tối đa 1000 ký tự; UGC Image tối đa 18000; UGC Video (Kling-3.0) tối đa 2500; UGC Ad Video script tối đa 2000; Sample Dialogue (Google Flow voice) tối đa 120 ký tự `[b03 mục 3]`.
- **Mỗi cảnh video AI nên giới hạn 5-10 giây, không quá dài**, để tránh giật/lag hoặc AI xử lý sai — rule này lặp lại ở nhiều nguồn độc lập: `[b08 t=237s]` "mỗi cảnh chỉ được tối đa 5-10 giây", `[b06]` "mỗi cảnh 10 giây, voiceover 25-35 từ", slide lỗi ở `[b22]` "Cắt xén câu thoại sao cho đủ tối đa 10s. Trung bình 2 dòng trong câu lệnh."
- **Nên test với đoạn ngắn (10-30 giây) trước khi làm video dài** — nếu lần đầu kết quả chưa đúng ý sẽ tốn ít công sửa hơn; xuất hiện lặp lại độc lập ở `[b26 t=59s]` và `[b46 Video2 Tip1, t=675s]`: "luôn test với script ngắn 30 giây trước, chạy ổn rồi mới làm video dài."

### 5.4 Từ bị hiểu nhầm / nhập nhằng
- **"Storyboard"** (xem 5.1) — nhập nhằng giữa ảnh tĩnh lưới panel và chuỗi video rời.
- **Model bị nhận diện sai qua transcript tự động**: "Claude" bị nhận thành "Clock" trong transcript VMEG `[b11 t=886s]`; "Gemini" bị nhận thành "Dream night" trong phụ đề tự động `[b44]` — chỉ là lỗi nhận diện giọng nói tự động, không phải nội dung thật, cần đối chiếu hình ảnh gốc để xác nhận tên đúng trước khi trích dẫn.
- **Tên nhân vật do AI gợi ý có thể không khớp với tên AI thực sự chọn khi generate** — ví dụ script gợi ý "Soren Mercer"/"Eamon Vance" nhưng UI thực tế chọn "Soren Kael" `[b04 mục 7]` — cần double-check tên nhân vật thực tế đã dùng, không tin hoàn toàn vào text mô tả.
- **Format hex màu trong bản rút gọn có thể lệch với hex màu gốc người dùng cung cấp** (`#FF0C49` gốc vs `#CC0000` trong bản tóm tắt AI tự tạo) `[b43 mục 7]` — luôn kiểm tra lại bảng màu cuối cùng, không mặc định AI giữ đúng hex đã cho.
- **Đọc số bằng giọng nói (dictation) có thể bị ghi thành chữ thay vì số**: "hai mươi phần trăm" thay vì "20%" `[b32 t=420s]` — cần kiểm tra lại nội dung trước khi gửi nếu dùng nhập liệu bằng giọng nói.
- Chữ tiếng Việt lỗi phông trong ví dụ minh hoạ (`"Vet tlin"`, `"Xiε chậo"`) minh hoạ vấn đề AI phát âm/hiển thị tiếng Việt không chuẩn khi không kiểm soát chặt ngôn ngữ `[b13 t=807s]`.

### 5.5 Ràng buộc chống biến dạng nhân vật/sản phẩm (constraint quan trọng nhất, xuất hiện lặp lại nhiều nguồn độc lập)
- Chống méo chi tiết sản phẩm: "Retain the details of the dryer, do not alter the product's appearance. Ensure 100% representation of the dryer." `[b03]`.
- Chống biến dạng nhân vật khi thêm cảnh mới: "Giữ nguyên trang phục, quần áo, tính chất gương mặt, tóc tai, độ dài tóc, tỷ lệ gương mặt" + "Giữ nguyên bối cảnh như ở ảnh đính kèm 1" `[b12]`.
- Chống nhân vật bị đổi hẳn diện mạo giữa các cảnh: "IDENTICAL character design: [...] — do NOT change face, hair, outfit, or art style." `[b17]`.
- Chống AI tự "dọn dẹp" quá tay khi sửa code/design có sẵn: khối "HARD RULES" liệt kê rõ CHỈ được đổi gì, còn lại giữ nguyên 100% `[b37]`.
- [Chỉ nghe nói, không thấy trực tiếp trên UI] Nhắc lại qua lời kể trong 2 nguồn độc lập: tóc nhân vật nữ có thể tự dài ra bất thường so với ảnh gốc nếu không khoá rõ ràng buộc `[b04 mục 7]`; nhân vật "không nhất quán" là lỗi phổ biến với người mới `[b22 mục 7]`.

### 5.6 Cạm bẫy khác liên quan trực tiếp đến việc viết prompt (không phải lỗi kỹ thuật hệ thống)
- Đưa ảnh sản phẩm nền trắng (hoặc tách nền trước) giúp AI dễ ghép hơn — mẹo lặp lại 2 lần độc lập `[b04 Tip1 t=809.2s]` và `[b26 t=787s]` ("lên pexels lấy background dạng giấy để có cảm giác thủ công").
- Với hội thoại nhiều nhân vật, nên đặt lời thoại của từng người trong ngoặc kép riêng biệt và gắn rõ tên nhân vật đứng trước, tránh việc AI ghép sai lời `[b12]`.
- Đối với prompt code/rebrand, nên đánh số từng mục thay đổi (1, 2, 3...) rồi chốt lại bằng khối ràng buộc cuối cùng, giúp AI dễ theo đúng phạm vi `[b37]`.
- Với brand kit / style cố định dùng nhiều lần, nên tạo 1 "khung mẫu có chỗ trống" (giống MASTER IMAGE GENERATION PROMPT ở mục 1.2) để đảm bảo tính nhất quán giữa nhiều lần tạo, thay vì viết lại từ đầu mỗi lần `[b25]`.
- Prompt phải luôn nêu rõ khi nào cần Chain-of-Thought ("Hãy suy nghĩ từng bước một") nếu muốn AI suy luận có cấu trúc trước khi trả lời, đặc biệt với tác vụ chấm điểm/phân tích `[b38]`.

---

## Ghi chú về nguồn và độ tin cậy
Toàn bộ nội dung trên trích từ 49 file quan sát khung hình (`b01`–`b49`), một số prompt bị cắt trên màn hình đã ghi rõ trong ngoặc; các nhận định gắn nhãn "[chỉ nghe nói, không thấy]" là lời tác giả nói qua phụ đề/voice-over, KHÔNG phải chữ hiển thị trực tiếp trên giao diện, được giữ nguyên nhãn cảnh báo khi trích dẫn lại ở trên. Danh sách style ở mục 4 có thể đã thay đổi theo thời điểm cập nhật của từng công cụ (đặc biệt NotebookLM Infographic thấy 4 bộ tên khác nhau ở 4 video khác nhau) — nên xác minh lại trực tiếp trên UI hiện tại trước khi đưa vào skill chính thức.
