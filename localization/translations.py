"""
Translations and localization for the Whisper Transcription Application.
"""

class TranslationManager:
    def __init__(self, default_language="de"):
        """Initialize translation manager with a default language."""
        self.current_language = default_language
        self.translations = self._get_translations()
        
    def _get_translations(self):
        """Define all application translations."""
        return {
            "en": {  # English
                "window_title": "Whisper Transcription",
                "title_label": "Whisper Transcription",
                "file_label": "Audio File:",
                "browse_button": "Browse",
                "model_label": "Model Size:",
                "model_info": "Note: The 'large' model requires more memory (min. 8GB)",
                "device_label": "Hardware: {device}",
                "transcribe_button": "Transcribe Audio",
                "status_ready": "Ready",
                "status_loading": "Loading model...",
                "status_large_warning": "Loading large model on CPU - may be slow",
                "status_model_loaded": "Model '{model}' loaded on {device}",
                "status_loaded_in": "Loaded in {time:.1f}s",
                "status_processing": "Processing audio...",
                "status_loading_audio": "Loading audio...",
                "status_transcribing": "Transcribing...",
                "status_completed": "Transcription completed! ({time:.1f}s)",
                "status_select_file": "Please select an audio file",
                "status_wait_model": "Model is still loading, please wait",
                "status_remaining": "Remaining: ~{time:.1f}s",
                "transcript_label": "Transcription:",
                "copy_button": "Copy",
                "save_button": "Save",
                "clear_button": "Clear",
                "status_copied": "Copied to clipboard",
                "status_no_transcript": "No transcription to save",
                "status_saved": "Saved: {filename}",
                "status_cleared": "Transcription cleared",
                "language_label": "Interface Language:",
                "error_audio": "Error processing audio: {error}",
                "error_saving": "Error saving: {error}",
                "error_generic": "Error: {error}"
            },
            "de": {  # German
                "window_title": "Whisper Transkription",
                "title_label": "Whisper Transkription",
                "file_label": "Audio-Datei:",
                "browse_button": "Durchsuchen",
                "model_label": "Modellgröße:",
                "model_info": "Hinweis: Das 'large' Modell benötigt mehr Arbeitsspeicher (mind. 8GB)",
                "device_label": "Hardware: {device}",
                "transcribe_button": "Audio transkribieren",
                "status_ready": "Bereit",
                "status_loading": "Modell wird geladen...",
                "status_large_warning": "Lade großes Modell auf CPU - kann langsam sein",
                "status_model_loaded": "Modell '{model}' geladen auf {device}",
                "status_loaded_in": "Geladen in {time:.1f}s",
                "status_processing": "Audio wird verarbeitet...",
                "status_loading_audio": "Audio wird geladen...",
                "status_transcribing": "Transkribieren...",
                "status_completed": "Transkription abgeschlossen! ({time:.1f}s)",
                "status_select_file": "Bitte wähle eine Audio-Datei aus",
                "status_wait_model": "Modell wird noch geladen, bitte warten",
                "status_remaining": "Verbleibend: ~{time:.1f}s",
                "transcript_label": "Transkription:",
                "copy_button": "Kopieren",
                "save_button": "Speichern",
                "clear_button": "Löschen",
                "status_copied": "In Zwischenablage kopiert",
                "status_no_transcript": "Keine Transkription zum Speichern",
                "status_saved": "Gespeichert: {filename}",
                "status_cleared": "Transkription gelöscht",
                "language_label": "Benutzeroberfläche:",
                "error_audio": "Fehler bei der Audioverarbeitung: {error}",
                "error_saving": "Fehler beim Speichern: {error}",
                "error_generic": "Fehler: {error}"
            },
            "fr": {  # French
                "window_title": "Whisper Transcription",
                "title_label": "Transcription Whisper",
                "file_label": "Fichier audio:",
                "browse_button": "Parcourir",
                "model_label": "Taille du modèle:",
                "model_info": "Remarque: Le modèle 'large' nécessite plus de mémoire (min. 8 Go)",
                "device_label": "Matériel: {device}",
                "transcribe_button": "Transcrire l'audio",
                "status_ready": "Prêt",
                "status_loading": "Chargement du modèle...",
                "status_large_warning": "Chargement du grand modèle sur CPU - peut être lent",
                "status_model_loaded": "Modèle '{model}' chargé sur {device}",
                "status_loaded_in": "Chargé en {time:.1f}s",
                "status_processing": "Traitement de l'audio...",
                "status_loading_audio": "Chargement de l'audio...",
                "status_transcribing": "Transcription...",
                "status_completed": "Transcription terminée! ({time:.1f}s)",
                "status_select_file": "Veuillez sélectionner un fichier audio",
                "status_wait_model": "Le modèle se charge encore, veuillez patienter",
                "status_remaining": "Restant: ~{time:.1f}s",
                "transcript_label": "Transcription:",
                "copy_button": "Copier",
                "save_button": "Enregistrer",
                "clear_button": "Effacer",
                "status_copied": "Copié dans le presse-papiers",
                "status_no_transcript": "Pas de transcription à enregistrer",
                "status_saved": "Enregistré: {filename}",
                "status_cleared": "Transcription effacée",
                "language_label": "Langue d'interface:",
                "error_audio": "Erreur lors du traitement audio: {error}",
                "error_saving": "Erreur lors de l'enregistrement: {error}",
                "error_generic": "Erreur: {error}"
            },
            "es": {  # Spanish
                "window_title": "Transcripción Whisper",
                "title_label": "Transcripción Whisper",
                "file_label": "Archivo de audio:",
                "browse_button": "Examinar",
                "model_label": "Tamaño del modelo:",
                "model_info": "Nota: El modelo 'large' requiere más memoria (mín. 8GB)",
                "device_label": "Hardware: {device}",
                "transcribe_button": "Transcribir audio",
                "status_ready": "Listo",
                "status_loading": "Cargando modelo...",
                "status_large_warning": "Cargando modelo grande en CPU - puede ser lento",
                "status_model_loaded": "Modelo '{model}' cargado en {device}",
                "status_loaded_in": "Cargado en {time:.1f}s",
                "status_processing": "Procesando audio...",
                "status_loading_audio": "Cargando audio...",
                "status_transcribing": "Transcribiendo...",
                "status_completed": "¡Transcripción completada! ({time:.1f}s)",
                "status_select_file": "Por favor seleccione un archivo de audio",
                "status_wait_model": "El modelo aún se está cargando, por favor espere",
                "status_remaining": "Restante: ~{time:.1f}s",
                "transcript_label": "Transcripción:",
                "copy_button": "Copiar",
                "save_button": "Guardar",
                "clear_button": "Borrar",
                "status_copied": "Copiado al portapapeles",
                "status_no_transcript": "No hay transcripción para guardar",
                "status_saved": "Guardado: {filename}",
                "status_cleared": "Transcripción borrada",
                "language_label": "Idioma de interfaz:",
                "error_audio": "Error al procesar audio: {error}",
                "error_saving": "Error al guardar: {error}",
                "error_generic": "Error: {error}"
            }
        }
    
    def set_language(self, language_code):
        """Set the current language."""
        if language_code in self.translations:
            self.current_language = language_code
            return True
        return False
    
    def get_text(self, key, **kwargs):
        """Get text in current language with formatting."""
        text = self.translations.get(self.current_language, {}).get(key, key)
        
        # Apply any format variables if provided
        if kwargs:
            return text.format(**kwargs)
        return text
    
    def get_language_options(self):
        """Get available language options for UI."""
        return {
            "en": "English",
            "de": "Deutsch",
            "fr": "Français",
            "es": "Español"
        }
    
    def get_language_code(self, language_name):
        """Convert language name to code."""
        lang_map = {
            "English": "en",
            "Deutsch": "de",
            "Français": "fr",
            "Español": "es"
        }
        return lang_map.get(language_name, "en")
