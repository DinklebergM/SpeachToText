"""
Handles the Whisper model and transcription processes.
"""
import torch
import whisper
import threading

class TranscriptionEngine:
    """Handles the Whisper model loading and transcription."""
    
    def __init__(self, status_callback=None):
        """Initialize the transcription engine.
        
        Args:
            status_callback: Callback function for status updates
        """
        self.model = None
        self.model_size = "small"  # Default
        self.device = self._detect_device()
        self.status_callback = status_callback
        self.is_loading = False
    
    def _detect_device(self):
        """Detect if a GPU is available for better performance."""
        if torch.cuda.is_available():
            device = "cuda"
            print(f"GPU detected: {torch.cuda.get_device_name(0)}")
        else:
            device = "cpu"
            print("No GPU detected. Using CPU.")
        return device
    
    def get_device_name(self):
        """Get the current device name (GPU/CPU)."""
        return "GPU" if self.device == "cuda" else "CPU"
    
    def load_model(self, model_size, on_complete=None):
        """Load Whisper model in a separate thread.
        
        Args:
            model_size: Size of the model to load
            on_complete: Callback when loading completes
        """
        if self.is_loading:
            return False
        
        self.is_loading = True
        self.model_size = model_size
        
        def load_model_task():
            try:
                # Load model with selected device
                self.model = whisper.load_model(model_size, device=self.device)
                self.is_loading = False
                if on_complete:
                    on_complete(True, None)
            except Exception as e:
                self.is_loading = False
                if on_complete:
                    on_complete(False, str(e))
        
        threading.Thread(target=load_model_task, daemon=True).start()
        return True
    
    def transcribe(self, audio_data, on_complete=None):
        """Transcribe audio data using the loaded model.
        
        Args:
            audio_data: Audio data as numpy array
            on_complete: Callback when transcription completes with
                        (success, transcription, error) parameters
        """
        if not self.model:
            if on_complete:
                on_complete(False, None, "Model not loaded")
            return False
        
        def transcribe_task():
            try:
                # Transcribe using loaded model
                result = self.model.transcribe(audio_data)
                transcription = result["text"]
                
                if on_complete:
                    on_complete(True, transcription, None)
            except Exception as e:
                if on_complete:
                    on_complete(False, None, str(e))
        
        threading.Thread(target=transcribe_task, daemon=True).start()
        return True
    
    def estimate_processing_time(self, audio_duration, model_factors):
        """Estimate processing time based on audio duration and model.
        
        Args:
            audio_duration: Duration of audio in seconds
            model_factors: Dictionary of processing time factors for each model size
            
        Returns:
            float: Estimated processing time in seconds
        """
        factor = model_factors.get(self.model_size, 1.0)
        
        if self.device == "cuda":
            # GPU is faster
            return audio_duration * factor * 0.1
        else:
            # CPU is slower
            return audio_duration * factor * 0.3
