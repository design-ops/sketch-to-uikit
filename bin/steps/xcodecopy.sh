#!/bin/bash

source "$( dirname "${BASH_SOURCE[0]}" )/_lib.sh"

input_dir="${plugin_project_path}/output/"

function show_help_and_exit {
    cat <<HELPTEXT

xcodecopy - copy files into Xcode

SYNOPSIS

    ./xcodecopy.sh -i path/to/generated/code -a path/to/xcode/project

MANDATORY ARGUMENTS

    -i  path to folder containing generated code
    -a  path to xcode app folder

OPTIONAL ARGUMENTS

    -h  display this help text

HELPTEXT
    exit 1
}


function run_docker_copy {
    docker_run ruby copy_to_xcode/copy_to_xcode.rb -a ${app_folder} -i ${input_dir}
}


# Parse command line args...
while getopts i:a:h: opt; do
    case $opt in
        i)
            input_dir=$OPTARG
            ;;
        a)
            app_folder=$OPTARG
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
run_docker_copy
