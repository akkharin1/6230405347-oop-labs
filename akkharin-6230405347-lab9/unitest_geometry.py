import unittest
import maths
from geometry import shape
from geometry import area

class TestMath(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(maths.sum(1, 2), 3)
        self.assertEqual(maths.sum(1.1, 2.3), 3.4)

    def test_subtract(self):
        self.assertEqual(maths.subtract(10, 2), 8)
        self.assertEqual(maths.subtract(-3, 2), -5)

if __name__ == '__main__':
    unittest.main()