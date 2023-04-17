#!/bin/bash

# ENV VARIABLES
export PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export MACHINE_NAME=$(hostname)
export USER_NAME=$(whoami)
export USER_ID=$(id -u)


# LOAD SCRIPTS
source "$PROJECT_DIR/scripts/log.sh"
source "$PROJECT_DIR/scripts/load_confs.sh"
source "$PROJECT_DIR/scripts/pip.sh"
source "$PROJECT_DIR/scripts/flask_app.sh"

# EXECUTE SCRIPTS
load_conf_files
pip_init
flask_app