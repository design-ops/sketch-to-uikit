from argparse import ArgumentParser
from sys import exit
from os import path, makedirs

from utils import read_json, write_file
from transformer_text_styles import *


def process_json(input_file: str, output_folder: str):
    output_swift = path.join(output_folder, "Stylist+textStyles.swift")
    output_enums = path.join(output_folder, "enums_text.yaml")

    try:
        sketch_json = read_json(input_file)
    except:
        print('Could not open file ' + input_file)
        exit(0)

    text_styles_data = parse(sketch_json)
    swift_doc = swift_code(text_styles_data)
    enums_doc = enum_report(text_styles_data)

    # Create output directory if it doesn't exist.
    if not path.exists(output_folder):
        makedirs(output_folder)

    try:
        write_file(output_swift, swift_doc)
    except IOError:
        print('Could not write textStyles swift file ' + output_swift)

    try:
        write_file(output_enums, enums_doc)
    except IOError:
        print('Could not write textStyles enum file ' + output_swift)


if __name__ == '__main__':
    # Set up the command line app
    parser = ArgumentParser()
    parser.add_argument("--input", help="path of input file")
    parser.add_argument("--output", help="path of output file")
    args = parser.parse_args()
    # run the process
    process_json(args.input, args.output)

