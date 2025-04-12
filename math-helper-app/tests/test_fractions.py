import unittest
from src.modules.fractions import add_fractions, subtract_fractions, multiply_fractions, divide_fractions

class TestFractions(unittest.TestCase):

    def test_add_fractions(self):
        self.assertEqual(add_fractions((1, 2), (1, 3)), (5, 6))
        self.assertEqual(add_fractions((1, 4), (1, 4)), (1, 2))

    def test_subtract_fractions(self):
        self.assertEqual(subtract_fractions((1, 2), (1, 3)), (1, 6))
        self.assertEqual(subtract_fractions((1, 2), (1, 2)), (0, 1))

    def test_multiply_fractions(self):
        self.assertEqual(multiply_fractions((1, 2), (1, 3)), (1, 6))
        self.assertEqual(multiply_fractions((2, 3), (3, 4)), (1, 2))

    def test_divide_fractions(self):
        self.assertEqual(divide_fractions((1, 2), (1, 3)), (3, 2))
        self.assertEqual(divide_fractions((1, 2), (1, 2)), (1, 1))

if __name__ == '__main__':
    unittest.main()