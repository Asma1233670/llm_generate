import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ll_model.LL_model import LL_model

class TestLlama3Model2(unittest.TestCase):
    def test_generate_response(self):
        response = LL_model.generate(prompt='Artificial intelligence', system_message="Given a complex topic, explain it to a 5 year old,"
                                        "using descriptive imagery and interesting and fun stories.")
        print(response)

if __name__ == '__main__':
    unittest.main()
