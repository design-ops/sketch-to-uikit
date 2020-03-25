# An Asset is a file, that is a particular instance of an icon, etc
import os
from typing import Optional, List
from dataclasses import dataclass
from itertools import groupby

from data.styles import BaseStyle, ItemGrouping, LayerStyle
from utils import empty_str
import re
import n2w
import stringcase

@dataclass
class AssetFile(BaseStyle):

    filename: str
    path: str
    context: str
    scale: Optional[str]

    @staticmethod
    def build(dir_entry: os.DirEntry, context: str):
        filename = dir_entry.name
        path = dir_entry.path
        context_as_array = context.split("/")
        context = context.replace("/", "_")  # context is a partial path section/organism/molecule (or less)

        if len(context_as_array) == 2:
            section = None
            element = None
            variant = None

            if context_as_array[0] != "*":
                section = context_as_array[0]

            if context_as_array[1] != "*":
                element_and_variant = context_as_array[1]
                pattern = r"(.+)\[(.+)\]" # searches for elements like elementName[variantName]
                match = re.search(pattern, element_and_variant)
                if match:
                    element = match.group(1)
                    variant = match.group(2)
                else:
                    element = element_and_variant

        else:
            # something unexpected happened...
            print(filename + ' has caused an error: expected "' + context + '" to have exactly 2 parts')
            return None
            # sys.exit(0)

        if section is None and element is None:
            asset_grouping = ItemGrouping.ATOM

        elif section is None and element is not None:
            asset_grouping = ItemGrouping.ELEMENT_ATOM

        elif section is not None and element is None:
            asset_grouping = ItemGrouping.SECTION_ATOM

        elif section is not None and element is not None:
            asset_grouping = ItemGrouping.SECTION_ELEMENT_ATOM

        atom = AssetFile.__name(filename)
        scale = AssetFile.__scale(filename)

        if section == "default":
            print('found default on '+path+" - "+filename)

        return AssetFile(atom=atom,
                         element=element,
                         section=section,
                         name=filename,
                         variant=variant,
                         grouping=asset_grouping,
                         filename=filename,
                         path=path,
                         context=context,
                         scale=scale)

    @staticmethod
    def __name(file_name: str) -> str:
        name = file_name.split('.')[0].split('@')[0].replace(' ', '')
        if name[0].isdigit():
            #  find numbers in the begin of the asset name
            number = [int(s) for s in re.findall(r'-?\d+\.?\d*', name)][0]
            #  convert number in words
            number_name = n2w.convert(number)
            #  remove numbers from name
            name = name[len(str(number)):]
            #  join number words to name without number in begin
            name = number_name + ' ' + name
            # convert to snake case to convert after to camelcase (don't work convert directly to camel case) 
            name = stringcase.snakecase(name)
            name = stringcase.camelcase(name)

        return name

    @staticmethod
    def __scale(path: str) -> Optional[str]:
        if path.split('.')[-1] == 'pdf':
            return None
        try:
            return path.split('@')[1].split('.')[0]
        except:
            return "1x"


@dataclass
class BaseGroup:
    atom: str
    element: Optional[str]
    section: Optional[str]
    grouping: ItemGrouping
    items: [BaseStyle]

    def get(self, key: str) -> Optional[str]:
        switcher = {
            "section": self.section,
            "element": self.element,
            "atom": self.atom
        }
        return switcher.get(key, None)


# An AssetGroup is a grouping of all sizes of an AssetFile (aka a particular icon, graphic etc)
# @TODO AssetGroup should inherit from BaseStyle not BaseGroup
@dataclass
class AssetGroup(BaseGroup):
    variant: Optional[str]

    @property
    def name(self):
        return empty_str('*/', self.section, "", "/") \
               + empty_str('*', self.element, "", "") \
               + empty_str('[]', self.items[0].variant, "[", "]") \
               + "/" + self.atom

    @property
    def context(self):
        return empty_str('*_', self.section, "", "_") \
               + empty_str('*_', self.element, "", "_") \
               + self.atom \
               + empty_str('', self.items[0].variant, "_", "")

    def imageset_name(self):
        return "%s.imageset" % self.context

    def path_appending(self, path: str):
        return os.path.join(path, self.imageset_name())

    @property
    def variant_object(self):
        if self.variant is None:
            return "UIControl.State.normal"
        switcher = {
            "normal": "UIControl.State.normal",
            "highlighted": "UIControl.State.highlighted",
            "disabled": "UIControl.State.disabled",
            "selected": "UIControl.State.selected",
            "focused": "UIControl.State.focused",
        }
        control_state = switcher.get(self.variant, None)
        if control_state is not None:
            return control_state
        # return a special variant
        return "AppVariant."+self.variant


@dataclass
class VariantGroup(BaseGroup):
    main: BaseStyle

    @classmethod
    def create_array_from_base_styles(cls, arr: List[BaseStyle]) -> []:

        group_by = lambda n: str(n.atom) + str(n.element) + str(n.section)
        arr.sort(key=group_by)
        sorted_arr: List[VariantGroup] = []
        orphaned_variants: List[List[BaseStyle]] = []
        orphaned_variant_names: List[str] = []

        for key, group in groupby(arr, group_by):
            variants: List[BaseStyle] = []
            main: BaseStyle = None
            for item in group:
                if item.variant is None or item.variant == "normal":
                    if main is None:  # first match gets stored
                        main = item
                    else:  # deal with duplicates or conflicts (/element/ & /element[normal]/)
                        if main.variant is None:
                            if item.variant is not None:
                                main = item
                                print('WARNING conflicting normal variant for ' + item.name)
                        else:  # main.variant is not None
                            if item.variant is not None:
                                print('WARNING duplicate normal variant for ' + item.name)
                else:
                    if item not in variants:
                        variants.append(item)
                    else:
                        print('WARNING rejected duplicate item:' + item.name)

            if main is not None:
                instance = VariantGroup(atom=main.atom, element=main.element, section=main.section,
                                        grouping=main.grouping,
                                        main=main, items=variants)
                sorted_arr.append(instance)
            elif len(variants) > 0:
                orphaned_variants.append(variants)
                orphaned_variant_names.append(variants[0].name)

        # loop back and find default (*/*/) values for variants
        for variants in orphaned_variants:
            item = variants[0]
            for variant_group in sorted_arr:
                if variant_group.section is None and variant_group.element is None and variant_group.atom == item.atom:
                    main = variant_group.main
                    instance = VariantGroup(
                        atom=item.atom, element=item.element, section=item.section,
                        grouping=item.grouping,
                        main=main, items=variants
                    )
                    sorted_arr.append(instance)
                    orphaned_variant_names.remove(item.name)
                    break

        [print("🚨WARNING🚨 Orphaned Variant (no default found) - ", n) for n in orphaned_variant_names]

        return sorted_arr

    def items_with_layer_style_image(self) -> [LayerStyle]:
        arr: [LayerStyle] = [item for item in self.items if (type(item) is LayerStyle) & (item.image is not None)]
        if (type(self.main) is LayerStyle) & (self.main.image is not None):
            arr.append(self.main)

        return arr

