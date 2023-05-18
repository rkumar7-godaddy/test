#import unit test to create unit tests
import unittest

# import the functions in functions.py
from functions import add, subtract

class TestBasicMethods(unittest.TestCase):

    # testing the add method
    def test_add(self):
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(3, 0), 3)
        self.assertEqual(add(23, 77), 100)
    
    # testing the subtract method
    def test_subtract(self):
        self.assertEqual(add(10, 2), 8)
        self.assertEqual(add(0, 4), -4)
        self.assertEqual(add(31, 31), 0)
