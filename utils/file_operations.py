"""
File operations for the Whisper Transcription App.
"""
import os
from customtkinter import filedialog

class FileOperations:
    """Handles file operations for the application."""
    
    def __init__(self, filetypes=None):
        """Initialize file operations with optional file types."""
        self.filetypes = filetypes or (
            ("Audio Files", "*.mp3;*.wav;*.ogg"),
            ("All Files", "*.*")
        )
    
    def browse_for_audio(self, title="Select Audio File"):
        """Show file open dialog to select an audio file.
        
        Args:
            title: Dialog title
            
        Returns:
            str: Selected file path or empty string if canceled
        """
        filename = filedialog.askopenfilename(
            title=title,
            filetypes=self.filetypes
        )
        
        return filename if filename else ""
    
    def save_transcript(self, transcript, default_extension=".txt"):
        """Save transcript to a text file.
        
        Args:
            transcript: Text content to save
            default_extension: Default file extension
            
        Returns:
            tuple: (success, filename or error message)
        """
        if not transcript:
            return False, "No transcript to save"
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=default_extension,
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if not file_path:
            return False, "Operation canceled"
        
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(transcript)
            return True, os.path.basename(file_path)
        except Exception as e:
            return False, str(e)
