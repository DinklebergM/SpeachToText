"""
Audio file loading and processing.
"""
import os
import numpy as np
import soundfile as sf
from pydub import AudioSegment

class AudioProcessor:
    """Process audio files for transcription."""
    
    def __init__(self):
        """Initialize audio processor."""
        pass
    
    def load_audio(self, file_path):
        """Load and process audio file from various formats.
        
        Args:
            file_path: Path to the audio file
            
        Returns:
            np.array: Processed audio data as a numpy array
            
        Raises:
            Exception: If there's an error processing the audio
        """
        file_ext = os.path.splitext(file_path)[1].lower()
        
        try:
            if file_ext == ".ogg":
                data, sample_rate = sf.read(file_path)
                if len(data.shape) > 1:
                    data = data.mean(axis=1)
            elif file_ext == ".mp3":
                sound = AudioSegment.from_mp3(file_path)
                temp_wav = os.path.join(os.path.dirname(file_path), "_temp_whisper.wav")
                sound.export(temp_wav, format="wav")
                data, sample_rate = sf.read(temp_wav)
                os.remove(temp_wav)
            elif file_ext == ".wav":
                data, sample_rate = sf.read(file_path)
                if len(data.shape) > 1:
                    data = data.mean(axis=1)
            else:
                sound = AudioSegment.from_file(file_path)
                temp_wav = os.path.join(os.path.dirname(file_path), "_temp_whisper.wav")
                sound.export(temp_wav, format="wav")
                data, sample_rate = sf.read(temp_wav)
                os.remove(temp_wav)
            
            # Ensure consistent data type (float32) to prevent type mismatches
            data = np.asarray(data, dtype=np.float32)
            return data
            
        except Exception as e:
            raise Exception(f"Error processing audio: {str(e)}")
    
    def get_audio_duration(self, audio_data):
        """Estimate audio duration in seconds (assuming 16kHz sample rate).
        
        Args:
            audio_data: Audio data as numpy array
            
        Returns:
            float: Estimated duration in seconds
        """
        return len(audio_data) / 16000  # Assuming 16kHz sample rate
