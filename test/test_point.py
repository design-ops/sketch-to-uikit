import unittest
from data.point import Point


class PointTest(unittest.TestCase):

    def test_point_from_integers(self):
        incoming = "{10, 10}"
        colour_build = Point.from_string(incoming)
        colour_hand = Point(x=10.0, y=10.0)
        self.assertEqual(colour_build, colour_hand, "expect integer dictonary to work")

    def test_point_from_floats(self):
        incoming = "{10.0, 10.0}"
        colour_build = Point.from_string(incoming)
        colour_hand = Point(x=10.0, y=10.0)
        self.assertEqual(colour_build, colour_hand, "expect integer dictonary to work")

if __name__ == '__main__':
    unittest.main()
