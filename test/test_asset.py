import unittest
from data.asset import AssetFile
from data.asset import ItemGrouping


class AssetsTest(unittest.TestCase):

    def test_no_context(self):
        dir_entry = PseudoDirEntry(name='atom.pdf', path='/working/*/*/atom.pdf', is_dir=False, stat=True)
        asset_build = AssetFile.build(dir_entry=dir_entry, context="*/*")
        asset_hand = AssetFile(filename='atom.pdf', path='/working/*/*/atom.pdf', context='*_*',
                           atom='atom', element=None, section=None,
                           scale=None, grouping=ItemGrouping.ATOM, variant=None, name="atom.pdf")
        self.assertEqual(asset_hand, asset_build, "expect default (atoms) to be equal")

    def test_molecule(self):
        dir_entry = PseudoDirEntry(name='atom.pdf', path='/working/*/molecule/atom.pdf', is_dir=False, stat=True)
        asset_build = AssetFile.build(dir_entry=dir_entry, context="*/molecule")
        asset_hand = AssetFile(filename='atom.pdf', path='/working/*/molecule/atom.pdf', context='*_molecule',
                           atom='atom', element='molecule', section=None,
                           scale=None, grouping=ItemGrouping.ELEMENT_ATOM, variant=None, name="atom.pdf")
        self.assertEqual(asset_hand, asset_build, "expect molecules to be processed")

    def test_section(self):
        dir_entry = PseudoDirEntry(name='atom.pdf', path='/working/section/*/atom.pdf', is_dir=False, stat=True)
        asset_build = AssetFile.build(dir_entry=dir_entry, context="section/*")
        asset_hand = AssetFile(filename='atom.pdf', path='/working/section/*/atom.pdf', context='section_*',
                           atom='atom', element=None, section='section',
                           scale=None, grouping=ItemGrouping.SECTION_ATOM, variant=None, name="atom.pdf")
        self.assertEqual(asset_hand, asset_build, "expect just sections to be processed")

    def test_section_and_molecule(self):
        dir_entry = PseudoDirEntry(name='atom.pdf', path='/working/section/molecule/atom.pdf', is_dir=False, stat=True)
        asset_build = AssetFile.build(dir_entry=dir_entry, context="section/molecule")
        asset_hand = AssetFile(filename='atom.pdf', path='/working/section/molecule/atom.pdf', context='section_molecule',
                           atom='atom', element='molecule', section='section',
                           scale=None, grouping=ItemGrouping.SECTION_ELEMENT_ATOM, variant=None, name="atom.pdf")
        self.assertEqual(asset_hand, asset_build, "expect sections and molecules to be processed")

    def test_no_context_with_numbers(self):
        dir_entry = PseudoDirEntry(name='360video.pdf', path='/working/*/*/360video.pdf', is_dir=False, stat=True)
        asset_build = AssetFile.build(dir_entry=dir_entry, context="*/*")
        asset_hand = AssetFile(filename='360video.pdf', path='/working/*/*/360video.pdf', context='*_*',
                           atom='threeHundredSixtyVideo', element=None, section=None,
                           scale=None, grouping=ItemGrouping.ATOM, variant=None, name="360video.pdf")
        self.assertEqual(asset_hand, asset_build, "expect default (atoms) to be equal")


class PseudoDirEntry:
    def __init__(self, name, path, is_dir, stat):
        self.name = name
        self.path = path
        self._is_dir = is_dir
        self._stat = stat

    def is_dir(self):
        return self._is_dir

    def stat(self):
        return self._stat


if __name__ == '__main__':
    unittest.main()