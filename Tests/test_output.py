import unittest
import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ll_model.LL_model import LL_model

class TestLlama3Model(unittest.TestCase):
    def test_generate_response_json(self):
        LL_model.generate(prompt='What is Data Science? Respond using JSON.',output_file='Tests/output.json')
    
    def test_generate_response_pdf(self):
        LL_model.generate(prompt='What is Computer Vision? ', output_file='Tests/output.pdf')
        
    def test_generate_response_txt(self):
        LL_model.generate(prompt= 'What is transfert learning?',output_file='Tests/output.txt')

if __name__ == '__main__':
    unittest.main()