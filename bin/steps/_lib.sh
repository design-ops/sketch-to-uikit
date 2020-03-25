#!/bin/bash
export VERSION=3.0.0

# get the plugin path so the steps can use it
current_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
plugin_project_path="${current_dir}/../.."


function check_docker_is_installed {
  echo "docker is: $(command -v docker)"
  if [ "$DOCKER_INSTALLED" != "true" ]; then
    if [ -x "$(command -v docker)" ]; then
        echo "👍 Docker is installed"
        export DOCKER_INSTALLED=true
    else
        cat <<NO_DOCKER
🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨

ERROR - docker does not appear to be installed

Please ensure docker is installed and that the docker command is available on the command line.

Get docker here - https://www.docker.com/get-docker

Once installed check that you can run it from the command line by running

    docker -v

which should return the installed docker version.

NO_DOCKER
        exit 1
    fi
  fi
}

function check_docker_image_installed {
  if [[ "$DOCKER_IMAGE_INSTALLED" != "true" ]]; then
    if docker images | tr -s " " | grep "sketch-to-stylable-uikit $VERSION" &> /dev/null ; then
        echo "👍 Docker image is installed"
        export DOCKER_IMAGE_INSTALLED=true
    else
        cat <<NO_CODEGEN_IMAGE
🚨🚨🚨🚨🚨🚨🚨🚨🚨🚨

ERROR - the correct Docker image does not appear to be installed

Run the bin/setup to build the docker image and try again.

NO_CODEGEN_IMAGE
        exit 1
    fi
  fi
}

# Docker on OS X requires an additional arg so we need to know if we are on a mac.
function check_for_osx {
    if uname | grep 'Darwin' &> /dev/null ; then
        echo "🍎 running on a mac"
        expose_computer_to_docker="-v /Users:/Users"
    else
        echo "🤓 not running on a mac"
        # presume we're running on Linux
        expose_computer_to_docker="-v /home:/home"
    fi

}

function enable_dev_mode {
    export DEV_MODE=true
}

function docker_run {
    check_for_osx
    if [[ "${DEV_MODE}" == "true" ]]; then
        dev_str="-v ${plugin_project_path}:/work "
    else
        dev_str=""
    fi
    docker run ${dev_str} ${expose_computer_to_docker} -w /work sketch-to-stylable-uikit $*
}