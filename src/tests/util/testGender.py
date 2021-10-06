import sys
import os

project_dir = os.getcwd()
sys.path.append(project_dir)

import unittest
from src.main.util.gender import Gender

class TestGender(unittest.TestCase): 
    
    def testGender(self):
        self.assertTrue(Gender.male == 'Male')
        self.assertTrue(Gender.female == 'Female')
        self.assertTrue(Gender.female == Gender.getGender('Female'))
        self.assertTrue(Gender.male == Gender.getGender('Male'))
        self.assertTrue(Gender.getGender('anything else') is None)
    
        
if __name__ == '__main__':
    unittest.main()
