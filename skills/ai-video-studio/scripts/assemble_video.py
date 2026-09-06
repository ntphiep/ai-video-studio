"""Lắp ráp các shot video + narration + nhạc nền thành MP4 chuẩn YouTube,
dùng ffmpeg.

Đầu vào: danh sách clip video (theo thứ tự), file narration, file nhạc nền (tuỳ chọn).
Xuất theo chuẩn: H.264 High, AAC-LC, 48kHz, 24fps, 16:9 hoặc 9:16.

Cách dùng (nếu chỉ nối clip không audio):
  python assemble_video.py --clips c1.mp4 c2.mp4 c3.mp4 --out final.mp4

Với narration + nhạc:
  python assemble_video.py --clips c1.mp4 c2.mp4 --narration voice.mp3 \
      --music bgm.mp3 --out final.mp4

Đọc không giới hạn số clip. Bước nối dùng concat demuxer với `-c copy` (không
re-encode). NHƯNG bước xuất cuối LUÔN re-encode bằng libx264 để chuẩn hoá
fps/pixel format/bitrate, nên tổng cộng video được encode lại một lần. Nếu
muốn giữ nguyên bit gốc thì dùng thẳng file ở bước nối.
"""
import argparse
import os
import subprocess
import sys

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
# Ép UTF-8 cho stdout/stderr để script chạy được mà không cần set biến môi trường.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass



def probe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        return 0.0


def concat_clips(clips, listfile):
    """Tạo concat list cho ffmpeg, và KIỂM THẬT rằng mọi clip cùng độ phân giải.

    ffmpeg concat demuxer nối mù: nếu các clip khác kích thước, nó ép hết về
    kích thước của clip đầu tiên mà không báo gì. Luồng của skill này rất dễ
    dính, vì hướng dẫn là nháp ở 360p rồi render bản cuối ở 720p, nên trong
    cùng một thư mục luôn có sẵn cả hai loại.
    """
    dims = [(c, _dimensions(c)) for c in clips]
    unknown = [c for c, d in dims if d == (0, 0)]
    if unknown:
        raise SystemExit("Không đo được kích thước của: " + ", ".join(unknown))
    if len({d for _, d in dims}) > 1:
        chi_tiet = "; ".join(f"{os.path.basename(c)}={d[0]}x{d[1]}" for c, d in dims)
        raise SystemExit(
            "Các clip KHÁC độ phân giải nên không nối trực tiếp được: " + chi_tiet
            + ". ffmpeg sẽ ép hết về kích thước clip đầu tiên và bạn mất chất lượng "
            "mà không hề được báo. Hãy đưa mọi clip về cùng kích thước trước, "
            "xem references/format-and-export.md mục 5."
        )
    with open(listfile, "w") as f:
        for c in clips:
            # escape đường dẫn chứa ký tự đặc biệt
            f.write(f"file '{os.path.abspath(c)}'\n")



def _ffprobe(args_list):
    """Chạy ffprobe, trả stdout đã strip; trả "" nếu lỗi."""
    try:
        out = subprocess.run(["ffprobe", "-v", "error"] + args_list,
                             capture_output=True, text=True, check=True)
        return out.stdout.strip()
    except Exception:
        return ""


def _has_audio(path):
    """True nếu file có ít nhất một audio stream."""
    return bool(_ffprobe(["-select_streams", "a", "-show_entries",
                          "stream=codec_type", "-of", "csv=p=0", path]))


def _dimensions(path):
    """Trả (width, height) đo bằng ffprobe, hoặc (0, 0) nếu không đo được."""
    out = _ffprobe(["-select_streams", "v:0", "-show_entries", "stream=width,height",
                    "-of", "csv=p=0", path])
    try:
        parts = [int(x) for x in out.strip().split(",")[:2]]
        return parts[0], parts[1]
    except Exception:
        return 0, 0


def _bitrate_for(path):
    """Bitrate theo ĐỘ PHÂN GIẢI: cạnh ngắn từ 1080 trở lên thì 8M, dưới thì 5M.

    Phải lấy CẠNH NGẮN chứ không phải chiều cao. Clip dọc 720x1280 có chiều cao
    1280 nhưng thực chất là 720p; nếu chỉ nhìn chiều cao sẽ gán nhầm 8M và làm
    file phình lên vô ích. Khung dọc 720p chính là khung Shorts phổ biến nhất.
    """
    w, h = _dimensions(path)
    if not w or not h:
        return "5M"          # không đo được thì chọn mức an toàn
    short_side = min(w, h)
    return "8M" if short_side >= 1080 else "5M"

def convert_aspect(path, target):
    """Đổi tỉ lệ khung của file tại chỗ, dùng đúng hai lệnh đã chạy thử thật.

    Nguồn hai bộ lọc: references/format-and-export.md mục 5, đã đo bằng ffprobe
    ra đúng 720x1280 và 1920x1080. Trả True nếu có đổi, False nếu vốn đã đúng.
    """
    w, h = _dimensions(path)
    if not w or not h:
        print("Không đo được kích thước nên bỏ qua bước đổi tỉ lệ.")
        return False
    dang_doc = h > w
    muon_doc = target == "9:16"
    if dang_doc == muon_doc:
        return False          # đã đúng hướng khung, không đụng vào
    if muon_doc:
        vf = "crop=ih*9/16:ih,scale=720:1280"
    else:
        vf = "scale=-2:1080,pad=1920:1080:(ow-iw)/2:0"
    tmp = path + ".aspect.mp4"
    print(f"Đổi tỉ lệ {w}x{h} sang {target}: ffmpeg -vf \"{vf}\"")
    subprocess.run(["ffmpeg", "-y", "-i", path, "-vf", vf,
                    "-c:a", "copy", "-preset", "medium", tmp], check=True)
    os.replace(tmp, path)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clips", nargs="+", required=True)
    ap.add_argument("--narration", default=None)
    ap.add_argument("--drop-original-audio", action="store_true",
                    help="Bỏ hẳn audio native của clip. Mặc định là GIỮ và trộn cùng narration/nhạc.")
    ap.add_argument("--original-volume", default="0.6",
                    help="Âm lượng audio gốc khi trộn với narration (mặc định 0.6)")
    ap.add_argument("--music", default=None)
    ap.add_argument("--aspect", default="16:9", choices=["16:9", "9:16"],
                    help="Khung đầu ra. Nếu khác khung nguồn thì file sẽ được "
                         "crop hoặc pad bằng lệnh đã kiểm chứng.")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    if not args.clips:
        print("Đầu vào trống.")
        sys.exit(1)

    listfile = "concat_list.txt"
    concat_clips(args.clips, listfile)

    # Bước 1: nối clip (concat demuxer, copy codec để không re-encode)
    joined = "joined.mp4"
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listfile,
        "-c", "copy",
    ]
    # Nếu có narration/music thì chúng ta mix sau, nên giữ joined chưa có audio video
    cmd += [joined]
    print("Nối clip:", " ".join(cmd))
    subprocess.run(cmd, check=True)

    # Bước 2: mix audio. Mặc định GIỮ audio gốc của clip (Veo/Omni luôn sinh
    # audio native) rồi trộn thêm narration và nhạc nền. Dùng --drop-original-audio
    # nếu muốn bỏ hẳn tiếng gốc.
    if args.narration or args.music:
        # dùng amix nếu cả 2, hoặc chỉ narration/music
        inputs = ["-i", joined]
        if args.narration:
            inputs += ["-i", args.narration]
        if args.music:
            inputs += ["-i", args.music]
        # filter: trộn các stream audio. narration lấy 100%, music giảm volume.
        idx = 1  # joined là input 0
        streams = []
        stream_labels = []   # tên label để amix tham chiếu
        if not args.drop_original_audio and _has_audio(joined):
            # audio native của clip; hạ nhẹ để narration nổi lên trên
            streams.append(f"[0:a]volume={args.original_volume}[orig]")
            stream_labels.append("[orig]")
        if args.narration:
            streams.append(f"[{idx}:a]volume=1.0[nar]")
            stream_labels.append("[nar]")
            idx += 1
        if args.music:
            streams.append(f"[{idx}:a]volume=0.25[bgm]")
            stream_labels.append("[bgm]")
        # amix các stream theo label (KHÔNG dùng số index input).
        # duration=longest chứ KHÔNG phải first. Với first, stream đầu tiên là audio
        # gốc của clip, nên narration dài hơn clip sẽ bị cắt cụt trong im lặng.
        # Đó chính là luồng chính của skill này (clip Flow ngắn, lồng tiếng Việt riêng),
        # nên mặc định phải giữ trọn narration.
        inputs_list = "".join(stream_labels)
        filter_complex = ";".join(streams) + f";{inputs_list}amix=inputs={len(stream_labels)}:duration=longest[aout]"

        # Nếu tiếng dài hơn hình thì kéo dài hình bằng cách giữ khung cuối,
        # nếu không video sẽ hết trước và người xem thấy màn hình đen.
        # CHỈ narration mới được phép kéo dài video. Nhạc nền phải theo hình,
        # nếu không một file nhạc 3 phút sẽ biến clip 16 giây thành 3 phút.
        vid_len = probe_duration(joined) or 0.0
        nar_len = probe_duration(args.narration) if args.narration else 0.0
        target = max(vid_len, nar_len or 0.0)
        if args.music:
            # cắt nhạc cho vừa đúng độ dài cuối cùng
            streams = [x.replace("[bgm]", f",atrim=0:{target:.3f}[bgm]")
                       if x.endswith("[bgm]") else x for x in streams]
            inputs_list = "".join(stream_labels)
            filter_complex = ";".join(streams) +                 f";{inputs_list}amix=inputs={len(stream_labels)}:duration=longest[aout]"
        vmap = "0:v:0"
        pad = target - vid_len
        if pad > 0.05:
            print(
                f"CẢNH BÁO: lời đọc dài {nar_len:.2f}s nhưng hình chỉ {vid_len:.2f}s. "
                f"Giữ khung hình cuối thêm {pad:.2f}s để không mất lời. "
                "Muốn hình khớp tiếng thì thêm clip hoặc cắt bớt lời đọc."
            )
            filter_complex += f";[0:v]tpad=stop_mode=clone:stop_duration={pad:.3f}[vout]"
            vmap = "[vout]"

        cmd = ["ffmpeg", "-y"] + inputs + [
            "-filter_complex", filter_complex,
            "-map", vmap, "-map", "[aout]",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "24",
            "-c:a", "aac", "-ar", "48000", "-ac", "2",
            "-movflags", "+faststart",
        ]
        # bitrate theo ĐỘ PHÂN GIẢI, không theo tỉ lệ khung.
        # Quy tắc ở references/format-and-export.md mục 4.
        bitrate = _bitrate_for(joined)
        cmd += ["-b:v", bitrate, "-preset", "medium", args.out]
    elif args.drop_original_audio:
        # Không có narration lẫn nhạc, mà người dùng yêu cầu bỏ tiếng gốc.
        # Trước đây nhánh này bị bỏ qua nên cờ không có tác dụng gì.
        cmd = ["ffmpeg", "-y", "-i", joined, "-an",
               "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "24",
               "-movflags", "+faststart", "-preset", "medium", args.out]
    else:
        # chỉ nối, thêm audio gốc từ joined (nếu có)
        cmd = ["ffmpeg", "-y", "-i", joined,
               "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "24",
               "-c:a", "aac", "-ar", "48000", "-ac", "2",
               "-movflags", "+faststart", "-preset", "medium", args.out]

    print("Xuất final:", " ".join(cmd))
    subprocess.run(cmd, check=True)

    # Đổi tỉ lệ nếu người dùng yêu cầu khác với khung hiện có.
    # Trước đây cờ --aspect được khai báo nhưng không dòng nào đọc tới,
    # nên người dùng tưởng đã ra khung dọc mà thực tế vẫn khung ngang.
    convert_aspect(args.out, args.aspect)

    # Bước 3: verify
    dur = probe_duration(args.out)
    size = os.path.getsize(args.out)
    print(f"✅ Xong: {args.out} | {size/1024/1024:.1f} MB | {dur:.1f}s")

    # dọn tạm
    for f in (listfile, joined):
        if os.path.exists(f):
            os.remove(f)


if __name__ == "__main__":
    main()
