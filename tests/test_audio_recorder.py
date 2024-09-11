import unittest
import os
from src.ai_tech_support.audio.recorder import AudioRecorder
import numpy as np

class TestAudioRecorder(unittest.TestCase):
    def setUp(self):
        self.recorder = AudioRecorder()

    def tearDown(self):
        self.recorder.close()

    def test_record_audio_chunk(self):
        print("Please speak for 5 seconds...")
        audio_data = self.recorder.record_audio_chunk(duration=5)
        self.assertIsNotNone(audio_data)
        self.assertGreater(len(audio_data), 0)

    def test_save_audio_chunk(self):
        audio_data = self.recorder.record_audio_chunk(duration=2)
        filename = self.recorder.save_audio_chunk(audio_data, "test_audio.wav")
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

    def test_is_silence(self):
        silent_data = np.zeros(1024, dtype=np.int16).tobytes()  # Create a buffer of zeros
        self.assertTrue(AudioRecorder.is_silence(silent_data))

        non_silent_data = (np.random.rand(1024) * 32767).astype(np.int16).tobytes()  # Create a buffer of max values
        self.assertFalse(AudioRecorder.is_silence(non_silent_data))

if __name__ == '__main__':
    unittest.main()