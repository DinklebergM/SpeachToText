"""
Application settings and configuration.
"""
import customtkinter as ctk

class AppSettings:
    """Application configuration settings."""
    
    def __init__(self):
        """Initialize application settings."""
        # UI settings
        self.appearance_mode = "System"  # System mode (light/dark)
        self.color_theme = "blue"  # Blue color theme
        self.window_title = "Whisper Transcription"
        self.window_size = "800x600"
        self.min_window_size = (800, 600)
        
        # Model settings
        self.default_model_size = "small"
        self.available_models = ["tiny", "base", "small", "medium", "large"]
        
        # Default language
        self.default_language = "de"
        
        # File types for dialog
        self.file_types = (
            ("OGG Files", "*.ogg"),
            ("WAV Files", "*.wav"),
            ("MP3 Files", "*.mp3"),
            ("All Files", "*.*")
        )
        
        # Apply custom tkinter settings
        self.apply_ctk_settings()
    
    def apply_ctk_settings(self):
        """Apply CustomTkinter global settings."""
        ctk.set_appearance_mode(self.appearance_mode)
        ctk.set_default_color_theme(self.color_theme)
    
    def get_model_factors(self):
        """Get processing time factors for different model sizes."""
        return {
            "tiny": 0.5, 
            "base": 1.0, 
            "small": 2.0, 
            "medium": 4.0, 
            "large": 8.0
        }
