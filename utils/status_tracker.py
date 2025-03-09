"""
Status and progress tracking for the Whisper application.
"""
import time
import threading

class StatusTracker:
    """Track status, progress, and timing for the application."""
    
    def __init__(self, status_label=None, progress_bar=None, percent_label=None, time_label=None):
        """Initialize the status tracker with UI components."""
        self.status_label = status_label
        self.progress_bar = progress_bar
        self.percent_label = percent_label
        self.time_label = time_label
        
        self.start_time = 0
        self.estimated_total_time = 0
        self.processing = False
        self.progress_update_thread = None
    
    def set_ui_components(self, status_label, progress_bar, percent_label, time_label):
        """Set the UI components for status updates."""
        self.status_label = status_label
        self.progress_bar = progress_bar
        self.percent_label = percent_label
        self.time_label = time_label
    
    def update_status(self, message):
        """Update the status message."""
        if self.status_label:
            self.status_label.configure(text=message)
    
    def update_progress(self, value, time_info=""):
        """Update progress bar with percentage and time information."""
        if self.progress_bar:
            self.progress_bar.set(value)
        
        if self.percent_label:
            percent = int(value * 100)
            self.percent_label.configure(text=f"{percent}%")
        
        if self.time_label:
            self.time_label.configure(text=time_info)
    
    def start_timer(self):
        """Start the processing timer."""
        self.start_time = time.time()
        self.processing = True
        return self.start_time
    
    def stop_timer(self):
        """Stop the processing timer and return elapsed time."""
        self.processing = False
        if self.progress_update_thread and self.progress_update_thread.is_alive():
            # Let the thread finish naturally
            self.progress_update_thread.join(timeout=0.5)
        
        elapsed_time = time.time() - self.start_time
        return elapsed_time
    
    def start_progress_updates(self, start_progress, end_progress, estimated_duration, text_provider):
        """Start a thread to update progress periodically.
        
        Args:
            start_progress: Starting progress value (0.0-1.0)
            end_progress: Ending progress value (0.0-1.0)
            estimated_duration: Estimated duration for the task in seconds
            text_provider: Function that returns text based on remaining time
        """
        self.estimated_total_time = estimated_duration
        
        def update_progress_timer():
            """Update the progress regularly during transcription."""
            start_update_time = time.time()
            
            # Update every 0.1 seconds
            update_interval = 0.1
            last_progress = start_progress
            
            while self.processing and last_progress < end_progress:
                elapsed = time.time() - start_update_time
                # Calculate progress based on elapsed time
                if estimated_duration > 0:
                    progress_fraction = elapsed / estimated_duration
                    current_progress = start_progress + progress_fraction * (end_progress - start_progress)
                    # Limit progress to end_progress
                    current_progress = min(current_progress, end_progress)
                else:
                    current_progress = min(last_progress + 0.01, end_progress)
                
                # Calculate remaining time
                if progress_fraction > 0 and progress_fraction < 1:
                    remaining_time = (estimated_duration - elapsed)
                    self.update_progress(current_progress, text_provider(remaining_time))
                
                last_progress = current_progress
                time.sleep(update_interval)
        
        self.progress_update_thread = threading.Thread(
            target=update_progress_timer,
            daemon=True
        )
        self.progress_update_thread.start()
        
        return self.progress_update_thread
