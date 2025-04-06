import subprocess
import os
import argparse
from pathlib import Path

def embed_subtitles(video_path, srt_path, output_path):
    print("開始進行字幕嵌入處理...")

    # 檢查檔案是否存在
    if not os.path.exists(video_path):
        print("影片檔案不存在。")
        return

    # 定義 FFmpeg 命令，使用 force_style 調整字體大小
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "error",
        "-i", video_path,
        "-vf", f"subtitles={srt_path}:force_style='FontSize=22'",
        output_path
    ]

    try:
        print("正在執行 FFmpeg 命令以嵌入字幕...")
        subprocess.run(command, check=True)
        print("字幕嵌入成功，輸出檔案為：", output_path)
    except subprocess.CalledProcessError as e:
        print("執行 FFmpeg 發生錯誤：", e)

def parse_args():
    parser = argparse.ArgumentParser(description="自動上字幕工具")
    parser.add_argument("video", help="輸入影片檔案的路徑")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    # 使用 pathlib 處理路徑
    video_path = Path(args.video)

    # 建立 output 目錄（如果不存在）
    output_dir = Path("output")
    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    subtitle_file = output_dir / video_path.with_suffix(".srt").name
    output_file = output_dir / video_path.name

    # 轉換為 POSIX 格式，確保跨平台正確性
    video_path_str = video_path.as_posix()
    subtitle_str = subtitle_file.as_posix()
    output_str = output_file.as_posix()

    # 列印檔案路徑
    print(f"Video Path: {video_path_str}")
    print(f"Subtitle File: {subtitle_str}")
    print(f"Output File: {output_str}")

    # 嵌入字幕到影片
    embed_subtitles(video_path_str, subtitle_str, output_str)
