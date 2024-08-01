import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ll_model.LL_model import LL_model

class TestLlama3Model3(unittest.TestCase):
    def test_create_model(self):
        LL_model.create(model_name="mario",modelfile="FROM llama3 \nSYSTEM You are mario from Super" 
                                                                  "Mario Bros.")

    def test_generate_response(self):
        response = LL_model.generate(prompt='Hi Mario! What are you doing??')
        print(response)

if __name__ == '__main__':
    unittest.main()