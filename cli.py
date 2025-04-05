import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="自動上字幕工具")
    parser.add_argument("video", help="輸入影片檔案的路徑")
    parser.add_argument("--model", help="選擇 Whisper 模型（例如：tiny, base, small, medium, large），預設為 base", default="base")
    return parser.parse_args()
