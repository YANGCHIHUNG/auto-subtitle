# Auto Subtitle Tool

This project provides an automated solution for generating subtitles (SRT files) from a video and embedding those subtitles into the video. It leverages the Whisper model to extract audio and create an SRT file, and uses FFmpeg to overlay the subtitles onto the video.

> **Note:** This tool is specially designed for Traditional Chinese (繁體中文) applications, ensuring accurate handling of Traditional Chinese text in subtitles.

## Demo

<p align="center">
  <img src="static/demo.gif" alt="Demo 1" width="45%">
  <img src="static/demo_subtitle.gif" alt="Demo 2" width="45%">
</p>

## Features

- **Automatic Subtitle Generation:**  
  Uses the Whisper model (`generate.py`) to process a video and create an SRT file.

- **Subtitle Embedding:**  
  Uses FFmpeg (`embed.py`) to embed the SRT file into the video, producing a final video with subtitles.

- **Command Line Interface:**  
  Automatically generates and saves output files in the `output/` directory when provided with a video path.

- **Manual Subtitle Editing:**  
  Edit the generated SRT file and use `embed.py` to embed the modified subtitles into the video.

## Installation

### Prerequisites

- Python 3.7 or higher
- **FFmpeg installed and available in your system PATH (verify by running `ffmpeg -version`)**
- Necessary Python packages (see `requirements.txt`)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/YANGCHIHUNG/auto-subtitle.git
   ```

2. **Create a Virtual Environment (Recommended):**

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Packages:**

   Use the provided `requirements.txt` to install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The tool can be used in two main ways:

### 1. Full Workflow (Generate Subtitles & Embed Them)

If you only provide the path to the input video, the program will automatically generate an SRT file and embed the subtitles. All output files (the generated SRT file and the final video) will be saved in the `output/` folder.

Additionally, you can select which Whisper model to use with the --model option.

The Whisper model provides several options that you can choose based on your requirements. The available models are:

- `tiny`
- `base`
- `small`
- `medium`
- `large`

Example command:
```bash
python main.py path/to/input_video.mp4 --model large
```
If you do not specify the --model option, the tool will use the default model (e.g., `large`).

### 2. Embedding Subtitles Only

If you have manually edited the generated SRT file or already have an SRT file, you can run the embedding functionality directly using `embed.py`.

Example command:
```bash
python embed.py path/to/input_video.mp4 path/to/your_subtitle.srt --output path/to/output_video.mp4
```

If the `--output` option is not provided, the output video will be saved in the `output/` folder with the same filename as the input video.

### Additional Notes

- **Output Location:**  
  When running the full workflow (i.e., only providing the input video), both the generated SRT file and the output video will automatically be stored in the `output/` directory.

- **Manual Subtitle Editing:**  
  After generating the SRT file, you can open and edit it using your preferred text editor. Once you have made your changes, run the embedding functionality (as shown above) to update the subtitles in your video.

- **Working Directory:**  
  Ensure you run the commands from the project root (or adjust your paths accordingly) so that relative paths are resolved correctly.

- **Traditional Chinese Support:**  
  This tool is designed with Traditional Chinese (繁體中文) in mind, ensuring that subtitles are generated and embedded with proper handling of Traditional Chinese characters.
