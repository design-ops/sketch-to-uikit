#!/bin/bash

source "$( dirname "${BASH_SOURCE[0]}" )/_lib.sh"

output_dir="${plugin_project_path}/output/"

function show_help_and_exit {
    cat <<HELPTEXT

general - generate supplementary StylableUIKit Files

SYNOPSIS

    ./general.sh

OPTIONAL ARGUMENTS

    -o  path to folder to generate code into (defaults to output folder in project)
    -h  display this help text

HELPTEXT
    exit 1
}

function copy_files {
    echo "🏃 adding AppStylist.swift"
    docker_run cp resources/general/AppStylist.swift ${output_dir}AppStylist.swift
    echo "🏃 adding Stylist+animatedAsset.swift"
    docker_run cp resources/general/Stylist+animatedAsset.swift ${output_dir}Stylist+animatedAsset.swift
}

# Parse command line args...
while getopts o:h: opt; do
    case $opt in
        o)
            output_dir=$OPTARG
            ;;
        h)
            show_help_and_exit
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            show_help_and_exit
            ;;
    esac
done

copy_files
