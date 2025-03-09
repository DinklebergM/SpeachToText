"""
Main application window for the Whisper Transcription App.
"""
import time
import customtkinter as ctk
from config.settings import AppSettings
from localization.translations import TranslationManager
from models.transcription_engine import TranscriptionEngine
from models.audio_processor import AudioProcessor
from utils.file_operations import FileOperations
from utils.status_tracker import StatusTracker
from gui.ui_components import UIFactory

class WhisperApp(ctk.CTk):
    """Main application window."""
    
    def __init__(self):
        """Initialize the application."""
        super().__init__()
        
        # Initialize components
        self.settings = AppSettings()
        self.translations = TranslationManager(self.settings.default_language)
        self.transcription_engine = TranscriptionEngine()
        self.audio_processor = AudioProcessor()
        self.file_operations = FileOperations(self.settings.file_types)
        self.status_tracker = StatusTracker()
        
        # Application state
        self.file_path = ""
        self.model_size = ctk.StringVar(value=self.settings.default_model_size)
        self.transcription = ""
        
        # Setup window
        self.title(self.get_text("window_title"))
        self.geometry(self.settings.window_size)
        self.minsize(*self.settings.min_window_size)
        
        # Create UI
        self.create_ui()
        
        # Load model
        self.load_model_thread()
    
    def get_text(self, key, **kwargs):
        """Get text in current language with formatting."""
        return self.translations.get_text(key, **kwargs)
    
    def create_ui(self):
        """Create the application UI."""
        # Main layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Title
        self.title_label = UIFactory.create_main_title(
            self, 
            self.get_text("title_label")
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # Main frame
        self.main_frame = UIFactory.create_main_frame(self)
        self.main_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_rowconfigure(5, weight=1)
        
        # Language selection
        lang_options = self.translations.get_language_options()
        self.lang_frame, self.lang_label, self.lang_menu = UIFactory.create_language_selector(
            self.main_frame,
            self.get_text("language_label"),
            lang_options,
            self.change_language
        )
        self.lang_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.lang_menu.set(lang_options[self.translations.current_language])
        
        # File selection
        self.file_frame, self.file_label, self.file_entry, self.browse_button = UIFactory.create_file_selector(
            self.main_frame,
            self.get_text("file_label"),
            self.get_text("browse_button"),
            self.browse_file
        )
        self.file_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        # Model selection
        self.model_frame, self.model_label, self.model_menu, self.model_info_label, self.device_label = UIFactory.create_model_selector(
            self.main_frame,
            self.get_text("model_label"),
            self.settings.available_models,
            self.get_text("model_info"),
            self.get_text("device_label", device=self.transcription_engine.get_device_name()),
            self.model_size,
            self.change_model
        )
        self.model_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        # Transcribe button
        self.transcribe_button = UIFactory.create_action_button(
            self.main_frame,
            self.get_text("transcribe_button"),
            self.transcribe_audio
        )
        self.transcribe_button.grid(row=3, column=0, padx=10, pady=20, sticky="ew")
        
        # Status area
        self.status_frame, self.progress, self.percent_label, self.status_label, self.time_label = UIFactory.create_status_area(
            self.main_frame
        )
        self.status_frame.grid(row=4, column=0, padx=10, pady=5, sticky="ew")
        
        # Update status tracker with UI components
        self.status_tracker.set_ui_components(
            self.status_label,
            self.progress,
            self.percent_label,
            self.time_label
        )
        
        # Transcript area
        self.transcript_frame, self.transcript_label, self.transcript_text = UIFactory.create_transcript_area(
            self.main_frame,
            self.get_text("transcript_label")
        )
        self.transcript_frame.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")
        
        # Button bar
        button_configs = [
            (self.get_text("copy_button"), self.copy_to_clipboard),
            (self.get_text("save_button"), self.save_to_file),
            (self.get_text("clear_button"), self.clear_transcript)
        ]
        self.button_frame, self.action_buttons = UIFactory.create_button_bar(
            self,
            button_configs
        )
        self.button_frame.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
    
    def update_ui_language(self):
        """Update all UI text based on selected language."""
        # Update window title
        self.title(self.get_text("window_title"))
        
        # Update main title
        self.title_label.configure(text=self.get_text("title_label"))
        
        # Update language selector
        self.lang_label.configure(text=self.get_text("language_label"))
        
        # Update file selection frame
        self.file_label.configure(text=self.get_text("file_label"))
        self.browse_button.configure(text=self.get_text("browse_button"))
        
        # Update model selection frame
        self.model_label.configure(text=self.get_text("model_label"))
        self.model_info_label.configure(text=self.get_text("model_info"))
        
        # Format device label
        device_text = self.get_text("device_label", device=self.transcription_engine.get_device_name())
        self.device_label.configure(text=device_text)
        
        # Update transcribe button
        self.transcribe_button.configure(text=self.get_text("transcribe_button"))
        
        # Update transcript section
        self.transcript_label.configure(text=self.get_text("transcript_label"))
        
        # Update buttons
        self.action_buttons[0].configure(text=self.get_text("copy_button"))
        self.action_buttons[1].configure(text=self.get_text("save_button"))
        self.action_buttons[2].configure(text=self.get_text("clear_button"))
        
        # Update status if it's in a default state
        current_status = self.status_label.cget("text")
        if current_status in ["Bereit", "Ready", "Prêt", "Listo"]:
            self.status_tracker.update_status(self.get_text("status_ready"))
    
    def change_language(self, choice):
        """Change the UI language."""
        # Map dropdown selection to language code
        lang_code = self.translations.get_language_code(choice)
        
        # Set new language
        self.translations.set_language(lang_code)
        
        # Update UI with new language
        self.update_ui_language()
    
    def browse_file(self):
        """Open file dialog."""
        filename = self.file_operations.browse_for_audio(
            title=self.get_text("file_label")
        )
        
        if filename:
            self.file_path = filename
            self.file_entry.delete(0, ctk.END)
            self.file_entry.insert(0, filename)
    
    def load_model_thread(self):
        """Load Whisper model in a separate thread."""
        self.status_tracker.update_status(self.get_text("status_loading"))
        self.status_tracker.update_progress(0.2, self.get_text("status_loading"))
        self.toggle_ui_state(False)
        
        # Start timer for estimation
        start_time = self.status_tracker.start_timer()
        
        def on_model_loaded(success, error):
            """Callback when model loading completes."""
            if success:
                elapsed_time = time.time() - start_time
                
                self.status_tracker.update_status(
                    self.get_text("status_model_loaded", 
                                 model=self.model_size.get(), 
                                 device=self.transcription_engine.get_device_name())
                )
                self.status_tracker.update_progress(
                    1.0, self.get_text("status_loaded_in", time=elapsed_time)
                )
                
                # Reset after a delay
                self.after(2000, lambda: self.status_tracker.update_progress(0, ""))
                self.after(2000, lambda: self.status_tracker.update_status(self.get_text("status_ready")))
            else:
                self.status_tracker.update_status(
                    self.get_text("error_generic", error=error)
                )
            
            self.toggle_ui_state(True)
            self.status_tracker.stop_timer()
        
        # Start loading the model
        self.transcription_engine.load_model(
            self.model_size.get(),
            on_complete=on_model_loaded
        )
    
    def change_model(self, choice):
        """Change model size."""
        self.model_size.set(choice)
        
        # Show warning for large model
        if choice == "large":
            self.status_tracker.update_status(self.get_text("status_large_warning"))
            self.after(3000, self.load_model_thread)  # Delay to read warning
        else:
            self.load_model_thread()
    
    def transcribe_audio(self):
        """Transcribe audio."""
        if not self.file_path:
            self.status_tracker.update_status(self.get_text("status_select_file"))
            return
        
        if self.transcription_engine.is_loading or not self.transcription_engine.model:
            self.status_tracker.update_status(self.get_text("status_wait_model"))
            return
        
        if self.status_tracker.processing:
            return
        
        # Setup for processing
        self.toggle_ui_state(False)
        self.status_tracker.update_progress(0.1, self.get_text("status_processing"))
        self.status_tracker.update_status(self.get_text("status_processing"))
        
        # Start timer
        self.status_tracker.start_timer()
        
        def process_audio():
            try:
                # Load audio
                self.status_tracker.update_status(self.get_text("status_loading_audio"))
                audio = self.audio_processor.load_audio(self.file_path)
                
                # Update progress
                self.status_tracker.update_progress(0.3, self.get_text("status_loading_audio"))
                self.status_tracker.update_status(self.get_text("status_transcribing"))
                
                # Calculate estimated time
                audio_duration = self.audio_processor.get_audio_duration(audio)
                model_factors = self.settings.get_model_factors()
                transcription_time = self.transcription_engine.estimate_processing_time(
                    audio_duration, model_factors
                )
                
                # Start progress updates
                self.status_tracker.start_progress_updates(
                    0.3, 0.9, 
                    transcription_time,
                    lambda time: self.get_text("status_remaining", time=time)
                )
                
                # Transcribe
                def on_transcription_complete(success, transcription, error):
                    if success:
                        self.transcription = transcription
                        
                        # Calculate total time
                        total_time = self.status_tracker.stop_timer()
                        
                        # Update UI
                        self.update_transcript(self.transcription)
                        self.status_tracker.update_progress(
                            1.0, self.get_text("status_completed", time=total_time)
                        )
                        self.status_tracker.update_status(
                            self.get_text("status_completed", time=total_time)
                        )
                        
                        # Reset after a delay
                        self.after(5000, lambda: self.status_tracker.update_progress(0, ""))
                        self.after(5000, lambda: self.status_tracker.update_status(self.get_text("status_ready")))
                    else:
                        self.status_tracker.update_status(
                            self.get_text("error_audio", error=error)
                        )
                        self.status_tracker.stop_timer()
                    
                    self.toggle_ui_state(True)
                
                # Start transcription
                self.transcription_engine.transcribe(audio, on_transcription_complete)
                
            except Exception as e:
                error_message = str(e)
                self.status_tracker.update_status(
                    self.get_text("error_audio", error=error_message)
                )
                self.status_tracker.stop_timer()
                self.toggle_ui_state(True)
        
        # Start processing in a new thread
        import threading
        threading.Thread(target=process_audio, daemon=True).start()
    
    def update_transcript(self, text):
        """Update transcript text."""
        self.transcript_text.delete("0.0", ctk.END)
        self.transcript_text.insert("0.0", text)
    
    def toggle_ui_state(self, enabled):
        """Enable/disable UI elements."""
        state = "normal" if enabled else "disabled"
        self.browse_button.configure(state=state)
        self.model_menu.configure(state=state)
        self.transcribe_button.configure(state=state)
        self.action_buttons[0].configure(state=state)  # Copy
        self.action_buttons[1].configure(state=state)  # Save
        self.action_buttons[2].configure(state=state)  # Clear
        self.lang_menu.configure(state=state)
    
    def copy_to_clipboard(self):
        """Copy to clipboard."""
        self.clipboard_clear()
        self.clipboard_append(self.transcription)
        self.status_tracker.update_status(self.get_text("status_copied"))
        self.after(2000, lambda: self.status_tracker.update_status(self.get_text("status_ready")))
    
    def save_to_file(self):
        """Save as text file."""
        if not self.transcription:
            self.status_tracker.update_status(self.get_text("status_no_transcript"))
            return
        
        success, result = self.file_operations.save_transcript(self.transcription)
        
        if success:
            self.status_tracker.update_status(self.get_text("status_saved", filename=result))
        else:
            self.status_tracker.update_status(self.get_text("error_saving", error=result))
        
        self.after(2000, lambda: self.status_tracker.update_status(self.get_text("status_ready")))
    
    def clear_transcript(self):
        """Clear transcription."""
        self.transcript_text.delete("0.0", ctk.END)
        self.transcription = ""
        self.status_tracker.update_status(self.get_text("status_cleared"))
        self.after(2000, lambda: self.status_tracker.update_status(self.get_text("status_ready")))
