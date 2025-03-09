# Whisper Transcription App Installation Guide

## Overview

The Whisper Transcription App is a GUI application that transcribes audio files using OpenAI's Whisper model. This guide provides detailed instructions for installing and setting up the application from GitHub.

## System Requirements

- Python 3.8 or newer
- 4GB RAM minimum (8GB recommended for "large" model)
- Windows, macOS, or Linux
- NVIDIA GPU with CUDA support (optional, for faster transcription)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/whisper-transcription-app.git
cd whisper-transcription-app
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If there's no requirements.txt file, install the following packages:

```bash
pip install customtkinter torch torchaudio whisper soundfile pydub numpy
```

### 4. Rename Files with Hyphens

The application uses files with underscores in imports, but some files may have hyphens. Rename the following files:

- `transcription-engine.py` → `transcription_engine.py`
- `audio-processor.py` → `audio_processor.py`
- `file-operations.py` → `file_operations.py`
- `status-tracker.py` → `status_tracker.py`
- `ui-components.py` → `ui_components.py`

### 5. Install FFmpeg

FFmpeg is required for processing various audio formats:

#### Windows

1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract the downloaded archive
3. Place `ffmpeg.exe` in the application directory or add it to your system PATH

#### macOS

```bash
brew install ffmpeg
```

#### Linux

```bash
sudo apt update
sudo apt install ffmpeg
```

### 6. Run the Application

```bash
# From the project root directory
python main.py
```

## Troubleshooting

### Common Issues

#### ModuleNotFoundError

If you see errors like `ModuleNotFoundError: No module named 'models.transcription_engine'`, ensure you've renamed the files as described in step 4.

#### FFmpeg Not Found

If you get a warning about FFmpeg not being found:

- Ensure FFmpeg is installed and accessible in your system PATH
- Or place `ffmpeg.exe` directly in the application directory

#### CUDA/GPU Issues

If you have GPU support but the app uses CPU:

- Ensure you've installed PyTorch with CUDA support
- Check your NVIDIA drivers are up-to-date

## Additional Information

- The application will automatically detect GPU availability for faster transcription
- For large audio files, more RAM might be required
- The first run will download the selected Whisper model (might take time depending on your internet connection)
