"""
Whisper Transcription Application
---------------------------------
A GUI application for transcribing audio files using OpenAI's Whisper model.
"""

# Make the main packages available at the root level
from . import gui
from . import models
from . import utils
from . import localization
from . import config

__version__ = '1.0.0'