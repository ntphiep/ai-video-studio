# Content playbook — chọn dạng nội dung, đường đi, chi phí

Chiến lược nội dung cho skill `ai-video-studio`. Prompt và công thức viết
prompt đã chuyển sang `prompt-library.md`, không lặp lại ở đây. Quy trình kỹ
thuật từng đường (Remotion, Gemini Notebook, VMEG, UGC) nằm ở
`other-routes.md`; số đo tool và định dạng nằm ở `flow-tools.md` và
`format-and-export.md`. File này chỉ trả lời: nên làm dạng nội dung gì, đi
đường nào, tốn bao nhiêu.

<!-- MUCLUC:BAT-DAU (sinh bang scripts/gen_toc.py, dung sua tay) -->
**Mục lục** (số dòng để đọc thẳng đúng đoạn, không cần nạp cả file)

- 1. Bảng nền tảng — dòng 23
- 2. Dạng nội dung khả thi — dòng 40
- 3. Quy trình theo từng dạng nội dung — dòng 62
- 4. Bốn dạng ngoài năng lực sinh video của Flow — dòng 82
- 5. Muốn làm dạng video X thì đi đường nào, tốn bao nhiêu — dòng 118
- 6. Lịch sản xuất đề xuất (một người, 5-10 giờ/tuần) — dòng 164
- 7. Monetization và policy (cảnh báo, dùng chính xác) — dòng 174
- Tự soát nguồn — dòng 197

<!-- MUCLUC:KET-THUC -->
## 1. Bảng nền tảng

| Nền tảng | Aspect | Độ dài ngọt | Ghi chú |
|---|---|---|---|
| YouTube (video dài) | 16:9 | 8-15 phút giữ chân tốt [kinh nghiệm] | Xuất H.264/AAC/48k/24fps |
| YouTube Shorts | 9:16 | [chưa xác minh, cần đọc lại doc YouTube] | Veo/Omni sinh 9:16 trực tiếp |
| TikTok | 9:16 | 15-60s [kinh nghiệm] | MP4 cùng spec |
| Instagram/Facebook Reels | 9:16 | 15-30s [kinh nghiệm] | MP4 cùng spec |

Flow chỉ sinh trực tiếp 16:9 và 9:16 (`format-and-export.md` mục 1). Đổi
sang 4:5, 1:1, 21:9, khung tuỳ chỉnh thì dùng Tool **Video Resizer**, đo bằng
ffprobe và ledger ngày 06/09/2026 là không trừ credit (`flow-tools.md` mục
3.5), cùng với **Type Overlays**. Đây là hai Tool duy nhất xử lý phía client;
Tool khác gọi model sinh ảnh/video (Whisk, Mask Magic...) nên coi là CÓ tốn
credit tới khi tự đo được, vì mở Tool nào Flow cũng cảnh báo "This Tool may
consume credits".

## 2. Dạng nội dung khả thi

| Dạng | Mô tả | Chi phí | Tại sao viral |
|---|---|---|---|
| ASMR cắt glass fruit | Dao cắt trái cây thuỷ tinh, macro, slow-mo | Thấp | Đã có lượng xem lớn, dễ nhập môn |
| ASMR quy mô bất khả thi | Kinetic sand khổng lồ, nghìn viên bi 240fps | Thấp | AI có lợi thế tuyệt đối vs quay thật |
| ASMR keyboard lạ | Bàn phím mật ong/dưa hấu, âm thanh không ghi được ngoài đời | Thấp | Twist mới đang kéo view |
| Survival/jungle building | Tutorial dựng lều, nấu ăn giữa rừng kiểu ASMR | Thấp-trung bình | Ngách tăng nhanh [1 nguồn] |
| Mukbang/food ASMR macro | Cảnh ăn macro, gắn affiliate dụng cụ bếp | Trung bình | RPM cao, cộng Shorts để discovery |
| Story/drama nhiều nhân vật | Kịch bản 3-6 nhân vật, drama gia đình Việt | Cao (Omni/Veo + Character + Voice) | Thông điệp đạo lý, dễ cuốn khán giả Việt |
| Faceless giáo dục/explain | Kịch bản, chia cảnh, image sang video | Thấp | Scale được, một người làm đủ |
| 2D avatar reaction | Avatar 2D nói/phản ứng theo voiceover | Trung bình | Dễ đồng bộ giọng, làm series |
| Whisper roleplay | Persona cố định, ví dụ bà kể chuyện bên lửa trại | Trung bình | Persona ổn định giảm rủi ro policy |
| Storyboard storytelling | Storyboard Studio tạo cast rồi dựng cảnh | Trung bình | Giữ đồng nhất nhân vật tốt nhất |
| Product ads/brand montage | 30s gồm 5-6 clip 4-6s, ghép nhạc có bản quyền | Trung bình | Case Wild Hare: cắt chi phí, bán được dịch vụ |
| Cinematic vlog b-roll | Bốn clip establishing/action/reaction/resolve | Thấp | Dễ loop, dễ series, hợp Reels/TikTok |

Bài học từ kênh @nontechlamAI: video A-Z tổng hợp viral gấp nhiều lần video
ngách lẻ, nên làm một video trụ cột cộng nhiều video ngách lấp lỗ hổng. ASMR
là nhóm chi phí thấp nhất, không cần giữ nhân vật nhất quán, không cần thoại,
hợp làm kênh khởi đầu.

## 3. Quy trình theo từng dạng nội dung

- **Shorts giá rẻ**: lấy ý tưởng Pinterest, Claude viết 6 cảnh (mỗi cảnh 2
  prompt ảnh), Flow sinh ảnh 9:16 x4 chọn ảnh 2K tốt nhất, sinh video từ ảnh
  đầu và ảnh cuối, mỗi clip 6 giây, rồi ghép.
- **Drama nhiều nhân vật tiếng Việt**: tạo từng Character (mô tả, 3 góc body,
  giọng Việt 100% cộng Customized Performance và câu mẫu), tạo ảnh bối cảnh
  bằng Nano Banana 9:16, dùng "+" gộp nhân vật và bối cảnh vào một prompt Omni
  Flash ghi rõ ai nói câu nào, lặp từng cảnh rồi ghép ở CapCut kèm nhạc.
- **Kể chuyện từ storyboard**: Storyboard Studio tự viết kịch bản/cast/asset
  theo style chọn trước, Gemini dựng storyboard từng cảnh 10 giây, tạo
  Character từ ảnh đó cộng giọng, generate từng cảnh rồi ghép.
- **Tự động hoá Claude điều khiển Flow**: viết prompt liền mạch, không xuống
  dòng (Enter trong Flow generate ngay, từng gây sinh 9 video cùng lúc); sau
  khi Claude compact hội thoại phải kiểm tra lại skill vì dễ quên đầu bài; có
  thời gian thì chỉ dùng Claude sinh prompt, tự thao tác Flow, nhanh và đỡ
  cháy credit hơn để agent tự bấm.
- **Explainer dài qua Agent**: đưa kịch bản đầy đủ, để Agent tự chia cảnh, tạo
  từng clip 10 giây, ghép, duyệt thủ công theo từng đợt.

## 4. Bốn dạng ngoài năng lực sinh video của Flow

Chi tiết từng bước ở `other-routes.md`, đây chỉ tóm tắt để chọn đường.

**UGC quảng cáo sản phẩm.** Người thật cầm sản phẩm review, giọng đời thường,
chân thực hơn quảng cáo chỉn chu điện ảnh. Theo lời kể người làm video (chưa
đối chiếu số liệu chính thức): nền tảng UGC chuyên dụng khoảng 15.000 đồng/
clip 30 giây, làm bằng Flow khoảng 45 credit (30.000-40.000 đồng), thuê KOC
thật từ 10.000 follower tốn tiền trăm nghìn đến triệu; nền tảng UGC chuyên
dụng cho chất lượng tiếng Anh tốt hơn hẳn tiếng Việt.

**Video đa ngôn ngữ có lip sync (VMEG).** Dịch video gốc ra nhiều ngôn ngữ,
giữ giọng gốc bằng voice clone rồi khớp lại khẩu hình. Chi phí đo trực tiếp
trên màn hình: dịch 3 ngôn ngữ 180 credit, Lip Sync 60 credit, thêm mỗi ngôn
ngữ 60 credit, Transcription 6 credit/phút (credit riêng của VMEG, không
chung với Flow). YouTube cho gắn nhiều track audio ngôn ngữ vào cùng một
video (Studio, mục ngôn ngữ) nên không cần đăng nhiều bản riêng cho từng thị
trường [chưa đối chiếu doc chính thức YouTube].

**Video từ tài liệu.** **NotebookLM đã đổi tên thành Gemini Notebook** từ
16/07/2026, theo blog chính thức của Josh Woodward (Phó chủ tịch Google Labs
phụ trách Gemini app và AI Studio). Studio xuất 9 loại, gồm Audio Overview,
Slide Deck, Video Overview, Mind Map, Reports, Flashcards, Quiz, Infographic,
Data Table. Video Overview có 3 định dạng (Cinematic, Explainer, Short/Brief
tuỳ bản UI) cộng dropdown chọn ngôn ngữ, hợp khi đã có tài liệu dài muốn
biến thành video mà không cần viết kịch bản từ đầu. Chưa thấy bảng giá
credit trên màn hình, chỉ có nhãn "PRO"/Upgrade không kèm số; "giới hạn 20
video Cinematic/ngày" chỉ là lời AI tự khai trong chat, độ tin cậy thấp.

**Motion graphics và kinetic typography chính xác.** Model sinh video của
Flow không kiểm soát được nội dung chữ chính xác (`troubleshooting.md` mục 4,
phần chữ không phải Latin). Chữ tĩnh hoặc hiệu ứng đơn giản dùng Tool **Type Overlays**, ra đúng
từng ký tự kể cả dấu tiếng Việt, không trừ credit. Chữ động phức tạp (đếm
số, biểu đồ, đường tia, nền trong suốt) dùng Remotion, xuất SRT hoặc video
nền trong suốt rồi ghép ở khâu dựng.

## 5. Muốn làm dạng video X thì đi đường nào, tốn bao nhiêu

Dựa trên bảng giá credit đọc trực tiếp trên panel cài đặt Flow ngày
06/09/2026, tài khoản gói AI Pro, khớp với trang hỗ trợ chính thức
support.google.com/flow/answer/16526234.

| Muốn làm gì | Đi đường nào | Chi phí |
|---|---|---|
| Nháp ý tưởng trước khi render bản cuối | Omni 1.1 Flash, 360p | 4 credit (4s) đến 7 credit (10s) |
| ASMR/faceless/b-roll/2D avatar/shorts (bản cuối) | Omni 1.1 Flash, 720p | 7 credit (4s) đến 15 credit (10s) |
| Cùng dạng trên, cần chất lượng Veo | Veo 3.1 Lite | 10 credit thường, 5 nếu Ultra |
| Drama/storyboard/ads cần khớp thoại tốt hơn | Veo 3.1 Fast | 20 credit thường, 10 nếu Ultra |
| Cảnh quan trọng nhất, cần chất lượng cao nhất | Veo 3.1 Quality | 100 credit, mọi gói như nhau |
| Đổi tỉ lệ khung hình sau khi đã có video | Tool Video Resizer | 0 credit (đã đo) |
| Tiêu đề/quote/lower-third chính xác từng chữ | Tool Type Overlays | 0 credit (đã đo) |
| Sửa (edit) một video đã sinh, không sinh lại từ đầu | Gemini Omni Flash, task edit | 40 credit, mọi gói như nhau |
| Nâng bản nháp thấp độ phân giải lên 1080p | Nâng cấp resolution (mọi model) | Miễn phí, áp dụng cho mọi người dùng đã trả phí (Plus/Pro/Ultra) |
| Nâng độ phân giải lên 4K | Nâng cấp resolution (mọi model) | 50 credit, CHỈ tài khoản Ultra dùng được |
| UGC quảng cáo sản phẩm | Nền tảng UGC chuyên dụng hoặc mô phỏng trong Flow | ~15.000đ/nền tảng UGC hoặc ~45 credit Flow/clip 30s [chưa xác minh] |
| Video đa ngôn ngữ kèm lip sync | VMEG | 180 credit/3 ngôn ngữ, 60 credit Lip Sync, 60 credit/ngôn ngữ thêm, 6 credit/phút transcription |
| Video dựng từ tài liệu có sẵn | Gemini Notebook | [chưa xác minh, chưa thấy bảng giá trên màn hình] |
| Chữ động phức tạp, đếm số, biểu đồ | Remotion | Không dùng credit Flow, chi phí API riêng, xem `other-routes.md` |

Ba dòng sửa video/nâng độ phân giải ở trên đọc trực tiếp từ bảng giá chính thức
`support.google.com/flow/answer/16526234`, đối chiếu với phép đo trực tiếp trên giao diện
mục 2, đọc 08/09/2026 [doc]. Trang chính thức không nói rõ Nâng lên 720p có
tốn credit hay không (chỉ có dòng 1080p và 4K) — không suy diễn thêm.

**Quy trình rẻ nhất hiện nay: nháp 360p rồi nâng độ phân giải, đừng sinh lại.**
Theo cập nhật "New creative controls in Google Flow" (Google Labs blog,
27/08/2026, xem `changelog.md`), cách rẻ nhất để có bản video chất lượng cao
không phải là sinh thẳng ở độ phân giải cao ngay từ đầu, mà là: sinh nháp ở
**360p** (rẻ nhất, 4-7 credit tuỳ độ dài) để duyệt nội dung và bố cục trước,
rồi mới **nâng độ phân giải** đúng bản đã ưng ý (miễn phí lên 1080p cho người
trả phí, 50 credit lên 4K chỉ Ultra), thay vì sinh lại nhiều lần ở 720p hoặc
cao hơn cho tới khi vừa ý. Mỗi lần sinh lại ở độ phân giải cao để thử sai tốn
credit gấp nhiều lần so với một lượt nháp 360p cộng một lượt nâng cấp duy
nhất khi đã chốt được nội dung.

Mục **"Veo 3.1 Lite [Lower Priority]"** xuất hiện trong một số video hướng
dẫn, nhưng theo changelog chính thức (mục 10/04/2026) chỉ dành cho gói Ultra;
tài khoản AI Pro không có, không phải lỗi quan sát. Con số "0 credit" gắn với
mục này đến từ một bài đăng mạng xã hội cùng ngày, không phải chữ trong
changelog, và hai người dùng đã lên Ultra vẫn báo không thấy mục này trên
support.google.com, nên đừng coi đây là đường miễn phí chắc chắn.

## 6. Lịch sản xuất đề xuất (một người, 5-10 giờ/tuần)

- Chọn 1-2 dạng nội dung chính, ví dụ story drama cộng faceless giáo dục.
- Mỗi tuần 1 video trụ cột (A-Z tổng hợp hoặc drama hoàn chỉnh) cộng 2-3
  Shorts cắt từ đó hoặc làm song song.
- Test ý tưởng bằng Omni 360p (4-7 credit) rồi mới render bản cuối. Model
  picker thật trên gói AI Pro chỉ có 4 lựa chọn: Omni 1.1 Flash, Veo Lite,
  Veo Fast, Veo Quality.
- Lưu prompt tốt vào file skill để dùng lại cho đợt sau.

## 7. Monetization và policy (cảnh báo, dùng chính xác)

Quy định chính thức đọc được: **YouTube không cấm AI, chỉ cấm "inauthentic
content"** (chính sách 15/07/2025): "content that looks like it's made with
a template with little to no variation across videos, or content that's
easily replicable at scale." Disclosure bắt buộc cho realistic synthetic
(người thật bị thay mặt/giọng, footage sự kiện thật bị biến đổi); không cần
disclosure cho cartoon, hiệu ứng rõ ràng, hoặc AI chỉ hỗ trợ viết kịch bản.
Không tự gắn nhãn thì YouTube tự gắn và xử phạt "repeated or serious cases".
Quyền thương mại Flow theo docs chính thức (mã 16353333): "original
generated content isn't claimed by Google; full Terms of Service apply."
Trên tài khoản đang dùng, Flow hiện dòng nguyên văn "Visible watermarking is required in your region", tức khu vực này bị bắt buộc gắn watermark hiển thị và không tắt được từ giao diện. Nhóm chưa đối chiếu văn bản quy định nào nên `[chưa xác minh cơ sở pháp lý]`.

Lời khuyên, không phải quy định chính thức: enforcement được ghi nhận là
theo cả kênh, một video lỗi pattern có thể kéo mất monetization toàn kênh
(case Bible Stories ~588K sub, ~30 nghìn đô/tháng, demonetize toàn kênh vì
pattern lặp template [1 nguồn, alici.ai]). Giảm rủi ro bằng cách đặt tên
riêng cho persona, đổi format giữa các video, thêm lớp commentary, trộn
footage không phải AI, làm thumbnail theo hệ thống riêng thay vì template,
bật disclosure khi cần, lưu production log làm bằng chứng, và khi bị gắn cờ
thì remediate rồi kháng nghị trong 21 ngày thay vì xoá hàng loạt. Tránh
nhạc/hình có bản quyền, ưu tiên nhạc tự sinh bằng Lyria.

## Tự soát nguồn

- Bảng nền tảng, phân loại dạng nội dung: tổng hợp từ 4 video đầu cộng kênh
  @nontechlamAI, không phải danh sách chính thức của Google; thời lượng
  ngọt là kinh nghiệm cộng đồng. Giới hạn Shorts chưa có số, đã bỏ số cũ vì
  không nguồn.
- Bảng credit Flow và pricing mục 5: đọc trực tiếp panel Flow ngày
  06/09/2026, khớp support.google.com/flow/answer/16526234; Video Resizer và
  Type Overlays 0 credit đo bằng ffprobe cùng đối chiếu ledger cùng ngày.
  Mức bằng chứng cao nhất trong file này.
- Ba dòng sửa video (40 credit), nâng 1080p (miễn phí cho người trả phí),
  nâng 4K (50 credit, chỉ Ultra), và mục "quy trình rẻ nhất: nháp 360p rồi
  nâng độ phân giải": đọc lại trực tiếp support.google.com/flow/answer/16526234
  tại `support.google.com/flow/answer/16526234`, đọc 08/09/2026 [doc]; mốc 27/08/2026 lấy từ
  changelog chính thức và blog Google Labs, xem `changelog.md`.
- "Veo 3.1 Lite [Lower Priority]" chỉ dành Ultra: changelog chính thức
  flow.google.com/changelogs, mục 10/04/2026; số "0 credit" đến từ một bài
  đăng mạng xã hội cùng ngày, mức bằng chứng trung bình.
- NotebookLM đổi tên Gemini Notebook: blog.google ngày 16/07/2026 (tác giả
  Josh Woodward), đối chiếu quan sát trực tiếp trên màn hình video hướng dẫn.
- VMEG (180/60/60/6 credit): modal thật trên màn hình lúc submit lệnh dịch,
  credit riêng không quy đổi được sang VNĐ hay credit Flow.
- UGC (15.000đ, 45 credit), giới hạn 20 video/ngày của Gemini Notebook, và
  multi-track audio ngôn ngữ YouTube: đều là lời kể/transcript chủ quan của
  người làm video, chưa đối chiếu bảng giá hay thông báo chính thức nào,
  [chưa xác minh].
- Monetization/policy: định nghĩa inauthentic content, disclosure, quyền
  thương mại Flow là chính sách công khai đọc được; case Bible Stories và
  checklist chống demonetize là suy luận/kinh nghiệm cộng đồng, không phải
  văn bản chính sách.
