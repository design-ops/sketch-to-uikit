# StylableUIKit
from argparse import ArgumentParser
from sys import exit
from os import path, makedirs

from utils import read_json, write_file
from transformer_layer_styles import parse, process_background_images, swift_code, enum_report


def process_json(input_file: str, sketch_doc: str, output_folder: str):
    print("layer_styles: input_file:"+input_file)
    print("layer_styles: sketch_doc:"+sketch_doc)
    print("layer_styles: output_folder:"+output_folder)

    output_swift = path.join(output_folder, "Stylist+layerStyles.swift")
    output_enums = path.join(output_folder, "enums_layer.yaml")


    try:
        sketch_json = read_json(input_file)
    except IOError:
        print('Could not open file ' + input_file)
        exit(0)

    layer_styles_data = parse(sketch_json)

    process_background_images(layer_styles_data, sketch_doc, output_folder)

    swift_doc = swift_code(layer_styles_data)
    enums_doc = enum_report(layer_styles_data)

    # Create output directory if it doesn't exist.
    if not path.exists(output_folder):
        makedirs(output_folder)

    try:
        write_file(output_swift, swift_doc)
    except IOError:
        print('Could not write layerStyles swift file ' + output_swift)

    try:
        write_file(output_enums, enums_doc)
    except IOError:
        print('Could not write layerStyles enums yaml file ' + output_swift)


if __name__ == '__main__':
    # Set up the command line app
    parser = ArgumentParser()
    parser.add_argument("--input-json", help="path of input JSON file", nargs="+")
    parser.add_argument("--input-sketch", help="path of input Sketch file", nargs="+")
    parser.add_argument("--output", help="path of output file", nargs="+")
    args = parser.parse_args()
    # run the process
    process_json(' '.join(args.input_json), ' '.join(args.input_sketch), ' '.join(args.output))
