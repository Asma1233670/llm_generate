import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ll_model.LL_model import LL_model

class TestLlama3Model_(unittest.TestCase):
    def test_chat(self):
        response = LL_model.chat(prompt="What is the meaning of life?",system_message="You are a wise sage!",output_file="chat.txt")
        print(response)

if __name__ == '__main__':
    unittest.main()