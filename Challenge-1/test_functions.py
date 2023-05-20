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
        self.assertEqual(add(35, -4), 31)
    
    # testing the subtract method
    def test_subtract(self):
        self.assertEqual(subtract(10, 2), 8)
        self.assertEqual(subtract(0, 4), -4)
        self.assertEqual(subtract(31, 31), 0)
        self.assertEqual(subtract(21, -3), 24)
