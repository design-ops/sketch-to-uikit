# Set up the command line app
import argparse
from utils import write_file
import os
from transformer_assets import *
from shutil import rmtree


def process_assets(input_dir: str, output_dir: str, keep_files: str):
    output_swift = os.path.join(output_dir, 'Stylist+assets.swift')
    output_enums = os.path.join(output_dir, "enums_assets.yaml")

    asset_list = asset_groups_from_dir(input_dir)
    move_assets(asset_list, output_dir)

    assets_data = create_metadata_from_assets(asset_list)
    swift_code_output = swift_code(assets_data)
    enum_report_output = enum_report(assets_data)

    try:
        write_file(output_swift, swift_code_output)
    except IOError:
        print('Could not write assets swift file ' + output_swift)

    try:
        write_file(output_enums, enum_report_output)
    except IOError:
        print('Could not write assets enum file ' + output_enums)

    keep_files = (keep_files == "1")
    if not keep_files:
        rmtree(input_dir)


if __name__ == '__main__':
    # Set up the command line app
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="path of input file")
    parser.add_argument("--output", help="path of output file")
    parser.add_argument("--keep_files", help="don't delete intermediary files", default="0")
    args = parser.parse_args()
    # run the process
    process_assets(args.input, args.output, args.keep_files)
