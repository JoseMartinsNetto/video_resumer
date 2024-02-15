from typing import Callable, Optional
import whisper

class WhisperAudioToTextParser:
    def __init__(self, audioPath: str, modelName: str = 'medium', language: str = 'pt', autoDetectLanguage: bool = False) -> None:
        self.audioPath = audioPath
        self.modelName = modelName
        self.language = language
        self.autoDetectLanguage = autoDetectLanguage

    def parse(self, on_parsing_progress: Optional[Callable[[list, int, int, float], bool]] = None) -> dict:
        model = whisper.load_model(self.modelName)
        result = model.transcribe(self.audioPath, progress=on_parsing_progress)
        
        return result