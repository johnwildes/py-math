import unittest
from src.modules.geometry import calculate_area, calculate_perimeter

class TestGeometry(unittest.TestCase):

    def test_calculate_area_square(self):
        self.assertEqual(calculate_area('square', 4), 16)

    def test_calculate_area_rectangle(self):
        self.assertEqual(calculate_area('rectangle', 4, 5), 20)

    def test_calculate_area_circle(self):
        self.assertAlmostEqual(calculate_area('circle', 3), 28.27, places=2)

    def test_calculate_perimeter_square(self):
        self.assertEqual(calculate_perimeter('square', 4), 16)

    def test_calculate_perimeter_rectangle(self):
        self.assertEqual(calculate_perimeter('rectangle', 4, 5), 18)

    def test_calculate_perimeter_circle(self):
        self.assertAlmostEqual(calculate_perimeter('circle', 3), 18.85, places=2)

if __name__ == '__main__':
    unittest.main()