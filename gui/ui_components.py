"""
UI components for the Whisper Transcription App.
"""
import customtkinter as ctk

class UIFactory:
    """Factory for creating UI components."""
    
    @staticmethod
    def create_main_title(parent, text, font_size=20):
        """Create main title label."""
        title = ctk.CTkLabel(
            parent, 
            text=text, 
            font=ctk.CTkFont(size=font_size, weight="bold")
        )
        return title
    
    @staticmethod
    def create_main_frame(parent):
        """Create main content frame."""
        frame = ctk.CTkFrame(parent)
        frame.grid_columnconfigure(0, weight=1)
        return frame
    
    @staticmethod
    def create_language_selector(parent, label_text, options, command):
        """Create language selection frame and components."""
        frame = ctk.CTkFrame(parent)
        
        label = ctk.CTkLabel(frame, text=label_text)
        label.grid(row=0, column=0, padx=10, pady=10)
        
        menu = ctk.CTkOptionMenu(
            frame,
            values=list(options.values()),
            command=command
        )
        menu.grid(row=0, column=1, padx=10, pady=10)
        
        return frame, label, menu
    
    @staticmethod
    def create_file_selector(parent, label_text, browse_text, command):
        """Create file selection frame and components."""
        frame = ctk.CTkFrame(parent)
        frame.grid_columnconfigure(1, weight=1)
        
        label = ctk.CTkLabel(frame, text=label_text)
        label.grid(row=0, column=0, padx=10, pady=10)
        
        entry = ctk.CTkEntry(frame)
        entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        button = ctk.CTkButton(
            frame, 
            text=browse_text, 
            command=command
        )
        button.grid(row=0, column=2, padx=10, pady=10)
        
        return frame, label, entry, button
    
    @staticmethod
    def create_model_selector(parent, label_text, model_options, info_text, device_text, variable, command):
        """Create model selection frame and components."""
        frame = ctk.CTkFrame(parent)
        
        label = ctk.CTkLabel(frame, text=label_text)
        label.grid(row=0, column=0, padx=10, pady=10)
        
        menu = ctk.CTkOptionMenu(
            frame,
            values=model_options,
            variable=variable,
            command=command
        )
        menu.grid(row=0, column=1, padx=10, pady=10)
        
        info_label = ctk.CTkLabel(
            frame, 
            text=info_text,
            font=ctk.CTkFont(size=10),
            text_color="gray60"
        )
        info_label.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="w")
        
        device_label = ctk.CTkLabel(
            frame, 
            text=device_text, 
            font=ctk.CTkFont(size=10),
            text_color="gray60"
        )
        device_label.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="w")
        
        return frame, label, menu, info_label, device_label
    
    @staticmethod
    def create_action_button(parent, text, command, height=40, font_size=14):
        """Create primary action button."""
        button = ctk.CTkButton(
            parent,
            text=text,
            font=ctk.CTkFont(size=font_size, weight="bold"),
            height=height,
            command=command
        )
        return button
    
    @staticmethod
    def create_status_area(parent):
        """Create status and progress tracking area."""
        frame = ctk.CTkFrame(parent)
        frame.grid_columnconfigure(0, weight=1)
        
        # Progress row with bar and percentage
        progress_row = ctk.CTkFrame(frame, fg_color="transparent")
        progress_row.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        progress_row.grid_columnconfigure(0, weight=1)
        
        progress = ctk.CTkProgressBar(progress_row)
        progress.grid(row=0, column=0, padx=(0, 10), pady=5, sticky="ew")
        progress.set(0)
        
        percent_label = ctk.CTkLabel(progress_row, text="0%", width=40)
        percent_label.grid(row=0, column=1, padx=(0, 5), pady=5)
        
        # Info row with status and time
        info_row = ctk.CTkFrame(frame, fg_color="transparent")
        info_row.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        info_row.grid_columnconfigure(0, weight=1)
        
        status_label = ctk.CTkLabel(info_row, text="Ready", anchor="w")
        status_label.grid(row=0, column=0, padx=0, pady=5, sticky="w")
        
        time_label = ctk.CTkLabel(info_row, text="", anchor="e")
        time_label.grid(row=0, column=1, padx=0, pady=5, sticky="e")
        
        return frame, progress, percent_label, status_label, time_label
    
    @staticmethod
    def create_transcript_area(parent, label_text):
        """Create transcript display area."""
        frame = ctk.CTkFrame(parent)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)
        
        label = ctk.CTkLabel(
            frame, 
            text=label_text,
            anchor="w"
        )
        label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        
        text_box = ctk.CTkTextbox(frame, wrap="word")
        text_box.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        
        return frame, label, text_box
    
    @staticmethod
    def create_button_bar(parent, button_configs):
        """Create button bar with multiple buttons.
        
        Args:
            parent: Parent widget
            button_configs: List of (text, command) tuples
        """
        frame = ctk.CTkFrame(parent)
        
        buttons = []
        for i, (text, command) in enumerate(button_configs):
            button = ctk.CTkButton(
                frame,
                text=text,
                command=command
            )
            button.grid(row=0, column=i, padx=10, pady=10)
            buttons.append(button)
        
        return frame, buttons
