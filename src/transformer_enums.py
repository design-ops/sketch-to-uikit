import yaml
import pybars
import os
from utils import read_template
from root import ROOT_DIR


def parse(data_str: [str]) -> dict:
    assets = set()
    elements = set()
    sections = set()
    variants = set()
    text = set()
    layer = set()

    for index, string in enumerate(data_str):
        try:
            data = yaml.load(string)
            if data.get("asset"):
                [assets.add(x) for x in data["asset"]]
            if data.get("element"):
                [elements.add(x) for x in data["element"]]
            if data.get("section"):
                [sections.add(x) for x in data["section"]]
            if data.get("variant"):
                [variants.add(x) for x in data["variant"]]
            if data.get("atom_text"):
                [text.add(x) for x in data["atom_text"]]
            if data.get("atom_layer"):
                [layer.add(x) for x in data["atom_layer"]]
        except yaml.YAMLError:
            print("🚨 WARNING 🚨 Enums failed to parse file #"+str(index))

    filtered_variants = filter_known_variants(variants)

    ret = {
        "assets": list(assets),
        "elements": list(elements),
        "sections": list(sections),
        "variants": filtered_variants,
        "text": list(text),
        "layer": list(layer)
    }
    ret["assets"].sort()
    ret["elements"].sort()
    ret["sections"].sort()
    ret["variants"].sort()
    ret["text"].sort()
    ret["layer"].sort()

    return ret


def filter_known_variants(variants: set) -> [str]:
    known_default_variants = ["normal", "highlighted", "disabled", "selected", "focused"]
    variants = [v for v in list(variants) if v not in known_default_variants]
    return variants


# TODO should this be an object to keep it DRY
def __parse_enum_file(src: str, data: dict) -> dict:
    lines = src.splitlines()
    parsing = None
    for line in lines:
        if parsing is None:
            if line.startswith("public enum PlatformAsset"):
                parsing = "Asset"
            elif line.startswith("public enum PlatformElement"):
                parsing = "Element"
            elif line.startswith("public enum PlatformSection"):
                parsing = "Section"
        elif parsing == "Asset":
            if line.strip().startswith("case"):
                enum = line.strip().split(" ")[1]
                data["assets"].add(enum)
            elif line.strip().startswith("}"):
                parsing = None
        elif parsing == "Element":
            if line.strip().startswith("case"):
                enum = line.strip().split(" ")[1]
                data["elements"].add(enum)
            elif line.strip().startswith("}"):
                parsing = None
        elif parsing == "Section":
            if line.strip().startswith("case"):
                enum = line.strip().split(" ")[1]
                data["sections"].add(enum)
            elif line.strip().startswith("}"):
                parsing = None

    return data


def swift_assets(data: dict) -> str:
    return template_assets(data)


def swift_elements(data: dict) -> str:
    return template_elements(data)


def swift_sections(data: dict) -> str:
    return template_sections(data)


def swift_variants(data: dict) -> str:
    return template_variants(data)


def swift_text_styles(data: dict) -> str:
    return template_text(data)


def swift_layer_styles(data: dict) -> str:
    return template_layer(data)


compiler = pybars.Compiler()
template_assets = compiler.compile(read_template(ROOT_DIR + '/../resources/templates/enums/assets.mustache'))
template_elements = compiler.compile(read_template(ROOT_DIR + '/../resources/templates/enums/elements.mustache'))
template_sections = compiler.compile(read_template(ROOT_DIR + '/../resources/templates/enums/sections.mustache'))
template_variants = compiler.compile(read_template(ROOT_DIR + '/../resources/templates/enums/variants.mustache'))
template_text = compiler.compile(read_template(ROOT_DIR + '/../resources/templates/enums/text.mustache'))
template_layer = compiler.compile(read_template(ROOT_DIR + '/../resources/templates/enums/layer.mustache'))
