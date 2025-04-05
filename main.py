from cli import parse_args
from generate import video_to_srt
from embed import embed_subtitles
from utils import setup_logging, check_file_exists
from pathlib import Path

def main():
    setup_logging()
    args = parse_args()

    # 使用 pathlib 處理路徑
    video_path = Path(args.video)

    model = args.model
    if model is None:
        # 如果沒有指定模型，則使用預設模型 "base"
        model = "base"


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

    # 檢查輸入影片檔案是否存在
    check_file_exists(video_path_str)

    # 生成 SRT 字幕檔，並將 model 參數傳入 generate 模組
    video_to_srt(video_path_str, model)
    # 嵌入字幕到影片
    embed_subtitles(video_path_str, subtitle_str, output_str)

if __name__ == "__main__":
    main()
