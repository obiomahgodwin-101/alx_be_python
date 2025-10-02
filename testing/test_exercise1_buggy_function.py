# test_exercise1_buggy_function.py
import unittest
from exercise1_buggy_function import square_number

class TestSquareNumber(unittest.TestCase):
    
    def test_square_of_positive(self):
        self.assertEqual(square_number(3), 9)  # Expected: 9
    
    def test_square_of_zero(self):
        self.assertEqual(square_number(0), 0)  # Expected: 0

    def test_square_of_negative(self):
        self.assertEqual(square_number(-2), 4)  # Expected: 4

if __name__ == "__main__":
    unittest.main()
