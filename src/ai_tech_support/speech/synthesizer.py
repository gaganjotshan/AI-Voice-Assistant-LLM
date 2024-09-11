# src/ai_tech_support/speech/synthesizer.py

import os
import time
import pygame
from gtts import gTTS
from ..utils.logger import get_logger
from ..utils.exception import exception_handler, CustomException

logger = get_logger(__name__)

@exception_handler
def play_text_to_speech(text, language='en', slow=False):
    logger.info(f"Converting text to speech: {text[:50]}...")
    tts = gTTS(text=text, lang=language, slow=slow)
    temp_audio_file = "temp_audio.mp3"
    tts.save(temp_audio_file)

    pygame.mixer.init()
    pygame.mixer.music.load(temp_audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    time.sleep(1)
    os.remove(temp_audio_file)
    logger.info("Text-to-speech playback completed")