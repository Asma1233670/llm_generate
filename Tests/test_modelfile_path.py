import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ll_model.LL_model import LL_model

class TestLlama3Model4(unittest.TestCase):
    def test_create_path(self):
        LL_model.create(model_name="helpful",modelfilepath="Tests/modelfile.txt")
    def test_generate_response(self):
        response = LL_model.generate(model="helpful",prompt='Can you explain to me quantum physics?')
        print(response)

if __name__ == '__main__':
    unittest.main()