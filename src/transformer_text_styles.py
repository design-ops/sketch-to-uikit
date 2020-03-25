import pybars
import yaml
from data.styles import ItemGrouping, TextStyle
from data.asset import VariantGroup
from data import styles
from root import ROOT_DIR
from utils import read_template

default_font = "ChalkboardSE-Regular"


def parse(sketch_json):
    original = [TextStyle.create_from_sketch_dict(i, default_font) for i in sketch_json['layerTextStyles']['objects']]
    original.extend([TextStyle.create_from_sketch_dict(i, default_font) for i in sketch_json['foreignTextStyles']])
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
    buckets["atoms"] = styles.unique_entries_dict(simplified, "atom")
    buckets["elements"] = styles.unique_entries_dict(simplified, "element")
    buckets["sections"] = styles.unique_entries_dict(simplified, "section")
    buckets["variants"] = styles.unique_entries_dict(original, "variant")
    data = {
        "objects": simplified,
        "grouped": buckets
    }
    return data


def swift_code(data):
    return template_stylist(data, partials={'text_style': partial_text_style, 'color': color_partial})


def enum_report(data: dict) -> str:
    enums = {
        "atom_text": data["grouped"]["atoms"],
        "element": data["grouped"]["elements"],
        "section": data["grouped"]["sections"],
        "variant": data["grouped"]["variants"]
    }
    return yaml.dump(enums)


root = ROOT_DIR + '/../resources/'
compiler = pybars.Compiler()
template_stylist = compiler.compile(read_template(root + 'text_swift_stylist.mustache'))
partial_text_style = compiler.compile(read_template(root + 'text_swift_stylist_textstyle.mustache'))
color_partial = compiler.compile(read_template(root + 'layer_swift_stylist_color.mustache'))
