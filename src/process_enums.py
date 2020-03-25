import argparse
from utils import read_template, write_file
import os
from transformer_enums import *


def process_enums(input_folder: str, app_dir: str, output_folder: str, keep_files: str):
    enum_src: [str] = []
    enum_path: [str] = []  # so they can be removed later

    keep_files = (keep_files == "1")

    for dir_path, _, files in os.walk(input_folder):
        for file in (file for file in files if file.startswith("enums_") and file.endswith(".yaml")):
            file_path = os.path.join(dir_path, file)
            try:
                src = read_template(file_path)
                enum_src.append(src)
                enum_path.append(file_path)
                print("✅ found enum '" + file + "'")
            except IOError:
                print("🚨 found '"+file_path+"' but it couldn't be loaded")

    if not enum_src:
        print("🚨 found no enums_*.yaml files, so nothing to process 😭")

    data = parse(enum_src)
    data["app_name"] = "App"

    enums_assets = swift_assets(data)
    enums_elements = swift_elements(data)
    enums_sections = swift_sections(data)
    enums_variants = swift_variants(data)
    enums_text_styles = swift_text_styles(data)
    enums_layer_styles = swift_layer_styles(data)

    output_assets = os.path.join(output_folder, "{0}Assets.swift".format(data["app_name"]))
    output_elements = os.path.join(output_folder, "{0}Elements.swift".format(data["app_name"]))
    output_sections = os.path.join(output_folder, "{0}Sections.swift".format(data["app_name"]))
    output_variants = os.path.join(output_folder, "{0}Variants.swift".format(data["app_name"]))
    output_text = os.path.join(output_folder, "{0}TextStyles.swift".format(data["app_name"]))
    output_layer = os.path.join(output_folder, "{0}LayerStyles.swift".format(data["app_name"]))

    try:
        write_file(output_assets, enums_assets)
    except IOError:
        print('Could not write enums assets file ' + output_assets)

    try:
        write_file(output_elements, enums_elements)
    except IOError:
        print('Could not write enums elements file ' + output_elements)

    try:
        write_file(output_sections, enums_sections)
    except IOError:
        print('Could not write enums sections file ' + output_sections)

    try:
        write_file(output_variants, enums_variants)
    except IOError:
        print('Could not write enums variants file ' + output_variants)

    try:
        write_file(output_text, enums_text_styles)
    except IOError:
        print('Could not write enums text identifier file ' + output_text)

    try:
        write_file(output_layer, enums_layer_styles)
    except IOError:
        print('Could not write enums layer identifier file ' + output_layer)

    if not keep_files:
        [os.remove(source_file) for source_file in enum_path]


if __name__ == '__main__':
    # Set up the command line app
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path of input folder")
    parser.add_argument("--app_dir", help="path of xcode app folder")
    parser.add_argument("--output", help="path of output folder")
    parser.add_argument("--keep_files", help="don't delete the found enum files", default="0")
    args = parser.parse_args()
    # Run the app
    process_enums(args.input, args.app_dir, args.output, args.keep_files)
