#!/bin/bash

source "$( dirname "${BASH_SOURCE[0]}" )/_lib.sh"
output_dir="${plugin_project_path}/output/"

function show_help_and_exit {
    cat <<HELPTEXT

assets - generate swift Stylist Asset code from a Sketch file

SYNOPSIS

    ./assets.sh -s sketch-file

MANDATORY ARGUMENTS

    -s  path to sketch file to process
    -f  path to assets folder to process (to bypass sketch)

OPTIONAL ARGUMENTS

    -o  path to folder to generate code into (defaults to output folder in project)
    -h  display this help text
    -k  set this to any value to skip deleting the intermediary files

HELPTEXT
    exit 1
}

# Creates the output directory for the code generator and returns the fully qualified path.
# Note - we echo out the result of the function so we can capture this in a result variable.
function generate_output_directory {
    local full_asset_folder_path=$1

    mkdir $full_asset_folder_path

    local dir_name=$(date "+exported_%Y%m%d_%H%M-%S")

    local full_output_path="$full_asset_folder_path/$dir_name"

    mkdir $full_output_path

    echo -n $full_output_path
}

function run_sketchtool {
    if [[ "${skip_sketchtool}" = true ]] ; then
        echo "😎 skipping sketchtool step"
    else
        echo "🏃 running sketchtool with sketch file '${sketch_file}'"

        assets_dir=$(generate_output_directory ${output_dir}/tmp-assets/)

        # mkdir ${assets_dir}
        /Applications/Sketch.app/Contents/Resources/sketchtool/bin/sketchtool export layers "${sketch_file}" --output="${assets_dir}"
    fi
}

function run_docker_assets {
    if [ "${skip_build}" = true ] ; then
        echo "😎 skipping build step"
    else
        echo "🏃 running build with input folder '${assets_dir}'"
        additional_params=""
        if [ ! -z "$keep_files" ] ; then
            additional_params="${additional_params} --keep_files 1"
        fi
        docker_run python src/process_assets.py --input ${assets_dir} --output ${output_dir} ${additional_params}
    fi
}

# Parse command line args...
while getopts s:f:o:h:k: opt; do
    case $opt in
        s)
            sketch_file=$OPTARG
            echo "📄 sketch file is $OPTARG"
            ;;
        f)
            assets_dir=$OPTARG
            skip_sketchtool=true
            echo "📄 json file is $OPTARG"
            ;;
        o)
            output_dir=$OPTARG
            ;;
        h)
            show_help_and_exit
            ;;
        k)
            keep_files=1
            echo "🤓 not deleting asset files (for dev use)"
            ;;
        \?)
            echo "🚨 Invalid option: -$OPTARG"
            show_help_and_exit
            ;;
    esac
done

check_docker_is_installed
check_docker_image_installed
run_sketchtool
run_docker_assets
