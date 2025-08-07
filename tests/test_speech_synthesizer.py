import unittest
from src.ai_tech_support.speech.synthesizer import play_text_to_speech

class TestSynthesizer(unittest.TestCase):
    def test_play_text_to_speech(self):
        text = "This is a test of the text-to-speech functionality."
        print(f"Playing: '{text}'")
        play_text_to_speech(text)
        user_input = input("Did you hear the audio clearly? (y/n): ")
        self.assertEqual(user_input.lower(), 'y')

if __name__ == '__main__':
    unittest.main()