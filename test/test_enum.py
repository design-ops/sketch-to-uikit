import unittest
from transformer_enums import filter_known_variants


class ProcessEnumsTest(unittest.TestCase):

    def test_variant_remove_defaults(self):
        variants = {"normal", "selected", "highlighted"}
        processed = filter_known_variants(variants)
        self.assertListEqual(processed, [])

    def test_return_not_defaults(self):
        variants = {"error", "normal", "selected", "highlighted"}
        processed = filter_known_variants(variants)
        self.assertListEqual(processed, ["error"])

    def test_handle_no_defaults(self):
        variants = {"new_value"}
        processed = filter_known_variants(variants)
        self.assertListEqual(processed, ["new_value"])
