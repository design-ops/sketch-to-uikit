
import unittest
from process_layer_styles import process_json
from root import ROOT_DIR
import filecmp
from uuid import uuid4
from os import path
from shutil import rmtree


class ProcessLayerStylesTest(unittest.TestCase):

    def test_pure_layer_styles(self):
        # run the process
        json = path.join(ROOT_DIR, '../test-resources/layer_styles/layer_styles.json')
        sketch = path.join(ROOT_DIR, '../test-resources/layer_styles/layer_styles.sketch')
        output = path.join(ROOT_DIR, "../test-resources/layer_styles/generated", str(uuid4()))
        process_json(json, sketch, output)

        # ensure it worked
        reference = path.join(ROOT_DIR, '../test-resources/layer_styles/Stylist+layerStyles.swift')
        generated = path.join(output, 'Stylist+layerStyles.swift')
        self.assertTrue(filecmp.cmp(reference, generated), 'files are different - diff {0} {1}'.format(reference, generated))
        rmtree(output)

    def test_layer_styles_with_variants(self):
        # run the process
        json = path.join(ROOT_DIR, '../test-resources/variants/variants_examples_layerstyles.json')
        sketch = path.join(ROOT_DIR, '../test-resources/variants/variants_examples_layerstyles.sketch')
        output = path.join(ROOT_DIR, "../test-resources/variants/generated", str(uuid4()))
        process_json(json, sketch, output)

        # ensure it worked
        reference = path.join(ROOT_DIR, '../test-resources/variants/Stylist+layerStyles.swift')
        generated = path.join(output, 'Stylist+layerStyles.swift')
        self.assertTrue(filecmp.cmp(reference, generated), 'files are different - diff {0} {1}'.format(reference, generated))
        rmtree(output)


if __name__ == '__main__':
    unittest.main()


