import pybars
import yaml
import os
from os import PathLike

from data.styles import ItemGrouping, LayerStyle
from data.asset import VariantGroup
from data.file_mapping import extract_file_with_name
from data.styles import unique_entries_dict
from utils import *
from root import ROOT_DIR


def parse(sketch_json: dict) -> dict:
    original = [LayerStyle.create_from_sketch_dict(i) for i in sketch_json['layerStyles']['objects']]
    original.extend([LayerStyle.create_from_sketch_dict(i) for i in sketch_json['foreignLayerStyles']])
    simplified = VariantGroup.create_array_from_base_styles(original)
    buckets = {}
    buckets["section_element_atom"] = [ag for ag in simplified if ag.grouping == ItemGrouping.SECTION_ELEMENT_ATOM]
    buckets["section_atom"] = [ag for ag in simplified if ag.grouping == ItemGrouping.SECTION_ATOM]
    buckets["element_atom"] = [ag for ag in simplified if ag.grouping == ItemGrouping.ELEMENT_ATOM]
    buckets["atom"] = [ag for ag in simplified if ag.grouping == ItemGrouping.ATOM]
    buckets["has_section_element_atom"] = len(buckets["section_element_atom"]) > 0
    buckets["has_section_atom"] = len(buckets["section_atom"]) > 0
    buckets["has_element_atom"] = len(buckets["element_atom"]) > 0
    # enum data
    buckets["atoms"] = unique_entries_dict(simplified, "atom")
    buckets["elements"] = unique_entries_dict(simplified, "element")
    buckets["sections"] = unique_entries_dict(simplified, "section")
    buckets["variants"] = unique_entries_dict(original, "variant")

    data = {
        "objects": simplified,
        "grouped": buckets
    }
    return data


def swift_code(data: dict) -> str:
    return template_stylist(data, partials={'color': color_partial,
                                            'layer_style': layerstyle_partial,
                                            'gradient': gradient_partial,
                                            'outline': outline_partial})


def enum_report(data: dict) -> str:
    enums = {
        "atom_layer": data["grouped"]["atoms"],
        "element": data["grouped"]["elements"],
        "section": data["grouped"]["sections"],
        "variant": data["grouped"]["variants"]
    }
    return yaml.dump(enums)


def value_in_dict_or_default(d: dict, v1: str, default: str) -> str:
    if v1 in d:
        return d[v1]
    return default


def fix_value(existing: str, match: str, replace: str):
    if existing == match:
        return replace
    return existing


def process_background_images(style_data: dict, sketch_doc: PathLike, output_folder: PathLike) -> [LayerStyle]:
    array: [VariantGroup] = style_data["objects"]
    requires_processing = list(flatten([item.items_with_layer_style_image() for item in array]))
    if len(requires_processing) > 0:
        assets_dir = __create_assets_bundle(output_folder)
        [__add_file_to_assets_bundle(item, sketch_doc, assets_dir) for item in requires_processing]
    return array


def __create_assets_bundle(output_dir: PathLike) -> PathLike:
    assets_dir = os.path.join(output_dir, 'StylableUIKitLayers.xcassets')
    create_dir(assets_dir)
    return assets_dir


def __add_file_to_assets_bundle(item: LayerStyle, sketch_doc: PathLike, output_path: PathLike):
    destination_file = item.image["file_name"]+".imageset"
    export_path = os.path.join(output_path, destination_file)
    create_dir(export_path)
    image_ref = item.image["ref"]
    extract_file_with_name(sketch_doc, image_ref, export_path)
    # add Contents.json
    file_name = os.path.basename(image_ref)
    mustache_data = {"items": [{"filename": file_name}]}
    write_file(os.path.join(export_path, 'Contents.json'), mustache_json(mustache_data))


path = ROOT_DIR + '/../resources/'
compiler = pybars.Compiler()

mustache_json = compiler.compile(read_template(ROOT_DIR + '/../resources/assets_json.mustache'))
color_partial = compiler.compile(read_template(path + 'layer_swift_stylist_color.mustache'))
layerstyle_partial = compiler.compile(read_template(path + 'layer_swift_stylist_layerstyle.mustache'))
gradient_partial = compiler.compile(read_template(path + 'layer_swift_stylist_gradient.mustache'))
outline_partial = compiler.compile(read_template(path + 'layer_swift_stylist_outline.mustache'))
template_stylist = compiler.compile(read_template(path + 'layer_swift_stylist.mustache'))
