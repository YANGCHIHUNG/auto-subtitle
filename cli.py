import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="自動上字幕工具")
    parser.add_argument("video", help="輸入影片檔案的路徑")
    return parser.parse_args()
