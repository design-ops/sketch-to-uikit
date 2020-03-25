#!/bin/bash

source "$( dirname "${BASH_SOURCE[0]}" )/_lib.sh"

input_dir="${plugin_project_path}/output/"
output_dir="${plugin_project_path}/output/"


function show_help_and_exit {
    cat <<HELPTEXT

enums - generate swift Stylist Enums from a Sketch file

SYNOPSIS

    ./enums.sh -i /path/to/_enum.yaml/files

MANDATORY ARGUMENTS

    -i  path to folder containing _enum.yaml files

OPTIONAL ARGUMENTS

    -a  path to xcode app project's folder
    -o  path to folder to generate code into (defaults to output folder in project)
    -h  display this help text

HELPTEXT
    exit 1
}

function run_docker_enums {
    additional_params=""
    if [[ ! -z "$keep_files" ]] ; then
        additional_params="${additional_params} --keep_files 1"
    fi
    docker_run python src/process_enums.py --input ${input_dir} --output ${output_dir} ${additional_params}
}

# Parse command line args...
while getopts i:a:p:o:k:h: opt; do
    case $opt in
        i)
            input_dir=$OPTARG
            echo "📄 input folder is $OPTARG"
            ;;
        a)
            app_folder=$OPTARG
            echo "📄 xcode app folder is $OPTARG"
            ;;
        p)
            platform_folder=$OPTARG
            echo "📄 xcode platform folder is $OPTARG"
            ;;
        o)
            output_dir=$OPTARG
            echo "📄 output folder is $OPTARG"
            ;;
        k)
            keep_files=1
            echo "🤓 not deleting enum files (for dev use)"
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

check_docker_is_installed
check_docker_image_installed
run_docker_enums
