#!/bin/bash

source "$( dirname "${BASH_SOURCE[0]}" )/_lib.sh"
output_dir="${plugin_project_path}/output/"

function show_help_and_exit {
    cat <<HELPTEXT

textstyles - generate swift Stylist TextStyle code from a Sketch file

SYNOPSIS

    ./textstyles.sh -s sketch-file

MANDATORY ARGUMENTS

    -s  path to sketch file to process
    -j  path to json file to process (to bypass sketch)

OPTIONAL ARGUMENTS

    -o  path to folder to generate code into (defaults to output folder in project)
    -h  display this help text

HELPTEXT
    exit 1
}

function run_sketchtool {
    if [[ "${skip_sketchtool}" = true ]] ; then
        echo "😎 skipping sketchtool step"
    else
        echo "🏃 extracting contents of sketch file '${sketch_file}'"
        json_dir="${output_dir}/tmp"
        mkdir $json_dir
        json_file="${output_dir}/tmp/tmp.json"

        tmp_dir=$(mktemp -d -t stylable-uikit)
        unzip -qq "${sketch_file}" -d "${tmp_dir}"
        cat "${tmp_dir}/document.json" | docker run -i sketch-to-stylable-uikit jq '{layerTextStyles: .layerTextStyles, foreignTextStyles: [.foreignTextStyles[].localSharedStyle]}' > "${json_file}"
        rm -rf "${tmp_dir}"
    fi
}

function run_docker_styles {
    if [[ "${skip_build}" = true ]] ; then
        echo "😎 skipping build step"
    else
        echo "🏃 running build with json file '${json_file}'"
        docker_run python src/process_text_styles.py --input "${json_file}" --output "${output_dir}"
        if [[ -z "${keep_files}" ]] ; then
            rm -f "${json_file}"
            rmdir "${json_dir}"
        fi
    fi
}

# Parse command line args...
while getopts s:j:o:h:k opt; do
    case $opt in
        s)
            sketch_file=$OPTARG
            echo "📄 sketch file is $OPTARG"
            ;;
        j)
            json_file=$OPTARG
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
            echo "🤓 not deleting temporary json file (for dev use)"
            ;;
        \?)
            echo "Invalid option: -$OPTARG"
            show_help_and_exit
            ;;
    esac
done

check_docker_is_installed
check_docker_image_installed
run_sketchtool
run_docker_styles
