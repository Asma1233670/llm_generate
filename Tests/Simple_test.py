import unittest
import sys,os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ll_model.LL_model import LL_model

class TestLlama3Model(unittest.TestCase):
    def test_generate_response(self):
        response = LL_model.generate(prompt='What is data science? Respond in 2 sentences.')
        print(response)

if __name__ == '__main__':
    unittest.main()
