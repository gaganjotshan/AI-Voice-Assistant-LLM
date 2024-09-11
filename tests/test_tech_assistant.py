import unittest
from src.ai_tech_support.llm_assistant.tech_assistant import TechSupportAssistant

class TestTechSupportAssistant(unittest.TestCase):
    def setUp(self):
        self.assistant = TechSupportAssistant()

    def test_interact_with_llm(self):
        query = "How do I reset my router?"
        response = self.assistant.interact_with_llm(query)
        self.assertIsNotNone(response)
        self.assertGreater(len(response), 0)
        print(f"Query: {query}")
        print(f"Response: {response}")

if __name__ == '__main__':
    unittest.main()