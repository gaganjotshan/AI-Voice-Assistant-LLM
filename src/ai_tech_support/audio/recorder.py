import pyaudio
import wave
import numpy as np
from ..utils.logger import get_logger
from ..utils.exception import exception_handler, CustomException

logger = get_logger(__name__)

class AudioRecorder:
    @exception_handler
    def __init__(self, chunk=1024, format=pyaudio.paInt16, channels=1, rate=16000):
        self.chunk = chunk
        self.format = format
        self.channels = channels
        self.rate = rate
        self.p = pyaudio.PyAudio()
        self.stream = None
        logger.info("AudioRecorder initialized")

    @exception_handler
    def start_stream(self):
        self.stream = self.p.open(format=self.format,
                                  channels=self.channels,
                                  rate=self.rate,
                                  input=True,
                                  frames_per_buffer=self.chunk)
        logger.info("Audio stream started")

    @exception_handler
    def record_audio_chunk(self, duration=5):
        if not self.stream:
            self.start_stream()

        logger.info(f"Recording audio chunk of {duration} seconds")
        frames = []
        for _ in range(0, int(self.rate / self.chunk * duration)):
            data = self.stream.read(self.chunk)
            frames.append(data)

        return b''.join(frames)

    @exception_handler
    def save_audio_chunk(self, frames, filename="temp_audio_chunk.wav"):
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.format))
            wf.setframerate(self.rate)
            wf.writeframes(frames)
        logger.info(f"Audio chunk saved to {filename}")
        return filename

    @staticmethod
    def is_silence(data, threshold=500):
        audio_data = np.frombuffer(data, dtype=np.int16)
        energy = np.sum(audio_data.astype(float) ** 2) / len(audio_data)
        return energy < threshold

    def close(self):
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
        logger.info("AudioRecorder closed")