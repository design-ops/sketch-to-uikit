import unittest
from data.styles import BaseStyle


class TransformerTest(unittest.TestCase):

    def test_no_variant(self):
        thing = BaseStyle.create_from_name("section/element/atom")
        self.assertEqual(None, thing.variant, "expect no variant")

    def test_variant(self):
        thing = BaseStyle.create_from_name("section/element[a_state]/atom")
        self.assertEqual("a_state", thing.variant, "expect a variant")
        self.assertEqual("element", thing.element, "expect element to have state removed")


if __name__ == '__main__':
    unittest.main()
