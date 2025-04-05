import os
import datetime
import srt
import whisper
from moviepy import VideoFileClip
from opencc import OpenCC  # 載入 OpenCC 進行簡體到繁體的轉換

def video_to_srt(video_path, model_name):
    print("開始處理影片轉字幕...")
    
    # 取得影片檔名（不包含副檔名）
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    print(f"處理的影片檔名：{base_name}")
    
    # 檢查 output 資料夾是否存在，若不存在則建立它
    output_folder = "output"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 建立輸出的 SRT 檔名：原檔名加上 _srt，並存放於 output 資料夾中
    srt_filename = os.path.join(output_folder, f"{base_name}.srt")
    print(f"字幕檔案將儲存為：{srt_filename}")
    
    # 1. 從影片中提取音訊，並儲存為臨時檔案
    print("正在從影片中提取音訊...")
    clip = VideoFileClip(video_path)
    audio_path = "temp_audio.wav"
    clip.audio.write_audiofile(audio_path, logger=None)
    print(f"音訊已儲存為臨時檔案：{audio_path}")
    
    # 2. 載入 Whisper 模型並進行語音轉錄
    print("正在載入 Whisper 模型...")
    model = whisper.load_model(model_name)
    model = model.to("cuda")  # 將模型移至 GPU
    print("Whisper 模型已載入，開始進行語音轉錄...")
    result = model.transcribe(audio_path)
    print("語音轉錄完成！")
    
    # 從轉錄結果中取得分段資訊
    segments = result.get("segments", [])
    print(f"取得 {len(segments)} 個轉錄分段。")
    
    # 建立 OpenCC 轉換器 (從簡體中文轉為繁體中文)
    print("正在初始化 OpenCC 簡體到繁體轉換器...")
    cc = OpenCC('s2t')
    
    # 3. 將每個轉錄分段格式化成 SRT 的字幕格式，同時轉換為繁體中文
    print("正在格式化字幕內容...")
    subtitles = []
    for i, segment in enumerate(segments):
        start_seconds = segment.get("start", 0)
        end_seconds = segment.get("end", 0)
        text = segment.get("text", "").strip()
        # 轉換文字為繁體中文
        text_traditional = cc.convert(text)
        subtitle = srt.Subtitle(
            index=i + 1,
            start=datetime.timedelta(seconds=start_seconds),
            end=datetime.timedelta(seconds=end_seconds),
            content=text_traditional
        )
        subtitles.append(subtitle)
    print("字幕內容格式化完成。")
    
    # 將字幕內容合併成 SRT 格式
    print("正在合併字幕內容為 SRT 格式...")
    srt_content = srt.compose(subtitles)
    
    # 將 SRT 內容寫入檔案
    with open(srt_filename, "w", encoding="utf-8") as f:
        f.write(srt_content)
    
    print(f"SRT 檔案已成功生成：{srt_filename}")

# 使用範例：
if __name__ == "__main__":
    video_path = r"C:\Users\young\Documents\2025-nchu-spring\auto-subtitle\test_data\output_video_480p.mp4"
    video_to_srt(video_path)
