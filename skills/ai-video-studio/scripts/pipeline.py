"""Điều phối pipeline của skill ai-video-studio.

Chạy từng bước: kịch bản, ảnh keyframe, video từng shot, âm thanh, ghép, rồi
chuẩn bị metadata. Đọc một file spec dạng JSON do write_script.py sinh ra.

QUAN TRỌNG: đây chỉ là lớp điều phối mỏng. Các bước gọi API đều tốn tiền, nên
hãy chạy TỪNG BƯỚC MỘT, dừng lại sau bước render video để người dùng duyệt, và
tuyệt đối không chạy hết một mạch cho video dài.

Mọi lệnh con đều gọi bằng subprocess.run với danh sách tham số, KHÔNG dùng
os.system. Lý do có hai. Thứ nhất, os.system nuốt mã lỗi nên pipeline vẫn báo
thành công dù mọi shot đều hỏng. Thứ hai, prompt của skill này thường chứa dấu
nháy kép cho lời thoại và ký tự và, nội suy vào chuỗi shell sẽ làm mất ký tự
hoặc tách nhầm câu lệnh, nhất là trên PowerShell.

Cách dùng:
  python pipeline.py --spec spec.json --stage script
  python pipeline.py --spec spec.json --stage keyframes
  python pipeline.py --spec spec.json --stage video --model omni
  python pipeline.py --spec spec.json --stage audio
  python pipeline.py --spec spec.json --stage assemble
  python pipeline.py --spec spec.json --stage metadata --title "Video 1"
"""
import argparse
import json
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

HERE = os.path.dirname(os.path.abspath(__file__))


def run(script, *cli_args):
    """Gọi một script cùng thư mục và DỪNG NGAY nếu nó lỗi.

    Trả về CompletedProcess. Dùng check=True để mã lỗi không bị nuốt.
    """
    cmd = [sys.executable, os.path.join(HERE, script), *[str(a) for a in cli_args]]
    print("→", " ".join(cmd))
    return subprocess.run(cmd, check=True)


def load_spec(path):
    if not os.path.exists(path):
        sys.exit(f"Không có spec: {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def run_stage(spec, stage, args):
    if stage == "script":
        print(f"Kịch bản: {spec.get('script','')[:120]}... "
              f"| {len(spec.get('shots', []))} shot")
        return

    if stage == "keyframes":
        run("generate_image.py", spec.get("thumbnail_prompt", ""),
            "--out-prefix", "thumb")
        print("Đã tạo thumbnail, xem thumb_0.png. Chạy keyframe từng shot nếu cần.")
        return

    if stage == "video":
        for sh in spec.get("shots", []):
            out = f"shot_{sh['id']:02d}.mp4"
            dur = sh.get("duration")
            print(f"Shot {sh['id']} ({dur or 'mặc định'}s) sẽ ghi vào {out}")
            cli = [sh["scene_prompt"],
                   "--model", args.model,
                   "--aspect", sh.get("video_format", "16:9"),
                   "--out", out]
            if dur:
                cli += ["--duration", int(dur)]
            run("generate_video.py", *cli)
        return

    if stage == "audio":
        # TTS trả PCM thô nên phải lưu đuôi .wav, xem references/api-guide.md.
        run("generate_audio.py", "--tts", spec.get("voiceover_script", ""),
            "--out", "voice.wav")
        run("generate_audio.py", "--music", spec.get("music_style", "ambient"),
            "--out", "music.wav")
        return

    if stage == "assemble":
        clips = [f"shot_{s['id']:02d}.mp4" for s in spec.get("shots", [])]
        if not clips:
            sys.exit("Spec không có shot nào để ghép.")
        run("assemble_video.py", "--clips", *clips,
            "--narration", "voice.wav", "--music", "music.wav",
            "--out", "final.mp4")
        return

    if stage == "metadata":
        # Bước này CHỈ sinh file metadata JSON, không tải lên đâu cả.
        run("upload_video.py", "--title", args.title, "--file", "final.mp4",
            "--desc", spec.get("script", "")[:100], "--tags", args.tags,
            "--meta-out", "meta.json")
        return

    sys.exit(f"Stage không hợp lệ: {stage}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", default="spec.json")
    ap.add_argument("--stage", required=True,
                    choices=["script", "keyframes", "video", "audio",
                             "assemble", "metadata"])
    ap.add_argument("--model", default="omni",
                    help="Model sinh video. Mặc định omni vì rẻ nhất và là "
                         "model duy nhất chọn được độ phân giải lẫn thời lượng.")
    ap.add_argument("--title", default="Video AI")
    ap.add_argument("--tags", default="ai,video")
    args = ap.parse_args()

    spec = load_spec(args.spec)
    try:
        run_stage(spec, args.stage, args)
    except subprocess.CalledProcessError as e:
        sys.exit(f"Bước '{args.stage}' thất bại, lệnh con trả mã {e.returncode}. "
                 "Pipeline dừng để bạn xử lý thay vì chạy tiếp trên dữ liệu hỏng.")


if __name__ == "__main__":
    main()
