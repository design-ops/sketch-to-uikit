
import unittest
from process_text_styles import process_json
from root import ROOT_DIR
import filecmp
from os import path
from uuid import uuid4
from shutil import rmtree

class ProcessTextStylesTest(unittest.TestCase):

    def test_text_styles(self):
        # run the process
        json = path.join(ROOT_DIR, '../test-resources/text_styles/text_styles.json')
        output = path.join(ROOT_DIR, '../test-resources/text_styles/generated', str(uuid4()))
        process_json(json, output)

        # ensure it worked
        reference = path.join(ROOT_DIR, '../test-resources/text_styles/Stylist+textStyles.swift')
        generated = path.join(output, 'Stylist+textStyles.swift')
        self.assertTrue(filecmp.cmp(reference, generated), 'files are different - diff {0} {1}'.format(reference, generated))
        rmtree(output)


    def test_text_styles_with_variants(self):
        # run the process
        json = path.join(ROOT_DIR, '../test-resources/variants/variants_examples_textstyles.json')
        output = path.join(ROOT_DIR, '../test-resources/variants/generated', str(uuid4()))
        process_json(json, output)

        # ensure it worked
        reference = path.join(ROOT_DIR, '../test-resources/variants/Stylist+textStyles.swift')
        generated = path.join(output, 'Stylist+textStyles.swift')
        self.assertTrue(filecmp.cmp(reference, generated), 'files are different - diff {0} {1}'.format(reference, generated))
        rmtree(output)


if __name__ == '__main__':
    unittest.main()