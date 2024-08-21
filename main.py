# main.py

import os
from src.ai_tech_support.audio.recorder import AudioRecorder
from src.ai_tech_support.audio.transcriber import Transcriber
from src.ai_tech_support.llm_model.tech_assistant import TechSupportAssistant
from src.ai_tech_support.speech.synthesizer import play_text_to_speech
from src.ai_tech_support.utils.logger import get_logger
from src.ai_tech_support.utils.exception import exception_handler, CustomException

logger = get_logger(__name__)

@exception_handler
def main():
    recorder = AudioRecorder()
    transcriber = Transcriber()
    assistant = TechSupportAssistant()

    logger.info("AI Tech Support Assistant is ready")
    print("AI Tech Support Assistant is ready. How can I assist you today?")

    try:
        while True:
            print("_")
            audio_data = recorder.record_audio_chunk()
            if not recorder.is_silence(audio_data):
                audio_file = recorder.save_audio_chunk(audio_data)
                transcription = transcriber.transcribe(audio_file)
                os.remove(audio_file)
                logger.info(f"User: {transcription}")
                print(f"User: {transcription}")

                response = assistant.interact_with_llm(transcription)
                logger.info(f"Assistant: {response}")
                print(f"Assistant: {response}")
                play_text_to_speech(response)

    except KeyboardInterrupt:
        logger.info("Stopping the application...")
        print("\nStopping...")
    finally:
        recorder.close()

if __name__ == "__main__":
    main()