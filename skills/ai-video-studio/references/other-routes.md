# Các đường sản xuất video khác Google Flow

Tài liệu này gom từ 49 báo cáo quan sát khung hình, mã b01 đến b49, chỉ ghi những điều các agent đã thực sự nhìn thấy trên màn hình trong video hướng dẫn. Nguồn ghi theo định dạng [bXX t=Ns]. Nhãn [chưa xác minh], [suy luận], [chỉ nghe nói, không thấy] được giữ nguyên từ dữ liệu gốc khi trích dẫn lại.

---

## 1. Claude Code / Claude Cowork kết hợp Remotion

Đây là đường có nhiều dữ liệu nhất, xuất hiện ở ít nhất 6 video: b08, b09, b25, b26, b39, b46 (chi tiết đầy đủ nhất), cùng một số đoạn liên quan ở b16, b17 (chỉ nhắc thoáng qua, không có chi tiết kỹ thuật).

### 1.1 Cấu trúc thư mục project

Từ Finder macOS, project "Elly Test" [b26 t=490s]:
```
Projects
├── Projects Elly
├── Scheduled
    ├── 2D Animation Video
    ├── CV-Generate-Sample
    ├── Demo_Beauty Box_Assistant
    ├── Elly Test          (đang chọn)
    │   ├── count_0_to_100000.srt
    │   ├── generate_sfx.py
    │   ├── generate_voice_ghost.py
    │   ├── generate_voice.py
    │   ├── node_modules
    │   ├── out
    │   ├── package-lock.json
    │   ├── package.json
    │   ├── public
    │   ├── remotion.config.js
    │   ├── src
    │   └── whisper_result.json
    ├── Forbidden Thing
    ├── MONEY IDEA
    └── Redbull
```
Trong thư mục `public` của "Elly Test" [b26 t=499s]: `3M for dental.jpg`, `3M logo.jpeg`, `audio.mp3`, `Dentsply...png`, `Flag_of_Germany.svg.webp`, `Flag_of_the...svg`, `img_nokia_phone.jpg` (447 KB, 2409x3614, độ phân giải 72x72), `ivoclar logo.jpeg`, `KaVo equipment.jpeg`, `kavo logo.jpeg`, `logos`, `Nobel Biocare logo.jpeg`, `nokia_audio.mp3`, `nokia_transcript.json`, `NontechlamAI.png`, `straumann logo.jpeg`, `thiết bị.jpeg`, `vietnam`.

Project "psych-video" [b46 t=575s]: `Projects > Forbidden Thing > psych-video > public` chứa `img_0.png` đến `img_14.png`, `Vid3_merged.mp3`, cùng `node_modules`, `package.json`, `remotion.config.ts`, `script.ts`, `src`, `tsconfig.json`, `Vid3_Audio1.mp3`, `Vid3_Audio2.mp3`.

Project "stick-figure-video" do Claude tự trình bày cấu trúc [b25 t=515s]:
```
stick-figure-video/
├── package.json
├── tsconfig.json
├── remotion.config.ts
├── setup.sh                (chạy cái này đầu tiên)
├── public/
│   └── audio.mp3            (cần copy file MP3 vào đây)
├── src/
│   ├── index.ts
│   ├── Root.tsx
│   ├── Video.tsx             (sequencing 9 scenes + audio)
│   ├── components/
│   │   ├── DrawPath.tsx      (core draw-on animation, stroke-dashoffset)
│   │   ├── DrawCircle.tsx
│   │   ├── StickFigure.tsx   (nhân vật tái sử dụng)
│   │   ├── Background.tsx
│   │   └── Caption.tsx
│   └── scenes/
│       ├── Scene1.tsx  (GEN Z)
│       ├── Scene2.tsx  (CURATING THE SELF)
│       ├── Scene3.tsx  (THE GAP)
│       ├── Scene4.tsx  (ONLINE vs OFFLINE)
│       ├── Scene5.tsx  (NO UNDO)
│       ├── Scene6.tsx  (NO DELETE)
│       ├── Scene7.tsx  (NO FILTER)
│       ├── Scene8.tsx  (ANXIETY)
│       └── Scene9.tsx  (WITHDRAWAL)
```
Panel Progress của Claude liệt kê file skill đã tạo [b25 t=207s]: `Instructions - CLAUDE.md`, `package.json`, `tsconfig.json`, `remotion.config.ts`, `setup.sh`, `DrawPath.tsx`, `DrawCircle.tsx`, `StickFigure.tsx`, `Background.tsx`, `Caption.tsx`, `Scene1.tsx`.

Ở project khác, Claude tạo `SpiderReactionFull.jsx` (440 dòng theo [b09 t=546s], 429 dòng theo cách ghi ở [b08 t=306s] cho file cùng loại `OctopusReactionFull.jsx`), sửa `Root.tsx`, xóa file cũ `Composition.tsx` vì không còn được import [b09 t=546s]. Ở b08 còn có `AntFarmReaction.jsx` (381 dòng) [b08 t=306-501s].

### 1.2 Lệnh terminal (chép nguyên văn)

Hướng dẫn từng bước [b25 t=521s]:
- `cd "/Users/nguyenngochai/Documents/Claude/Projects/2D Animation Video/stick-figure-vid..."`
- `bash setup.sh` (chỉ chạy một lần)
- `npm start` (mở Remotion Studio tại `http://localhost:3000`)
- `npm run render` (xuất `out/video.mp4`)

Từ b46 [b46 t=344-579s]:
- Cài Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
- Kiểm tra Node/npm: `node --version` (v20.0.0), `npm --version` (11.12.1) [b46 t=201s]
- Tạo project Remotion mới: `npx create-video@latest` [b46 t=365s]
- Chạy dev server: `cd "đường-dẫn-project" && npm start` rồi mở `http://localhost:3000` [b46 t=533s]
- Ghép audio bằng ffmpeg: `ffmpeg -i "concat:..."` [b46 t=579s]
- Cài và chạy Whisper: `pip install openai-whisper` rồi `whisper "audio.mp3" --word_timestamps True --output_format json` [b46 t=506s]

Sự cố terminal thực tế khi agent tự scaffold project [b09 t=518-546s]:
- Lệnh `cd` thất bại do tên thư mục có dấu tiếng Việt lệch chuẩn hóa Unicode NFC/NFD, phải chuyển dùng glob (`*`) thay vì gõ tên chính xác.
- CLI `create-video` từ chối tên thư mục có khoảng trắng và ký tự non-ASCII ("Test mới"), agent phải scaffold trong thư mục tạm rồi di chuyển nội dung qua.
- Lệnh `shopt` thất bại vì shell đang dùng là zsh chứ không phải bash.
- Cờ `--no-git` và `--no-tailwind` không có tác dụng đầy đủ, dự án vẫn tự sinh `.git`, `.gitignore`, `.prettierrc` và vẫn cài dependency tailwind.

### 1.3 Quy trình từng bước

Pipeline chung lặp lại ở nhiều video (b08, b09, b25, b26, b46):
1. Chuẩn bị audio hoặc script (thu giọng ElevenLabs hoặc script tiếng Việt có sẵn).
2. Đưa file audio và script cho Claude, yêu cầu dựng video theo phong cách cụ thể.
3. Claude chạy Whisper để lấy word timestamps chính xác.
4. Claude tự tìm và tải ảnh nền qua Pexels/Unsplash hoặc browse web trực tiếp qua Chrome extension.
5. Claude viết code Remotion (các file scene .jsx/.tsx), đăng ký vào Root.jsx/Root.tsx.
6. Mở Remotion Studio (localhost:3000 hoặc 3001) để preview.
7. Người dùng xem và feedback nhiều vòng (thường 3-5 vòng) để chỉnh style, animation, timing.
8. Render ra MP4/MOV bằng nút Render trong Remotion Studio hoặc lệnh `npm run render`.
9. Đóng gói toàn bộ quy trình thành "skill" để tái sử dụng.

Chi tiết b26 [b26 t=245-1023s]: tra "vox style" qua Perplexity, chọn phong cách "collage cutout", đưa style cho Claude Code, test với audio ngắn 10-15 giây (ElevenLabs TTS), Claude hỏi nguồn ảnh (Pexels/upload/khác), lấy Pexels API key, cài Claude Extension cho Chrome, Claude tự transcribe bằng Whisper và tìm ảnh Pexels trực tiếp qua browser, dựng scene theo phong cách Collage Cutout, qua 5 vòng feedback (background giấy, tách nền bo viền trắng, chữ catchy hơn, animation low-key, thêm SFX, icon tiền to hơn), rồi đóng gói thành skill gọi lại bằng `/vox-collage-video`.

Chi tiết b08 [b08 t=77-515s]: đưa 5 ảnh tham khảo phong cách mascot-reaction, Claude phân tích ra 5 đặc điểm lặp lại (mascot cố định góc khung, nền là footage thật, khung viền tay vẽ, chữ đậm comic, biểu cảm mascot đổi theo giọng đọc), yêu cầu bo viền đen quanh mascot, dựng video mẫu 10 giây dọc để test, hỏi tỉ lệ khung hình (Dọc 9:16 / Ngang 16:9 / Other) qua hộp thoại chọn, dựng video hoàn chỉnh 9 cảnh theo giọng đọc thật, qua 3 vòng feedback lỗi, đóng gói thành skill tên `linh-vat-video-vox-style`, rồi test skill với project thứ hai (kiến/rệp) và một project hoàn toàn trống bằng slash command.

Chi tiết b25 [b25 t=91-657s]: xem 3 kênh tham khảo phong cách vẽ (Zenn, Franz, Dinzo), Claude phân tích phong cách "STICK FIGURE EDUCATIONAL COMEDY" (tương đồng Oversimplified/Casually Explained/CGP Grey), tạo Master Image Generation Prompt cho Midjourney/DALL-E/Stable Diffusion/Ideogram, chọn kỹ thuật "draw-on animation" (SVG stroke-dashoffset), pipeline đề xuất ban đầu là Audio → Whisper transcribe → Scene split → SVG generation → Frame rendering PNG → FFmpeg ghép audio + frames = MP4, nhưng Whisper local gặp lỗi mạng nên chuyển hướng dùng skill Remotion thay thế.

Chi tiết b46 (Video 2) [b46 t=24-714s]: không dùng CapCut/Premiere kéo thả, bước tay duy nhất là đưa file audio cho Claude; Claude tự phân tích và tính timestamps; dùng Canva connector để sinh ảnh; Remotion render; cài ffmpeg/Homebrew/Node qua Terminal; tạo skill riêng "psych-video"; render video test 59 giây trước, sau đó video dài 7 phút 23 giây.

### 1.4 Đóng gói thành skill và gọi bằng slash command

- [b26 t=886-944s]: yêu cầu "phân tích lại phong cách... tạo bộ skill, sau này tôi chỉ đưa audio và script thôi". Skill lưu tại menu Claude Code > Skills, gọi lại bằng `/vox-collage-video`.
- [b08 t=401-511s]: yêu cầu "pack giúp mình lại thành bộ skill nhé. Tên skill là linh vật - video - vox style". Skill lưu tên `linh-vat-video-vox-style` (thẻ hiển thị Settings > Customize > Skills, dòng phụ "by You"). Gọi lại bằng slash command kèm nội dung: `/linh-vat-video-vox-style [kịch bản voice-over]`.
- [b25 t=207-643s]: Claude tạo `SKILL.md`, gặp lỗi "SKILL.md must start with YAML frontmatter (---)"; sau khi thêm YAML frontmatter thì nút "Save skill" hoạt động. Skill lưu tên `2d-cartoon-basic`, hiển thị trong Context > Skills.
- [b46 t=473-506s]: Skill `psych-video` trong mục "Personal skills", ghi "Added by You", "Last updated Jun 7 2026", Trigger "Slash command + auto", mô tả "Tạo documentary video xã hội học/tâm lý học từ audio + script. Tự động tính word timestamps, gen ảnh Canva, download, cập nhật Remotion project." Các skill cá nhân khác cùng hiển thị: `dental-trip-script`, `blind-spot-youtube`, `psych-video`, `brand-guidelines`, `canvas-design`, `mcp-builder`, `skill-creator`. Skill có sẵn: `schedule`, `setup-cowork`, `context`.

### 1.5 Lỗi thực tế đã gặp và cách sửa

- [b26 t=622s] Preview Remotion màn đen kèm dòng đỏ: `"Composition with ID NokiaCollapse not found."` Nguyên nhân ghi trong log: cache hot-reload cũ vẫn dính tham chiếu đã xóa. Cách sửa: khởi động lại server Remotion Studio để lấy bundle mới.
- [b26 t=445s] `"Failed to verify final rendered video duration"` (dòng đỏ) — lỗi nhỏ khi verify, không chặn tiến trình.
- [b08 t=379s] Khung lỗi đỏ trong preview Remotion Studio: `"ReferenceError"` và `"Sfx is not defined"`. Nguyên nhân: file âm thanh đặt tên không khớp code gọi (code gọi `boing.wav` nhưng file thực tế tên `sfx_boing.wav`; log Claude: "Found it — files are named sfx_boing.wav not boing.wav. Fixing the path template."). Người dùng chọn bỏ hẳn SFX thay vì debug tiếp: "thôi bỏ các hiệu ứng âm thanh đi nhé, ko cần hiệu ứng âm thanh nữa".
- [b08] Claude tự ghi vào skill bài học: `OffthreadVideo` bị đứng hình khi phát trực tiếp trong Remotion Studio dù render cuối vẫn đúng, nên dùng `OffthreadVideo` cho bản render cuối và dùng `Video` cho preview trực tiếp.
- [b09 t=546s] `"Failed to write Root.tsx"` (dòng đỏ) ở lần ghi đầu tiên; Claude đọc lại file rồi ghi lại thành công (+10 -2 dòng).
- [b09 t=518-522s] CLI hỏi tương tác (interactive TUI) không nhận input qua pipe (`echo "n" | command`) do dùng raw mode, phải tìm flag tường minh qua `create-video --help`.
- [b25 t=463s] `"Network bị giới hạn nên không download được model"` khi chạy Whisper transcribe local, buộc chuyển hướng dùng skill Remotion thay vì tự build bằng Python + FFmpeg.
- [b39 t=369.2s] `"Failed to render final transparent video with explicit yuva444p10le pixel format"` và `"Background shell failed: Render final transparent video with explicit yuva444p10le..."`. Claude tự chẩn đoán nguyên nhân: "Remotion không tự bật kênh alpha cho ProRes 4444 nếu không đủ cờ --pixel-format=yuva444p10le và --image-format=png cùng lúc, thiếu 1 trong 2 là nó âm thầm xuất ra nền đặc." Sau khi sửa, pixel format thực tế đo được là `yuva444p12le`, kết quả "Đã xuất xong, nền trong suốt hoạt động đúng. ✅".
- [b39 t=529.3s, suy luận] Chạy script Python xử lý dữ liệu bản đồ (d3-geo/world-atlas) ở ngoài thư mục dự án sẽ không tìm thấy node_modules, phải di chuyển script vào trong thư mục dự án Remotion mới chạy được.
- [b46 t=714s] Lỗi caption lệch giọng đọc từ phút thứ 3 trở đi. Claude tự nhận lỗi: "Audio có đọc cả tiêu đề ở đầu... nhưng tôi bỏ sót phần này khi tính timestamps", rồi fix lại toàn bộ.
- [b08 t=213s] Cạm bẫy quan trọng: dán ảnh trực tiếp vào khung chat Claude Code không tạo ra file thật trên máy. Claude tự báo: "không có tool nào để trích xuất chúng thành file thật trên máy (đã kiểm tra /tmp, Downloads, cache paste, không có file nào khớp)".

### 1.6 Con số thật (không làm tròn)

- [b26 t=622s] Render lần 1: `out/nokia_collapse.mp4 (3.7MB, 15s, 1920x1080)`.
- [b26 t=638s] Render sau khi thêm texture giấy: `out/nokia_collapse.mp4 (11.4MB, 15s, 1920x1080)`.
- [b26 t=354s] Audio test dài 14.3 giây.
- [b08 t=216s] Canvas video mẫu đầu: 1080x1920 (dọc). [b08 t=269s] Canvas chốt cho video chính: 1920x1080 (ngang).
- [b08 t=306-322s] Video hoàn chỉnh 9 cảnh, mỗi cảnh 3.8-8.4 giây, không cảnh nào vượt 10 giây, tổng thời lượng khoảng 50 giây.
- [b08 t=437s] Video thứ hai: audio dài 40 giây; clip kiến từ Pexels dài 20 giây, mã hóa lại 1920x1080 ở 30fps.
- [b09 t=546s] Hai ảnh gốc 2823x3764 và 3376x4220 pixel, downscale còn khoảng 1920px chiều ngang.
- [b25 t=0s] Composition StickFigureVideo: độ phân giải 1280x720, 30 FPS, Duration 00:42:27; FPS thực tế dao động 29.9-31.7.
- [b25 t=490s] Bộ skill nhân vật: 5 hat x 5 outfit x 6 emotion = 150 tổ hợp.
- [b39 t=356.9s] Composition MicrosoftLayoffs: canvas 1920x1080, 450 khung hình = 15 giây.
- [b39 t=372.8s] File xuất: `out/microsoft-layoffs.mov (1920x1080, 15s, ProRes 4444, ~274MB)`, pixel format cuối `yuva444p12le`.
- [b46 t=490-501s] Skill psych-video: font Montserrat 300 (body) + 600 (current word); caption 1 dòng giữa dưới 64px, word-by-word sync; Ken Burns zoom 1.0 đến 1.08 kèm pan nhẹ; scrim gradient đen 38%; fade 10 frame đầu/cuối mỗi segment.
- [b46 t=615s] Video test: 1080x1920, 59 giây. [b46 t=705s] Composition PsychVideo: 1920x1080, 30 FPS, thời lượng 07:23.11.
- [b46 t=645s] Vid2_Audio1.mp3 dài 331.65s, Vid2_Audio2.mp3 dài 132.52s, Total merged 464.17s.

### 1.7 Ghi chú độ tin cậy

- [b26 t=16s, chỉ nghe nói, không thấy hình minh hoạ cụ thể]: lời dẫn nói không cần model AI đắt tiền, không cần RunwayML/Kaiber/Pika, chỉ cần Claude Code + Remotion.
- [b26 t=59s, chỉ nghe nói]: tác giả nói mất khoảng 1 tiếng để ra bản vừa ý sau nhiều vòng chỉnh sửa.
- [b16, b17, chỉ liên quan gián tiếp]: hai file này ghi nhận bước cuối cùng của pipeline "Claude → Google Flow → Claude → Google Flow → Claude → Google Flow → Remotion" có dùng Remotion để ghép clip Flow thành video hoàn chỉnh, nhưng không có chi tiết kỹ thuật cụ thể về code/lệnh Remotion trong hai file này.

---

## 2. NotebookLM (nay đổi tên thành Gemini Notebook)

Nguồn chính: b14, b15, b18, b19, b29, b34, b36, b38, b40, b41, b42, b45, b48, b49 (b31, b33, b43 hầu như không có nội dung liên quan, chỉ trích phần hiếm hoi có liên quan).

Xác nhận đổi tên chính thức: blog.google ngày 16 tháng 7 năm 2026, tác giả Josh Woodward (Phó chủ tịch Google Labs, Gemini app & AI Studio): "NotebookLM nay đã đổi tên thành Gemini Notebook." Bài blog ghi NotebookLM ra mắt tại Google I/O 2023 với tên "Dự án Tailwind", hiện có "hơn 30 triệu người và hơn 600.000 tổ chức" đang sử dụng [b41 t=15-83s].

### 2.1 9 loại đầu ra của Studio (Phòng thu)

Bản tiếng Anh (lặp lại nhất quán): "Audio Overview, Slide Deck, Video Overview, Mind Map, Reports, Flashcards, Quiz, Infographic, Data Table" [b14 t=96-112s], [b18 t=537-566s], [b34 t=180.9s, t=194.2s], [b48 t=176s].

Bản Việt hoá (tên gọi có khác biệt nhỏ giữa các phiên bản UI): "Tổng quan âm thanh, Slide Deck/Bản trình bày, Tổng quan video, Sơ đồ tư duy/Bản đồ tư duy, Báo cáo, Thẻ học từ vựng/Thẻ ghi nhớ, Trắc nghiệm/Bài kiểm tra, Infographic/Bản đồ hoạ thông tin, Bảng dữ liệu" [b18 t=118.4s], [b36 t=40s], [b40 t=66.1s, t=203.8s], [b49 t=90s].

Bố cục 3 cột chuẩn: "Sources" (Nguồn) / "Chat" (Trò chuyện) / "Studio" (Phòng thu), xác nhận ở [b18 t=537s], [b38 t=176.6s], [b40 t=66.1s], [b45 t=74s], [b48 t=176s]. Panel Studio có thêm nút "Add note" / "+ Thêm ghi chú" cuối lưới 9 thẻ, và bản NotebookLM đầy đủ còn có nút "Export" [b48 t=176s].

### 2.2 Tùy chọn khi tạo Video Overview

Hộp thoại "Customize Video Overview":
- Format: thay đổi theo thời gian ghi hình. Ở [b34 t=127.4s, t=139.2s]: 3 thẻ Cinematic (nhãn "New!"), Explainer, Brief. Ở bản mới hơn [b45 t=77s, t=107s]: 3 thẻ Cinematic, Explainer, Short (nhãn "New!").
- Mục "What should the video focus on?" luôn có 3 thẻ gợi ý chủ đề có sẵn cộng khung "Custom topic" (placeholder "Describe your own"), nút "Generate" màu xanh [b45 t=77s].
- Choose visual style (carousel cuộn ngang, số lượng hiện cùng lúc khác nhau do cuộn/cắt khung hình): Auto-select, Custom, Classic, Whiteboard, Kawaii, Anime, Watercolor, Retro print, Heritage, Paper-craft [b34 t=139.2s, t=249.4s, t=253.5s]. Bản Việt tương ứng: "Tự động chọn, Tuỳ chỉnh, Cổ điển, Bảng trắng, Kawaii, Hoạt hì..." (chữ bị cắt) [b36 t=52s].
- Choose language: dropdown, mặc định English [b34 t=139.2s].
- Ô mô tả tuỳ chỉnh có 2 placeholder mẫu: "Hãy thử phong cách giống như trong truyện: 'Hình minh hoạ trong sách truyện thiếu nhi'" và "Bạn nên thử: nhắm đến trường hợp sử dụng cụ thể... tập trung vào nguồn cụ thể..." [b36 t=52s].
- Trong lúc xử lý, Studio hiện dòng "Generating Video Overview... / Generating Short Video Overview... This may take a while" [b45 t=137s, t=179s].
- Kết quả có trình phát tích hợp: thanh thời gian, tốc độ "1x", tua lùi/tiến, play/pause, phóng to, và 2 nút phản hồi "Good video"/"Bad video" (bản Việt "Video hay"/"Video tệ") [b34 t=194.2s, t=228.1s], [b36 t=255.7s], [b45 t=167s].
- Nhãn nguồn kèm kết quả: "Based on N source(s)", ví dụ "Based on 1 source" [b36 t=247.6s, t=255.7s].

Audio Overview (bối cảnh liên quan, cùng bộ dialog): Format có Deep Dive (mặc định), Brief, Critique, Debate; Length có Short/Default/Long [b34 t=169.2s].

### 2.3 Tùy chọn khi tạo Infographic

Hộp thoại "Customize Infographic":
- Choose language / Chọn ngôn ngữ: dropdown [b29 t=315.6s], [b38 t=690.1s], [b45 t=13.5s, t=122s, t=182s].
- Choose orientation / Chọn hướng: Landscape/Khổ ngang, Portrait/Khổ dọc, Square/Hình vuông [b29 t=315.6s], [b38 t=690.1s], [b45 t=13.5s, t=122s].
- Choose visual style (carousel, số lượng khác nhau tuỳ frame): bản Việt [b29 t=315.6s, t=319.1s] thấy Đất sét, Báo chí, Hướng dẫn, Lưới Bento, Gạch (đang chọn Gạch); bản Anh [b38 t=690.1s] thấy Auto-select, Kawaii, Clay, Sketch Note, Anime, Editorial; bản khác [b45 t=13.5s, t=122s, t=182s] thấy Auto-select, Sketch Note, Kawaii, Professional, Scientific, Anime.
- Level of detail / Mức độ chi tiết: Concise/Ngắn gọn, Standard/Tiêu chuẩn (mặc định), Detailed/Chi tiết (luôn gắn nhãn "BETA") [b29 t=315.6s], [b38 t=690.1s], [b45 t=13.5s, t=122s].
- Khung mô tả tự do: "Describe the infographic you want to create", placeholder ví dụ "Guide the style, color, or focus: 'Use a blue color theme and highlight the 3 key stats.'" [b45 t=122s].
- Kết quả xem trong popup phóng to có nút chia sẻ, resize, đóng, 2 nút đánh giá "Good content"/"Bad content", link "View prompt and N sources" [b38 t=712.5-755.97s], [b40 t=82.7s].
- Cạm bẫy quan trọng: infographic tạo trong NotebookLM không chỉnh sửa trực tiếp được, phải tải ảnh rồi đưa vào Canva (dùng Magic Layers, Edit image) để tách lớp và chỉnh từng phần [b45, video "nl8hU9YUauk", t=364.5-493.7s]. Có lỗi chính tả thực tế trên infographic do NotebookLM sinh ra: tiêu đề thiếu từ "Đưa" trong "Artemis II: Bước Tiến Lịch Sử [Đưa] Con Người Trở Lại Mặt Trăng", cột "HUY" bị cắt chữ đáng lẽ là "ĐỘI CHỈ HUY" [b45 t=486.7-490.5s].

### 2.4 Giới hạn số nguồn (sources)

Không quan sát thấy thông báo giới hạn cứng kiểu "tối đa X sources" trên giao diện trong toàn bộ 18 file đã đọc. Con số sources lớn nhất quan sát được là notebook "Kịch Bản AI" với 285 sources, không kèm cảnh báo giới hạn [b18 t=117s]. Các notebook mẫu Google Featured khác có 62, 39, 36, 46, 70, 31, 152 sources [b41 t=31s], [b45 t=68s], [b48]. Hộp thoại thêm nguồn "Website and YouTube URLs" chỉ ghi giới hạn về NỘI DUNG chứ không phải số lượng, nguyên văn giống hệt ở 2 file [b48 t=179-182s] và [b18 t=145-180s], [b38 t=196.1s]:
> "To add multiple URLs, separate with a space or new line."
> "Only the visible text on the website will be imported at this time."
> "Paid articles are not supported."
> "Only the text transcript in YouTube will be imported at this time."
> "Only public YouTube videos are supported."
> "Recently uploaded videos may not be available to import."
> "If upload fails, learn more for common reasons."

Ô dán "Copied text" giới hạn 300 ký tự, hiện "1/300" [b36 t=373.2s] (đây là giới hạn độ dài văn bản dán, không phải giới hạn số sources). Kết luận: không có bằng chứng màn hình về một con số trần cụ thể cho tổng số sources mỗi notebook.

### 2.5 Giới hạn số video tạo mỗi ngày

- [b34 t=224.4s, chỉ nghe nói/AI tự khai trong khung chat, KHÔNG phải thông báo hệ thống chính thức, độ tin cậy thấp]: nội dung ghi "tạo 1 video Cinematic mất khoảng 15-20 phút, Google giới hạn tối đa 20 video Cinematic mỗi ngày cho mỗi tài khoản gói Pro và Ultra".
- [b40, video "So Sánh NotebookLM vs Gemini", t=432.8s]: sau khi tạo video xuất hiện thông báo "Bạn có thể tạo thêm 2 video nữa trong ngày hôm nay." Thông báo này xuất hiện ở phần Gemini (tạo video bằng Veo), không rõ có phải giới hạn của NotebookLM Video Overview hay không [chưa xác minh thuộc tính năng nào].
- Không tìm thấy thông báo giới hạn video/ngày nào khác trực tiếp trên giao diện chính thức Studio > Video Overview.

### 2.6 Lỗi thực tế và quy trình thao tác

Lỗi chép nguyên văn:
- "NotebookLM can't answer this question. Try rephrasing it, or ask a different question." — xảy ra khi gõ trực tiếp yêu cầu tạo infographic vào khung chat thay vì dùng nút chức năng riêng trong Studio [b45, video "lpAWQgeE90Q", t=209s]. Cạm bẫy: phải dùng đúng nút chức năng trong panel Studio, gõ trong chat không hoạt động.
- "Couldn't connect / Reload" — lỗi kết nối tạm thời ở sidebar Gemini [b18 t=649s].
- Khi yêu cầu Gemini xuất file PDF/Excel, lần đầu chỉ nhận link xem trực tuyến thay vì file tải về thật; Gemini tự nhận lỗi: "Thầy xin lỗi em vì sự nhầm lẫn ở lượt phản hồi trước khi chỉ cung cấp các liên kết xem trực tuyến." [b18 t=942s]. Phải yêu cầu lại rõ ràng mới ra file thật.
- Cảnh báo cố định cuối câu trả lời: "NotebookLM có thể đưa ra thông tin không chính xác, hãy kiểm tra kỹ câu trả lời mà bạn nhận được." (bản Việt) [b36 t=40s]; "NotebookLM can be inaccurate; please double check its responses." (bản Anh) [b48 t=176s].

Quy trình tạo notebook mới và thêm nguồn [tổng hợp b41 t=31-138s, b48 t=139-198s, b45 t=68-107s]:
1. Bấm "+ Create new" / "+ Tạo số ghi chú".
2. Màn hình loading "Creating your notebook..." (URL đổi thành notebooklm.google.com/notebook/creating).
3. Notebook trống hiện ra, nút "+ Add sources" hoặc khung "Create Audio and Video Overviews from your documents" với 4 nút Upload files, Websites, Drive, Copied text.
4. Nếu chọn Websites: hộp thoại "Website and YouTube URLs", dán link, bấm "Insert" (chỉ active khi có nội dung).
5. Đếm sources tăng dần.
6. Vào Studio, chọn 1 trong 9 loại đầu ra, mở hộp thoại Customize, chọn Format/Style/Language/Level of detail, nhập mô tả tự do, bấm "Generate".
7. Trạng thái "Generating [Video/Audio] Overview... This may take a while" [b45 t=137-179s], [b41 t=183-238s] (có trường hợp treo mãi không hoàn tất trong phần còn lại của video).
8. Kết quả xuất hiện dạng thẻ trong lịch sử Studio, ghi "N sources · X phút/giờ/ngày trước".

Tích hợp Gemini và NotebookLM [b18]: mở notebook từ sidebar "Notebooks" trong Gemini app, chat trong đó, bấm link "NotebookLM" góc trên phải để mở sang notebooklm.google.com cùng notebook, thấy nguồn "Chats from Gemini (1)" tự động đồng bộ làm 1 source [b18 t=537-566s]. Tính năng "Move Chat" cho phép chuyển một đoạn chat vào notebook có sẵn qua modal "Select a notebook to move this chat into" [b18 t=610s].

### 2.7 Con số thật khác

- Video Cinematic "NotebookLM: Biến Nghiên Cứu Thành Video" dài 04:33 [b36 t=255.7s, t=309.6s].
- File mp4 tải về "Free_vs.mp4": 69.2 MB, 5:53, 1280x720, 30fps [b34 t=228-238s].
- Audio Overview mẫu "OpenClaw and the aut...": dài 24:01 [b34 t=686s]. Video Overview cùng chủ đề: 05:46 [b34 t=699.8s].
- Video "Free vs. Paid: The $15 Google Education AI Dilemma": 05:53 [b34 t=194.2s, t=557.1s]. Video Short "How to Read a River for Gold": 01:21 [b45 t=167s]. Video "The Science of the Perfect Chocolate...": 04:44 [b45 t=209s]. Video "Cam Nang Leo Nui Trong Nha" (14 sources): 07:06 [b45 t=308s]. Video Short "How to Position Your Arms in Climbing" (10 sources): 01:08 [b45 t=389s]. Video "World Cup History and Broken Records" (10 sources): 01:19 [b45 t=415s]. Video "How Ocean Waves Travel Without Moving Water" (11 sources): 01:13 [b45 t=530s].
- Flashcards: tổng 65 thẻ trong 1 bộ [b34 t=352.6s].
- File PDF xuất từ notebook: 147 KB, trạng thái "Done" [b38 t=345.3s].
- Giới hạn ký tự Custom persona trong Configure Chat: 10.000 ký tự (ví dụ đã nhập "2207/10000") [b38 t=405.3-435.3s].
- Không quan sát thấy bảng giá cụ thể (Pro/Ultra) trên màn hình; chỉ có nhãn "PRO"/"CHUYÊN NGHIỆP" cạnh tên notebook và nút "Upgrade" nhưng không hiện giá cụ thể khi bấm [b40, t=208s]. [chỉ nghe nói, không thấy]: phụ đề nói gói Pro mở khoá video cinematic/short, tài khoản miễn phí bị giới hạn tính năng nâng cao, không có bảng so sánh giá Free/Pro nào được chụp lại [b45].

---

## 3. VMEG (dịch video đa ngôn ngữ và lip sync)

Nguồn: b10 (phần 1/2, t=0-845s), b11 (phần 2/2, t=847-936s). Kênh "Non-tech làm AI", người dẫn Elly.

### 3.1 Chi phí credit thật

- Credit ban đầu: 1008 credits [b10 t=55.3s].
- Dịch video mẫu 8 giây sang 3 ngôn ngữ (Japanese, Korean, English United States): modal "Need: 180 credits; Remaining: 1008 credits" [b10 t=364.9s]. Sau submit còn 828 credits [b10 t=453.4s].
- Lip Sync: theo lời kể tốn khoảng 60 credit [chỉ nghe nói, không thấy]; quan sát trên UI trước lip sync 828 credit [b10 t=453s], màn hình chờ xử lý hiện 768 credits [b10 t=468.4s] (828-768=60, khớp lời kể).
- My Tasks sau đó hiện 648 credits [b10 t=516.4s] (giảm thêm 120 so với 768, chưa rõ nguyên nhân chênh lệch này, lúc đó có 2 task đang chạy song song 99%) [suy luận].
- Dịch thêm sang tiếng Tây Ban Nha (Smart Tools > "Translate to other languages"): modal "Need: 60 credits; Remaining: 648 credits" [b10 t=628.8s], sau submit còn 588 credits [b10 t=684s].
- Transcription cho file "2 Phút Ra Design Đẹp...": modal "Confirm Submission" ghi Transcription Task Duration 11:24, Size 53.35MB, "basic transcription 6 credits/min * 12 mins", Credits Consumed 72 [b10 t=690.5s]; sau xác nhận credit đầu trang giảm còn 516 [b10 t=692.5s], khớp với "516 credits" hiển thị ở b11 [b11 t=886s].
- Không có bảng giá credit cố định công bố cho từng loại thao tác (ví dụ giá riêng của Lip Sync, Voice Cloning) trên UI ngoài các con số Need/Remaining nêu trên; chỉ Transcription có công thức rõ ràng "6 credits/min".

### 3.2 Các tùy chọn trên giao diện

Menu trái dashboard: Dashboard, Translation Agent, Dubbing Workflow (nhãn "New"), All Tools, Video Translator, Audio Translator, Transcription, Text to Speech (nhãn "New"), Subtitle Translator, My Tasks, Billing, My Assets, Clone Voice, Glossary, API [b10 t=55.3s, t=79.5s].

Trang Video Translation: tab "Single file translation" / "Bulk file translation", nút "Upload Media", ô dán link, hỗ trợ YouTube/Instagram/TikTok/X/Facebook/Google Drive/Zoom/Podcast [b10 t=70.3s]. Cài đặt dịch: Original Language, Target language (chọn nhiều ngôn ngữ cùng lúc), Pick a Voice Style, toggle "Allow Adjustments to Video Speed", "Advanced Options", nút "Submit", toggle "Multi Languages" [b10 t=70.3s].

Pick a Voice Style có 4 lựa chọn: "Voice Cloning – More Emotional" (tag Emotional, "Makes the voice more expressive and preserves the emotions in each sentence. Best for films, dramas, or storytelling."), "Voice Cloning – More Consistent" (tag Consistent, "Keeps each speaker's voice steady and consistent throughout the video. Great for lectures, meetings, or tutorials."), "Match System Voices", "Manually Select Voices" [b10 t=324s].

Advanced Options: Subtitle Type (No subtitles / Translation / Original / Bilingual), Subtitles Style, Upload SRT/VTT, Translation Prompt, Glossary, Pronunciation, Filler Word Selection, Select a Folder, High Quality Transcription Mode [b10 t=335-364s].

Trang Editor có panel: Details, Setting, Voice, Video, Subtitle, Lip Sync, Glossary [b10 t=110s]. Panel Subtitle: Preset styles (12 kiểu chữ), My styles, Typography (font đổi theo ngôn ngữ đích, ví dụ "Exo-Bold" size 16 cho tiếng Anh [b10 t=396.4s], "NotoSansJapanese" cho tiếng Nhật [b10 t=573.8s]), Outline/Shadow/Background. Subtitle Split Mode có "Sync with Dubbing" và "Auto Split" [b10 t=373.7s]. Panel Voice: Volume, Speed, Speaker, Voice, "Redo Voice Clone", "Apply voice to all Vlogger", Emotion setting [b10 t=661.5s].

Transcription Mode: "Balanced" (Standard, good quality) và "Accurate" (Fast, high-precision) [b10 t=650.1s]. Kết quả Transcription tải về theo 6 định dạng: TXT, SRT, VTT, Spruce (.stl), TTML (.xml), YouTube (.sbv) [b10 t=690-698s].

Smart Tools trong Editor có 3 mục: "Recognize original script", "Upload SRT subtitles", "Translate to other languages" [b10 t=573.8-588.8s].

Dubbing Workflow: bảng "Workflow Projects (N)", nút "+ New Project", modal cho phép upload tối đa 20 file (.mp4, .mov, .webm, .m4v, .mkv) [b10 t=796-801s]. Bước "Original Script Review" có thanh tiến trình dạng "0/9, 0%", cột ngôn ngữ gốc, mỗi dòng có speaker/mốc thời gian/ô văn bản, nút "Proofread Script" và "Generate Translation" [b10 t=812-827s], lặp lại ở b11 [b11 t=886s].

### 3.3 Checklist "Best Practices" (chép nguyên văn)

"Best Practices for Lip Sync Accuracy" [b10 t=684s]:
- Keep only one face in the video (multiple faces can reduce sync accuracy)
- Keep head movements minimal (excessive shaking may break sync)
- Ensure a clear front-facing view (avoid side angles or obstructions)
- Use good lighting (shadows or flickering lights affect accuracy)
- Speak at a natural speed (too fast or exaggerated speech may cause mismatches)
- Video size must be at least 360px (lower resolutions may not work well)

### 3.4 Quy trình từng bước

1. [b10 t=55.3s] Vào dashboard VMEG, bấm "Video Translator".
2. [b10 t=70-77s] Upload Media, chọn file MOV (tên file "dji_export_20260701_145807_1782892687709_compose_0.MOV", 31.6 MB).
3. [b10 t=106-149s] Chọn Original Language = Vietnamese, thêm 3 Target Language: Japanese, Korean, English (United States).
4. [b10 t=164s] Chọn Voice Style = "Voice Cloning – More Consistent".
5. [b10 t=179-254s] Mở Advanced Options, thử các Subtitle Type, xem các mục còn lại.
6. [b10 t=268-298s] Bấm Submit (180 credits), sang My Tasks chờ xử lý.
7. [b10 t=350-395s] Vào Editor, xem từng đoạn dịch, chỉnh Voice, Preset Style phụ đề, Typography.
8. [b10 t=438-453s] Bấm Lip Sync, đọc Best Practices, bấm Continue.
9. [b10 t=468-521s] Chờ xử lý (credit giảm còn 768 rồi 648), mở kết quả video đã lip sync.
10. [b10 t=550-628s] Mở Smart Tools > "Translate to other languages", thêm Spanish, giữ Voice Style, Submit (60 credit).
11. [b10 t=650-698s] Chuyển sang Transcription, chọn Balanced, tải file lên, Confirm Submission (72 credits), xem kết quả transcript song ngữ.
12. [b10 t=713s] Chuyển sang Text to Speech, minh họa hội thoại nhiều giọng với tag cảm xúc.
13. [b10 t=796-834s] Chuyển sang Dubbing Workflow, tạo New Project, bước Original Script Review.
14. [b10 t=845s] Kết đoạn phần 1, chuyển sang YouTube Studio.
15. [b11 t=847-886s] Ở YouTube Studio, thao tác thêm bản âm thanh dịch ("Âm thanh bằng Tiếng Anh") cho video đã đăng; sau đó quay lại VMEG ở "Original Script Review" cho video khác ("CLAUDE + REMOTION").

### 3.5 Lỗi và điểm bất thường thực tế

- Toast "Added successfully" khi áp preset phụ đề mới [b10 t=395s].
- Transcript tự động ghi "Clock" thay vì "Claude" ở nhiều dòng thoại (cả ở b10 lẫn b11), khả năng công cụ nhận diện giọng nói phiên âm sai tên riêng "Claude" [suy luận, b11 t=886s].
- [b11 t=869s] Nút "Xuất bản" trong hộp thoại thêm âm thanh YouTube Studio có màu xám nhạt hơn nút "Hủy", có thể đang vô hiệu hoá chờ chọn tệp trước [suy luận].
- [b11, t=908-936s, chỉ nghe nói, không thấy minh hoạ cụ thể]: tác giả nhận xét VMEG "chất lượng khá là ok", "tạo được cùng một lúc nhiều phiên bản dịch", "có thể detect được speaker khác nhau", nhưng "dịch thì nó cũng tương đối là sắt" (nghe không rõ).
- Popup QR "Join our WhatsApp community for instant support and updates" xuất hiện lặp lại rất nhiều lần khắp giao diện dashboard.

### 3.6 Con số thật khác

- File gốc: 31.6 MB theo hộp thoại mở file [b10 t=77.1s]; Editor timeline ghi 30.17 MB [b10 t=95.4-364.9s] (chênh lệch nhỏ, cách đo khác nhau) [suy luận].
- Thời lượng video test: 8 giây (00:00:00 / 00:00:08) [b10 t=298-453s].
- Kênh YouTube "Non-tech làm AI": 2.73 nghìn người đăng ký, 34 video [b10 t=91-96s, t=453s].
- b11: thời lượng video xem trước VMEG "00:00:46", timeline kéo dài đến "00:06:00" dù nội dung chỉ 46 giây [suy luận, có thể khung timeline kéo rộng hơn nội dung, b11 t=886s]. Thời lượng video gốc trong hộp thoại YouTube Studio: "21:06" [b11 t=877s].

---

## 4. OpenMusic AI và Suno để làm MV ca nhạc

Nguồn: b30 duy nhất. Video: "Tạo MV Ca Nhạc AI từ A-Z chỉ với 1 công cụ AI duy nhất - OpenMusic AI".

### 4.1 Chi phí credit từng thao tác trên OpenMusic

- Tạo âm nhạc: 2 credit (nút "Tạo âm nhạc ✦2") [b30 t=486s].
- Tối ưu hóa lời: 0.5 credit (nút "Tối ưu hóa ✦0.5") [b30 t=571s].
- Tạo lời bài hát (mới/ngẫu nhiên): 0.5 credit (nút "Tạo lời bài hát ✦0.5") [b30 t=571s, t=601s].
- Tách nhạc (AI Vocal Remover): 2 credit (nút "Tách nhạc ✦2") [b30 t=746s].
- Huấn luyện mô hình âm thanh (Voice AI): 30 credit (nút "Huấn luyện mô hình âm thanh ✦30") [b30 t=845-978s].
- Tạo Bìa (Cover): 2 credit (nút "Tạo Bìa ✦2") [b30 t=893s].
- Tạo hình ảnh mỗi shot (Video ca nhạc AI): 2 credit.
- Tạo Phiên Bản Mới video mỗi shot: 18 credit (thấy 2 lần) và 21 credit (thấy 1 lần, không cố định) [b30 t=1063-1088s].
- Thử lại video toàn bộ: 15 credit [b30 t=1096s].
- Credit còn lại giảm dần đúng theo thứ tự xuất hiện trên video: 1015.5 → 1013.5 → 1012.5 → 1010.5 → 980.5 → 978.5 → 976.5 → 962.5 → 836.5 (giảm mạnh nhất ở bước tạo video từng shot) → 836.5 (không đổi khi mở MIDI editor).

### 4.2 Quy trình từng bước làm MV

1. [b30 t=137-227s] Vào OpenMusic AI và mở song song Suno.com; điền mô tả bài hát vào "Song Description" trên Suno, tạo workspace "Bài hát 1 - Em đã mạnh mẽ hơn"; kết quả ban đầu "No songs found" do bộ lọc 3 điều kiện chặn.
2. [b30 t=252-282s] Mở project Claude "Chuyên gia viết chuẩn hoá prompt" (model "Sonnet 4.6", mức "Medium") để chuẩn hoá lại mô tả trước khi đưa vào công cụ nhạc; xác nhận qua caption "Mình để bộ prompt chuyên gia chuẩn hoá mọi prompt ở phần description nhé".
3. [b30 t=307-354s] Chuyển sang OpenMusic thật, mở "Trình tạo bản cover bài h...", thêm Persona, xem lời bài hát mẫu.
4. [b30 t=367-431s] Trên Suno (Advanced), điền phong cách "Funk", thêm gợi ý "deep synth bass", "taiko drum", bấm Create.
5. [b30 t=456-601s] Trên OpenMusic, dán lời, đặt Phong cách = Funk, tạo bài "Minh Đủ Rồi"; chỉnh sửa từng đoạn lời qua "Tối ưu hóa ✦0.5".
6. [b30 t=746-836s] Vào AI Vocal Remover, tách nhạc, xem file kết quả instrumental.mp3 và vocal.mp3.
7. [b30 t=845-978s] Vào Trình tạo Giọng hát AI, ghi âm mẫu giọng (~3 phút, "Tốt"), chọn giới tính Nam, Huấn luyện mô hình (30 credit); dùng giọng "Elly Huyền" để cover bài "Yêu Em Bằng Điều Anh Làm" qua Trình tạo bản cover, Tạo Bìa (2 credit).
8. [b30 t=1000-1096s] Vào Video ca nhạc AI > Video nhạc truyện: chọn bài hát nguồn, cắt đoạn nhạc nền (15 giây đến 8 phút), chọn tối đa 2 Character, chọn phong cách hình ảnh, viết tóm tắt câu chuyện, chọn độ phân giải 720p/1080p, tạo (chờ 3-5 phút theo thông báo hệ thống).
9. [b30 t=1096-1153s] Xem từng ảnh shot, bấm Tạo video để biến ảnh thành clip động (18-21 credit/shot); vào Trình chỉnh sửa để ráp các shot thành video hoàn chỉnh trên timeline kèm track âm thanh.
10. [b30 t=1153-1198s] Giới thiệu thêm Trình chỉnh sửa MIDI AI (piano roll) và AI Âm thanh sang MIDI.
11. [b30 t=1228-1258s] Bảng so sánh SUNO vs OPENMUSIC.AI để tổng kết chọn công cụ.
12. [b30 t=1288s trở đi] Video lyric hoàn chỉnh của bài hát làm đoạn kết.

Quy trình dựng video tóm tắt 3 bước: (1) tạo hình ảnh từng shot, (2) biến ảnh thành video từng shot (mô tả chuyển động camera theo giây, thuật ngữ "CẮT CỨNG"), (3) dùng Trình chỉnh sửa để ráp toàn bộ với track âm thanh trên timeline.

### 4.3 Giới hạn của từng nền tảng

- Độ dài mẫu giọng huấn luyện Voice AI: 1 phút (Tối thiểu) / 10 phút (Tốt, khuyến nghị) / 30 phút (Tối đa) [b30 t=787s]. Bản ghi thực tế: "Đã tải lên: 3min", trạng thái "Tốt".
- Nguồn "Âm thanh đào tạo" có 3 cách: Tải lên nhạc (10-30 phút âm thanh sạch), Ghi âm, Tách giọng hát (trích từ bài hát đầy đủ) [b30 t=787s].
- Độ dài audio hợp lệ cho Video nhạc truyện: 15 giây đến 8 phút.
- Character: tối đa 2 nhân vật mỗi video [b30 t=1012-1022s].
- Độ phân giải video xuất: 720p / 1080p.
- Định dạng hỗ trợ AI Vocal Remover: MP3, WAV, OGG, M4A, FLAC, WMA [b30 t=746s]. Định dạng hỗ trợ Âm thanh sang MIDI: .wav, .mp3, .flac, .ogg [b30 t=1168s].
- Trên Suno: bản nhạc preview (nhãn "v5.5 Preview") chỉ nghe được 1:00, cần "Upgrade for full song" để nghe đầy đủ [b30 t=1063-1088s].
- Công cụ "Video hát" (trong Video ca nhạc AI) gắn nhãn "Sắp ra mắt", chưa dùng được tại thời điểm quay [b30 t=1000s].

### 4.4 So sánh giá Suno vs OpenMusic

Giá gói theo bảng so sánh cuối video: Suno Pro = 8 USD/tháng; OpenMusic.AI = 10 USD/tháng [b30 t=1228-1258s]. Model đang dùng: Suno hiển thị "v4.5-all" (Simple/Advanced), có banner giới thiệu model mới "v5.5"; OpenMusic hiển thị "V2.5". Suno có Weirdness 50% và Style Influence 50% (mặc định). OpenMusic có bộ công cụ rộng hơn: Trình tạo nhạc AI, Trình tạo lời bài hát AI, Trình tạo bản cover, Trình tạo Giọng hát AI, Video ca nhạc AI, AI Vocal Remover, AI Tách Stem, Mastering AI, Trình chỉnh sửa MIDI AI, AI Âm thanh sang MIDI, Máy tính BPM. Tính năng làm MV video (Video nhạc truyện, Video từ ảnh, Video hát "Sắp ra mắt") chỉ thấy trên OpenMusic, không thấy trên Suno.

Lưu ý mâu thuẫn tiêu đề [suy luận, dựa trên nhiều frame]: dù tiêu đề video ghi "chỉ với 1 công cụ AI duy nhất - OpenMusic AI", nội dung thực tế dùng song song cả Suno và OpenMusic; tên project Claude còn ghi "OpenMusic ai comparison video" và cuối video có bảng so sánh Suno vs OpenMusic, nội dung thực chất là video so sánh hai công cụ.

### 4.5 Lỗi thực tế

- "The upstream API service timed out and no results were returned..." khi tạo nhạc thất bại trên OpenMusic (bài "Tự Yêu Minh") [b30 t=520s].
- Trên Suno, tìm bằng bộ lọc 3 điều kiện trả về "No songs found" kèm nút "Reset filters" [b30 t=307s].
- Trong Trình chỉnh sửa MIDI AI, hộp thoại chọn file nhập hiện toàn file ảnh PNG không liên quan MIDI/audio, có thể do duyệt nhầm thư mục "Tài liệu" chứ không phải bug công cụ [suy luận, b30].

### 4.6 Con số thật khác

- Bài "Golden" (mẫu demo AI Vocal Remover) dài 01:40; bài "Tự Ơm Lấy Em" dài 4:05.
- Video mỗi shot khi xem trước dài khoảng 6 giây (00:00/00:06).
- Clip TikTok cá nhân "Elly Huyền" dùng làm nguồn cảm hứng: 44.8K tim, 48 bình luận, 885 lượt lưu, 912,2K lượt xem, 1079 lượt chia sẻ [b30 t=616-698s].

---

## 5. Các công cụ khác (Google AI Studio, Google Vids, Canva, Pomelli, Stitch)

Chỉ phần liên quan làm video hoặc hình ảnh, viết ngắn gọn hơn 4 mục trên.

### 5.1 Google AI Studio

Panel "Run settings" khi chọn model ảnh: System instructions, Output format (Images & text / Images only), Temperature, Aspect ratio, Resolution, Thinking level, mục Tools (Grounding with Google Search, Grounding with Google Maps, URL context, Code execution, Function calling, Structured outputs) [b47 t=38s, t=181.5s]. Model tạo ảnh "Nano Banana 2" (id kỹ thuật "gemini-3.1-flash-image-preview") [b47 t=181.5s]. Aspect ratio: Auto, 1:1, 9:16, 16:9, 3:4, 4:3, 3:2 (cuộn tiếp) [b47 t=405.1s]. Resolution: 1K, 2K. Thinking level: Minimal, High [b47 t=435.133333s].

Giá API (per 1M token, ghi chú "miễn phí khi dùng UI AI Studio không chọn API key" [b47 t=598.3s]):
- Gemini 3 Pro Image Preview: Text Input 2.00 USD / Output 12.00 USD; Image Input 2.00 USD / Output 0.134 USD mỗi ảnh; cutoff Jan 2025; release Nov 20, 2025 [b15 t=750.2s].
- Nano Banana (gemini-2.5-flash-image): Text Input 0.30 USD / Output 2.50 USD; Image Input 0.30 USD / Output 0.039 USD mỗi ảnh; cutoff Jun 2025; release Sep 30, 2025 [b15 t=750.2s].
- Gemini 3 Flash Preview: Input 0.50 USD / Output 3.00 USD [b47 t=328.4s]. Gemini 3.1 Pro Preview: dưới 200K token Input 2.00 USD / Output 12.00 USD, trên 200K token Input 4.00 USD / Output 18.00 USD [b47 t=328.4s].

Thời gian tạo ảnh mẫu (prompt "1 con lười"): 15.2 giây [b47 t=156.966667s]. GenType (labs.google/gentype) đã chuyển hẳn sang AI Studio; bản cũ báo lỗi "GenType is currently under maintenance. Please check back later." [b15 t=587.8s]. App tự build trong AI Studio (ví dụ "BizMate") phát sinh lỗi "1 error running the code" ngay sau khi tạo xong [b47 t=1004.4s, t=1028.6s].

### 5.2 Google Vids

Popup khởi tạo "Hello, [tên]. Let's start creating." có 3 tab tỉ lệ Landscape/Portrait/Square và 8 cách tạo nội dung: "Veo 3.1 New", "AI avatar New", "Lyria 3 New", "Convert Slides", "Record", "Upload", "Templates", "Storyboard", cùng "Blank vid" [b42 t=284s]. Khi chọn "Convert Slides": popup "Select slides" hiện "Generating thumbnails..." kèm toggle "Include AI voiceover, script, background music and animation" [b42 t=314s]. Kết quả video dựng từ slide có timeline với track lời thoại, đồng hồ tiến trình "00:21.8 / 02:35.7" [b42 t=342s]. Thanh công cụ dựng video: Veo, Avatar, Voiceover, Music, Image, Record, Uploads, Stock, Captions, Text [b14 t=264-283s].

### 5.3 Canva (qua Claude connector và độc lập) — chỉ phần liên quan tới ảnh

Claude connector Canva có thể sinh ảnh design mới ngay trong hội thoại: "Canva generated 4 design candidates! Here they are, pick your favorite:" [b41 t=324s], [b43 t=623.9s]. Prompt Red Bull dùng lại y nguyên trên cả Claude, Gemini, Canva AI: "@Canva Create an Instagram post for a Red Bull new flavor launch. Bold headline 'NEW FLAVOR' text, can centered, dark background, neon glow effects, 1:1 format - follow brandkit and add logo" [b43 t=624s, t=696s, t=884.8s].

Lỗi/giới hạn liên quan tới ảnh:
- "không thể truy cập file ảnh từ domain này" khi dùng ảnh xuất Canva ở nơi khác, sửa bằng cách dùng Canva export URL trực tiếp [b41 t=601s].
- Claude "cứ loay hoay không upload được" ảnh riêng, sửa bằng cách upload ảnh lên Canva trước [b41 t=616s].
- Tải ảnh từ Claude+Canva connector chỉ ra file PNG tĩnh (qua export-download.canva.com), không mở được file Canva chỉnh sửa được như kỳ vọng [b43 t=670.6s].
- Gemini dùng "@Canva" nhiều lần bị chặn: "I'm sorry, but it looks like you've reached your Canva plan's monthly AI limit..." [b43 t=711-825s].
- Canva công cụ AI (Magic) có thời gian chờ giữa các lần dùng, popup đếm ngược "Bạn có thể tạo lại sau 3:53" [b44 t=1042s, t=1072s].

Tính năng riêng của Canva đáng chú ý cho làm ảnh/video: "Magic Layers" tách ảnh AI (ví dụ infographic từ NotebookLM) thành các lớp chỉnh sửa được, popup "Hình ảnh được tách thành các lớp có thể chỉnh sửa" [b45 t=382s, t=412s]. Panel "Chỉnh sửa hình ảnh" gồm 8 công cụ, trong đó có "Hình ảnh thành video" và "Xóa nền" [b44 t=1103s].

### 5.4 Pomelli — chỉ phần liên quan tới ảnh

Pomelli (nhãn "EXPERIMENT" [b32 t=214s]) chủ yếu là công cụ chiến lược thương hiệu và web, ngoài phạm vi skill này; phần duy nhất liên quan tới làm ảnh là bước "Generate a Product Photoshoot" [b32 t=35s], sinh ảnh sản phẩm theo danh mục General (Studio, In Use, Contextual, Flatlay), Beauty, giới hạn chọn tối đa 4 template ảnh mỗi lần ("4/4 selected") [b32 t=336s].

### 5.5 Stitch — ngoài phạm vi skill

Stitch là công cụ thiết kế app/web (tạo giao diện, xuất code Figma/HTML), không sinh ảnh hay video, nên ngoài phạm vi skill này [b28 t=0s, t=64-75.5s].
