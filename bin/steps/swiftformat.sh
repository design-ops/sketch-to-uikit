#!/bin/bash

source "$( dirname "${BASH_SOURCE[0]}" )/_lib.sh"

input_dir="${plugin_project_path}/output/"

function show_help_and_exit {
    cat <<HELPTEXT

swiftformat - format code of generated swift files

SYNOPSIS

    ./swiftformat.sh -i /path/to/swift/files

MANDATORY ARGUMENTS

    -i  path to folder containing generated swift files

OPTIONAL ARGUMENTS

    -h  display this help text

HELPTEXT
    exit 1
}

function run_docker_swiftformat {
    docker_run swiftformat ${input_dir} --swiftversion 5
}

# Parse command line args...
while getopts i:a:p:o:k:h: opt; do
    case $opt in
        i)
            input_dir=$OPTARG
            echo "📄 input folder is $OPTARG"
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
run_docker_swiftformat
