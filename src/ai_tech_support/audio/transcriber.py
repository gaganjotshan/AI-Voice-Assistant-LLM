# src/ai_tech_support/audio/transcriber.py

from faster_whisper import WhisperModel
from ..utils.logger import get_logger
from ..utils.exception import exception_handler, CustomException

logger = get_logger(__name__)

class Transcriber:
    @exception_handler
    def __init__(self, model_size="medium", device="cpu", compute_type="int8"):
        self.model = WhisperModel(model_size, device=device, compute_type=compute_type)
        logger.info(f"Transcriber initialized with model size: {model_size}")

    @exception_handler
    def transcribe(self, audio_file):
        logger.info(f"Transcribing audio file: {audio_file}")
        segments, _ = self.model.transcribe(audio_file, beam_size=5)
        transcription = ' '.join(segment.text for segment in segments)
        logger.info(f"Transcription completed: {transcription[:50]}...")
        return transcription