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
| Cao | Đọc trực tiếp tài liệu chính thức của Google | ghi `[doc]` kèm URL và ngày đọc |
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

## Bảng năng lực theo model, đọc trước khi chọn model

Nguồn: `support.google.com/flow/answer/16352836`, đọc ngày 08/09/2026 `[doc]`.

| Chế độ | Veo 3.1 Lite | Veo 3.1 Fast | Veo 3.1 Quality | Omni Flash 1.1 |
|---|---|---|---|---|
| Text to Video | 4, 6, 8 giây | 4, 6, 8 giây | 4, 6, 8 giây | 4, 6, 8, 10 giây |
| Frames to Video, chỉ khung đầu | có | có | có | có |
| Frames to Video, khung đầu và khung cuối | có | có | có | có |
| Ingredients to Video | chỉ 8 giây | chỉ 8 giây | **không có** | 4, 6, 8, 10 giây |
| Extend, nối dài clip | chỉ 8 giây | **không có** | **không có** | Coming Soon |
| Sửa video | **không có** | **không có** | **không có** | có, tối đa 10 giây |

Bốn điều ngược trực giác trong bảng này. Chỉ bản **Lite** rẻ nhất mới nối dài được clip.
Bản **Quality** đắt nhất lại không nhận Ingredients, nên không giữ được nhân vật nhất quán.
Chỉ **Omni** mới sửa được video. Và Ingredients trên Veo bị khoá cứng ở 8 giây.

## Bảng giá credit của Flow

Số dưới đây đọc trực tiếp từ nhãn `Generating will use N credits` mà chính Flow
hiện ra trước khi sinh, trên tài khoản gói AI Pro, ngày 06/09/2026.

| Model | 4s | 6s | 8s | 10s |
|---|---|---|---|---|
| Omni 1.1 Flash, 360p | 4 | 5 | 6 | 7 |
| Omni 1.1 Flash, 720p | 7 | 10 | 12 | 15 |
| Veo 3.1 Lite | 10 mỗi lần sinh, Ultra còn 5 | | | |
| Veo 3.1 Fast | 20, Ultra còn 10 | | | |
| Veo 3.1 Quality | 100 ở mọi hạng, và chỉ có 8 giây | | | |

Ba dòng nữa không nằm trong bảng trên vì chúng không phải sinh clip, đọc từ trang chính
thức `support.google.com/flow/answer/16526234` ngày 08/09/2026:

| Việc | Giá |
|---|---|
| Sửa một video, chỉ Gemini Omni Flash làm được | 40 credit |
| Nâng lên 1080p | miễn phí cho người có gói trả phí |
| Nâng lên 4K | 50 credit, và chỉ gói Ultra |

Con số 40 đáng nhớ vì nó **đắt hơn sinh mới**. Một clip 10 giây ở 720p chỉ tốn 15 credit.
Chỉ sửa khi cần giữ lại phần lớn khung hình cũ, còn muốn đổi nội dung thì sinh lại rẻ hơn.

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

1. **Luôn nháp ở Omni 360p trước, rồi NÂNG CẤP chứ đừng sinh lại.** Đây là điểm đã thay
   đổi từ bản cập nhật ngày 27/08/2026. Trước kia nháp xong phải sinh lại ở độ phân giải
   cao, tức trả tiền hai lần. Nay nâng chính clip đó lên 1080p không mất thêm credit cho
   người có gói trả phí. Nâng lên 4K thì tốn 50 credit và chỉ gói Ultra
   `[doc, support.google.com/flow/answer/16526234, 08/09/2026]`. Riêng việc nâng từ 360p
   lên 720p có nguồn bên thứ ba nói miễn phí, nhưng bảng chính thức không có dòng đó,
   nên `[chưa xác minh]`, hãy tự đọc nhãn credit trước khi bấm.
   Cách ép nháp mạnh nhất là đặt Agent instruction, xem `flow-core.md` mục 7.3.
2. **Báo giá trước khi sinh.** Flow hiện sẵn số credit ngay trong panel cài đặt, dạng
   `Generating will use N credits`. Đọc con số đó và nói cho người dùng biết trước khi bấm.
   Từ 08/09/2026, nhãn này là nguồn số dư đáng tin DUY NHẤT còn lại: trang
   `one.google.com/ai/activity` nay hiện `AI credits: 0` kèm dòng *"AI credits included with
   your plan have been replaced by product-based usage limits"*, tức sổ credit cũ đã đổi cơ
   chế `[live 08/09/2026]`. Đừng dùng trang đó để đối chiếu nữa.
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
| Thời lượng và độ phân giải của Veo | **Trong Flow không chọn được**, cả ba bản Veo. Panel chỉ có Mode, Video type, Aspect ratio, model, số lượng. Chỉ Omni mới có hai ô này | Muốn đổi thời lượng Veo thì phải đi API. Bảng năng lực nói Veo hỗ trợ 4, 6, 8 giây là nói ở cấp model, không phải cấp giao diện | `[live 08/09/2026]` thử đủ ba model Veo, cả hai Video type, có và không có ảnh Start |
| Độ phân giải video | Sinh ra ở 360p hoặc 720p, rồi nâng lên 1080p hoặc 4K trong menu `Download media` | Skill từng nói Flow chỉ có 720p, điều đó đã lạc hậu từ 27/08/2026. Trên Pro, `1080p Upscaled` dùng được còn `4K Upscaled` bị khoá kèm link nâng gói | `[live 08/09/2026]` đọc menu tải về |
| Nối dài clip trong Flow | Chỉ Veo 3.1 Lite, mỗi lần 8 giây. Nút tên `Extend (Veo 3.1 - Lite)` và **giấu trong menu của nút `Add clip` ở timeline** | Muốn cảnh liền mạch dài thì phải chọn Lite ngay từ đầu. Trên clip do Omni sinh, nút này luôn bị vô hiệu hoá | `[doc]` bảng năng lực, `[live 08/09/2026]` xác nhận nhãn và vị trí |
| Nối dài clip qua API | Veo tới 148 giây đầu ra, Omni tới 40 giây | API mạnh hơn giao diện rất nhiều ở điểm này | `[doc]` trang Veo và Omni trên ai.google.dev |
| Sửa video | Chỉ Gemini Omni Flash, video tối đa 10 giây, tốn 40 credit | Sinh mới thường rẻ hơn sửa | `[doc]` bảng năng lực và bảng giá chính thức |
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

Thư mục `scripts/` có 13 file Python: 9 file cho đường B tức đường gọi API, 3 file
cho các đường miễn phí đỡ tốn quota Google, và 1 script bảo trì chính tài liệu này.
Đây là phần duy nhất của skill chạy được không cần trình duyệt.

| Script | Làm gì |
|---|---|
| `doctor.py` | **Chạy đầu tiên trên máy mới.** Kiểm tra Python, khoá API, ffmpeg, ffprobe, node, npx, yt-dlp, curl, rồi nói thiếu gì và cài bằng lệnh nào trên đúng hệ điều hành |
| `config.py` | Đọc key từ biến môi trường `GEMINI_API_KEY` hoặc `~/.gemini_key`, giữ danh sách model |
| `write_script.py` | Sinh kịch bản và chia shot, xuất ra `spec.json` |
| `generate_image.py` | Sinh ảnh bằng Nano Banana |
| `generate_video.py` | Sinh một clip bằng Veo hoặc Omni. Có `--resolution` và `--reference-images`, và tự chặn trước các tổ hợp tham số mà API sẽ từ chối |
| `generate_audio.py` | Sinh giọng đọc bằng TTS và nhạc nền bằng Lyria |
| `assemble_video.py` | Nối clip, trộn tiếng, đổi tỉ lệ, xuất bản cuối |
| `upload_video.py` | Chỉ sinh file metadata JSON, không tải lên đâu cả |
| `pipeline.py` | Điều phối các bước trên theo `spec.json` |
| `gen_toc.py` | Bảo trì, không dính tới sản xuất video. Sinh lại mục lục kèm số dòng cho mọi file trong `references/`. **Chạy lại sau mỗi lần sửa file reference**, nếu không số dòng trong mục lục sẽ lệch. Dùng `--check` để chỉ báo lệch mà không ghi |

Ba script dưới đây dùng bậc miễn phí của bên ngoài Google, để dành quota Veo và
Gemini cho việc thật sự cần. Đều tuỳ chọn, thiếu key thì skill vẫn chạy đủ.

| Script | Làm gì | Cần gì |
|---|---|---|
| `fetch_stock.py` | Tải ảnh và video stock từ Pexels làm B-roll. **Cảnh nào không cần nhân vật nhất quán thì lấy stock, đừng sinh bằng Veo.** Đây là cách tiết kiệm credit hiệu quả nhất. Pexels cho dùng thương mại, không bắt ghi công, nhưng script vẫn ghi sẵn danh sách tác giả ra file | `PEXELS_API_KEY`, đăng ký miễn phí |
| `generate_image_cf.py` | Sinh ảnh bằng FLUX.1 schnell trên Cloudflare Workers AI, 10.000 Neuron mỗi ngày miễn phí, không cần thẻ. Hợp cho ảnh nháp và ảnh nền. **KHÔNG nhận ảnh tham khảo nên không giữ được nhân vật nhất quán** — cần nhất quán thì vẫn phải dùng Nano Banana hoặc Characters trong Flow | `CLOUDFLARE_ACCOUNT_ID` và `CLOUDFLARE_API_TOKEN` |
| `generate_audio_edge.py` | Giọng đọc miễn phí có tiếng Việt qua edge-tts. Hợp để đo độ dài lời đọc trước khi dựng hình. **Không phải API chính thức của Microsoft**, là bản dịch ngược dịch vụ Read Aloud của Edge, có thể bị chặn bất cứ lúc nào, nên chỉ dùng cho bản nháp, đường chính vẫn là Gemini TTS | `pip install edge-tts` |

Chạy `doctor.py` để biết đang thiếu key hay gói nào và lấy ở đâu.

Chạy từng bước một, đừng chạy hết một mạch, vì mỗi bước đều tốn tiền API:

```bash
python pipeline.py --spec spec.json --stage video --model omni
```

Bốn điều cần biết trước khi dùng. Thứ nhất, `generate_video.py` gọi Omni qua
`POST /v1beta/interactions` và đặt tỉ lệ khung hình bằng `response_format.aspect_ratio`.
Trước ngày 08/09/2026 nó nhét tỉ lệ vào giữa câu prompt tiếng Anh vì lúc đó chưa biết có
tham số này, và đó là một lỗi thật đã sửa. Thứ hai, `assemble_video.py` sẽ **dừng và báo**
nếu các clip khác độ phân giải, vì nối thẳng sẽ mất chất lượng mà không ai hay.
Thứ hai, nếu lời đọc dài hơn hình, script giữ khung hình cuối cho đủ tiếng và in
cảnh báo kèm số giây. Thứ ba, `pipeline.py` dừng ngay khi một bước con lỗi thay
vì chạy tiếp trên dữ liệu hỏng.

## Quy tắc tra cứu khi nghi ngờ

Khi người dùng hỏi một tính năng có tồn tại hay không, **đừng chỉ mở giao diện ra
xem**. Giao diện chỉ cho biết tài khoản này thấy gì, không cho biết tính năng có
tồn tại ở gói khác, vùng khác, mới ra hay vừa bị gỡ. Hãy mở song song bốn nguồn.

| Nguồn | Địa chỉ | Trả lời được câu hỏi gì |
|---|---|---|
| Giao diện | `flow.google.com` | Tài khoản này hiện thấy gì |
| Bảng năng lực | `support.google.com/flow/answer/16352836` | Model nào làm được chế độ nào, thời lượng nào |
| Bảng giá | `support.google.com/flow/answer/16526234` | Giá từng việc, kể cả sửa và nâng độ phân giải |
| Changelog | `flow.google.com/changelogs` và `ai.google.dev/gemini-api/docs/changelog` | Có từ bao giờ, cho gói nào |

Hai bài học, cả hai đều là lần suýt kết luận sai.

Lần thứ nhất, mục `Veo 3.1 Lite - Lower Priority` không có trên tài khoản Pro, nhưng
changelog chính thức ngày 10/04/2026 ghi rõ nó tồn tại và dành riêng cho gói Ultra.

Lần thứ hai, ngày 08/09/2026 skill vẫn dừng ở mục changelog ngày 26/08/2026 và tưởng đó là
mới nhất. Thực ra ngay hôm sau, ngày 27/08/2026, blog chính thức đã công bố Start and End
Frames, xuất 1080p và 4K, cùng quy trình nháp 360p rồi nâng cấp. Changelog của Flow đi
chậm hơn blog và chậm hơn changelog của Gemini API, nên **chỉ đọc changelog của Flow là
không đủ**.

## Kịch bản thường gặp

| Người dùng muốn | Làm gì |
|---|---|
| Một clip thử nhanh | Omni 360p, 4 giây, hết 4 credit |
| Video kể chuyện nhiều cảnh | Tạo Character trước, rồi gọi bằng cú pháp `@tên_nhân_vật` ngay trong prompt, nhanh hơn gắn ảnh thủ công. Đưa chính mình vào cảnh thì dùng `@me`, nhưng không dùng được ở EEA, Anh và Thuỵ Sĩ |
| Video dọc cho Shorts hoặc TikTok | Đặt 9:16 ngay từ đầu, đừng sinh 16:9 rồi cắt |
| Tỉ lệ lạ như 4:3, 21:9, hoặc số đo riêng | Sinh 16:9 rồi qua Video Resizer. Đo hai lần không thấy trừ credit, nhưng Flow vẫn cảnh báo `This Tool may consume credits` |
| Chữ tiếng Việt chính xác trên hình | Type Overlays, hoặc dựng bằng Remotion |
| Thoại tiếng Việt nghe tự nhiên | Sinh video không lồng tiếng, lồng tiếng riêng rồi ghép |
| Một video ra nhiều thứ tiếng | Đường VMEG trong `other-routes.md` |
| Video từ tài liệu dài | Gemini Notebook, mục Video Overview |
| Chữ động, biểu đồ, đồ hoạ dữ liệu | Claude Code với Remotion |
| Một cảnh liền mạch dài hơn 10 giây | Trong Flow thì chỉ Veo 3.1 Lite nối dài được, mỗi lần 8 giây. Cần dài hơn nữa thì đi API, Veo cho tới 148 giây và Omni cho tới 40 giây |
| Sửa một video đã có, giữ phần lớn khung hình | Gemini Omni Flash, video tối đa 10 giây, tốn 40 credit. Nếu chỉ đổi nội dung thì sinh lại rẻ hơn |
| Cần bản 4K | Nâng độ phân giải, tốn 50 credit và chỉ gói Ultra. Gói Pro dừng ở 1080p |
| Nối hai ảnh thành một chuyển động | Frames to Video. Trên giao diện hai nút tên là `Start` và `End`, không phải First và Last |
| Đăng video lên YouTube | Nếu video làm hoàn toàn trong Flow thì chuột phải lên nó rồi chọn `Publish to YouTube`, có sẵn trong Flow. Script `upload_video.py` của skill KHÔNG tải lên, nó chỉ sinh file metadata |

## Trước khi nói đã xong

Bắt buộc làm đủ bốn việc sau rồi mới báo hoàn thành.

1. Tải file về máy, không chỉ nhìn thấy nó nằm trong thư viện.
2. Chạy `ffprobe` và đọc ra kích thước, thời lượng, có tiếng hay không.
3. Nếu video có thoại hoặc có chữ, mở một khung hình ra xem hoặc nghe lại để đối
   chiếu với kịch bản.
4. Nói cho người dùng biết đã tiêu hết bao nhiêu credit.

Nếu bất cứ bước nào không làm được, hãy nói thẳng là chưa xác minh, đừng nói xong.
