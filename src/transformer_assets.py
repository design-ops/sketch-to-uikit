from data.asset import AssetGroup, AssetFile, ItemGrouping, VariantGroup
from utils import *
import pybars
import os
from root import ROOT_DIR
from itertools import groupby
from shutil import copyfile
from typing import List
import yaml


def move_assets(asset_list: [AssetGroup], output_dir: str) -> None:
    # make xcassets folder inside output_dir
    assets_dir = os.path.join(output_dir, 'StylableUIKitAssets.xcassets')
    create_dir(assets_dir)

    # move AssetFiles inside AssetGroups into output
    [__write_asset_group(asset_group, assets_dir) for asset_group in asset_list]

    # write Contents.json inside AssetGroup folders
    [__write_meta_data(asset_group, assets_dir) for asset_group in asset_list]


def create_metadata_from_assets(asset_list: [AssetFile]) -> dict:
    grouped_list = __create_layout_element_atom_groups(asset_list)
    unique_atoms = __unique_entries(asset_list, "atom")
    unique_elements = __unique_entries(asset_list, "element")
    unique_sections = __unique_entries(asset_list, "section")
    unique_variants = __unique_entries(asset_list, "variant")
    return {"atoms": unique_atoms,
            "elements": unique_elements,
            "sections": unique_sections,
            "variants": unique_variants,
            "grouped": grouped_list}


def swift_code(data: dict) -> str:
    return template_stylist(data, partials={'asset': asset_partial})


def enum_report(data: dict) -> str:
    enums = {
        "asset": data["atoms"],
        "element": data["elements"],
        "section": data["sections"],
        "variant": data["variants"]
    }
    return yaml.dump(enums)


def __write_asset_group(asset_group: AssetGroup, assets_dir: str) -> None:
    output_path = asset_group.path_appending(path=assets_dir)
    create_dir(output_path)

    [copyfile(asset.path, os.path.join(output_path, os.path.basename(asset.filename))) for asset in asset_group.items]


def __write_meta_data(asset_group: AssetGroup, assets_dir: str) -> None:
    output_path = asset_group.path_appending(path=assets_dir)
    write_file(os.path.join(output_path, 'Contents.json'), mustache_json(asset_group))


def asset_groups_from_dir(input_dir: str) -> [AssetGroup]:
    asset_groups = []

    # get all of the folders that we want to process in the input dir
    # (aka everything that doesn't start with an underscore)

    asset_dirs = [entry for entry in os.scandir(input_dir)
                  if entry.is_dir and entry.name[:1] != "_"]

    assets = [__get_assets(d) for d in asset_dirs if d.is_dir()]
    assets = __remove_empty(flatten(assets))
    assets.sort(key=__groupby_name_context())

    for key, group in groupby(assets, __groupby_name_context()):
        asset_acc: List[AssetFile] = []
        for asset in group:
            if asset not in asset_acc:
                asset_acc.append(asset)
            else:
                print('rejected duplicate asset:'+asset.path+" "+asset.filename)
        asset_groups.append(
            AssetGroup(atom=asset.atom,
                       element=asset.element,
                       section=asset.section,
                       grouping=asset.grouping,
                       items=asset_acc,
                       variant=asset.variant)
        )
    return asset_groups


def __groupby_name_context():
    return lambda asset: asset.atom + str(asset.element) + str(asset.section) + str(asset.variant)


def __groupby_context():
    return lambda asset: str(asset.element) + str(asset.section)


def __unique_entries(asset_list: [AssetGroup], key: str) -> [AssetGroup]:
    unique = set()
    unique_assets = [getattr(x, key) for x in asset_list if (getattr(x, key) is not None) and not (getattr(x, key) in unique or unique.add(getattr(x, key)))]
    unique_assets.sort()
    return unique_assets


def __get_assets(dir_entry: os.DirEntry) -> [[AssetFile]]:
    return [_process_file_or_dir(dir_entry.name, f) for f in os.scandir(dir_entry.path) if f.name[:1] != "." and f.name[:1] != "_"]


# path is the full path,
def _process_file_or_dir(context: str, dir_entry: os.DirEntry) -> [[AssetFile]]:
    if dir_entry.is_file():
        return AssetFile.build(dir_entry=dir_entry, context=context)
    else:
        new_context = os.path.join(context, dir_entry.name)
        return [_process_file_or_dir(new_context, f) for f in os.scandir(dir_entry.path) if f.name[:1] != "." and f.name[:1] != "_"]


def __remove_empty(l) -> []:
    return [e for e in l if e]


def __create_layout_element_atom_groups(asset_groups: [AssetGroup]) -> dict:
    buckets = {}
    asset_groups = VariantGroup.create_array_from_base_styles(asset_groups)
    buckets["layout_element_atom"] = [ag for ag in asset_groups if ag.grouping == ItemGrouping.SECTION_ELEMENT_ATOM]
    buckets["layout_atom"] = [ag for ag in asset_groups if ag.grouping == ItemGrouping.SECTION_ATOM]
    buckets["element_atom"] = [ag for ag in asset_groups if ag.grouping == ItemGrouping.ELEMENT_ATOM]
    buckets["atom"] = [ag for ag in asset_groups if ag.grouping == ItemGrouping.ATOM]
    buckets["has_layout_element_atom"] = len(buckets["layout_element_atom"]) > 0
    buckets["has_layout_atom"] = len(buckets["layout_atom"]) > 0
    buckets["has_element_atom"] = len(buckets["element_atom"]) > 0
    return buckets


compiler = pybars.Compiler()
mustache_json = compiler.compile(read_template(ROOT_DIR + '/../resources/assets_json.mustache'))
template_stylist = compiler.compile(read_template(ROOT_DIR + '/../resources/assets_swift_stylist.mustache'))
asset_partial = compiler.compile(read_template(ROOT_DIR + '/../resources/assets_swift_stylist_asset.mustache'))
