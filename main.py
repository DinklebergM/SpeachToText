"""
Whisper Transcription App - Main Entry Point
"""
import os
import sys

# Add the project root directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.app import WhisperApp

if __name__ == "__main__":
    # Check if FFmpeg is available
    ffmpeg_present = False
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.exists(os.path.join(path, "ffmpeg.exe")):
            ffmpeg_present = True
            break

    if os.path.exists("ffmpeg.exe"):
        ffmpeg_present = True
        print("FFmpeg found in current directory.")

    if not ffmpeg_present:
        print("WARNING: FFmpeg not found. Audio processing might fail.")
        print("Please download ffmpeg.exe and save it in the application directory.")
    
    # Start the application
    app = WhisperApp()
    app.mainloop()