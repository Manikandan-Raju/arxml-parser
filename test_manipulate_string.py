import unittest
import re
from manipulate_string import Manipulate_string

class TestFishTank(unittest.TestCase):
    def setUp(self):
        self.manipulate_string = Manipulate_string()

    def test_correct(self):
        string = "He is a Good Boy"
        output = self.manipulate_string.output(string)
        output = re.sub(r'[^a-zA-Z]','',output)
        for i,s in enumerate(output):
            if i %2 == 0: 
                self.assertTrue(s.isupper())
            else:
                self.assertTrue(s.islower())

    def test_incorrect(self):
        string = "He is a Good Boy"
        output = self.manipulate_string.output(string)
        output = re.sub(r'[^a-zA-Z]','',output)
        output += 's'
        for i,s in enumerate(output):
            if i == len(output):
                if i %2 != 0: 
                    self.assertFalse(s.isupper())