import unittest
from data.colour import Colour


class ColourTest(unittest.TestCase):

    def test_default_colour(self):
        colour_build = Colour.default()
        colour_hand = Colour(red=0, green=0, blue=0, alpha=0)
        self.assertEqual(colour_build, colour_hand, "expect default colour to be correct")

    def test_colour_from_dict(self):
        colour_dict = {"red": 0.2, "blue": 0.4, "green": 1, "alpha": 0}
        colour_build = Colour.from_dict(colour_dict)
        colour_hand = Colour(red=0.2, green=1, blue=0.4, alpha=0)
        self.assertEqual(colour_build, colour_hand, "expect dict colour to be correct")

    def test_malformed_colour(self):
        colour_dict = {"red": 2}
        with self.assertRaises(ValueError):
            Colour.from_dict(colour_dict)

        wrong_type_dict = {"red": "1"}
        with self.assertRaises(TypeError):
            Colour.from_dict(wrong_type_dict)


if __name__ == '__main__':
    unittest.main()
