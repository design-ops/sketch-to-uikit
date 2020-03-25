import unittest
from process_assets import process_assets
from root import ROOT_DIR
from uuid import uuid4
from os import path
from shutil import rmtree
from tempfile import gettempdir


class ProcessAssetsTest(unittest.TestCase):

    def test_process_assets_bad_dir(self):
        with self.assertRaises(FileNotFoundError):
            process_assets(path.join(ROOT_DIR, '../test-resources/missing'), gettempdir(), "0")

    def test_process_assets(self):
        output_dir = path.join(ROOT_DIR, "../test-resources/assets/generated/files", str(uuid4()))
        process_assets(path.join(ROOT_DIR, '../test-resources/assets/source'),
                       output_dir, "1")
        # Comment out if you want to hold onto the generated files
        rmtree(output_dir)


if __name__ == '__main__':
    unittest.main()
