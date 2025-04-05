import os
import logging

def setup_logging():
    """初始化並設置基本的日誌設定"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def check_file_exists(filepath):
    """檢查檔案是否存在，若不存在則記錄錯誤並引發 FileNotFoundError"""
    if not os.path.exists(filepath):
        logging.error(f"找不到檔案: {filepath}")
        raise FileNotFoundError(f"找不到檔案: {filepath}")
