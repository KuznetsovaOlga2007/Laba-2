import math
import unittest


def area(r): # Function that returns area of circle
    return math.pi * r * r


def perimeter(r): # function that returns perimeter of circle
    return 2 * math.pi * r # gets 2 varibles and returns one


class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_int_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_float_area(self):
        res = area(8.7)
        self.assertAlmostEqual(res, 86.2251306, delta=0.1)

    def test_zero_perimetr(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_int_perimetr(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_float_perimetr(self):
        res = perimeter(5.239)
        self.assertAlmostEqual(res, 32.916637, delta=0.1)
