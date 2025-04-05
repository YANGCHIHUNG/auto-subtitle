Below is an example README in English that meets your requirements:

---

# Auto Subtitle Tool

This project provides an automated solution for generating subtitles (SRT files) from a video and embedding those subtitles into the video. It leverages the Whisper model to extract audio and create an SRT file, and uses FFmpeg to overlay the subtitles onto the video.

## Features

- **Automatic Subtitle Generation:**  
  Uses the Whisper model (implemented in `generate.py`) to process an input video and generate a corresponding SRT subtitle file.

- **Subtitle Embedding:**  
  Uses FFmpeg's subtitle filter (implemented in `embed.py`) to embed the generated (or provided) SRT subtitle file into the video, producing a final video with embedded subtitles.

- **Command Line Interface:**  
  The tool is run from the command line. If only the path to the input video is provided, the tool automatically generates the SRT file and saves all output files in an `output/` directory. No need to provide the `--subtitle` and `--output` options in this case.

- **Manual Subtitle Editing:**  
  If you wish to manually edit the generated SRT file, you can do so and then run the "Embedding Subtitles Only" functionality (using `embed.py`) to embed your modified subtitles into the video.

- **Cross-Platform Compatibility:**  
  The project uses Python's `pathlib` module to handle file paths, ensuring compatibility on both Windows and macOS. Special handling for Windows paths is included to avoid parsing errors with FFmpeg.

## Installation

### Prerequisites

- Python 3.7 or higher
- FFmpeg installed and available in your system PATH (verify by running `ffmpeg -version`)
- Necessary Python packages (see `requirements.txt`)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your_username/auto-subtitle.git
   cd auto-subtitle
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

Example command:
```bash
python main.py path/to/input_video.mp4
```

### 2. Embedding Subtitles Only

If you have manually edited the generated SRT file or already have an SRT file, you can run the embedding functionality directly using `embed.py`.

Example command:
```bash
python embed.py path/to/input_video.mp4
```

### Additional Notes

- **Output Location:**  
  When running the full workflow (i.e., only providing the input video), both the generated SRT file and the output video will automatically be stored in the `output/` directory.

- **Manual Subtitle Editing:**  
  After generating the SRT file, you can open and edit it using your preferred text editor. Once you have made your changes, run the embedding functionality (as shown above) to update the subtitles in your video.

- **Working Directory:**  
  Ensure you run the commands from the project root (or adjust your paths accordingly) so that relative paths are resolved correctly.