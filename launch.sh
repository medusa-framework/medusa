#!/bin/bash

# Set PROJECT_DIR environment variable to current directory
export PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Source utils.sh to load the load_conf_file() and load_conf_files() functions
source "$PROJECT_DIR/scripts/utils.sh"

# Load variables from all .conf files
load_conf_files
echo "Environment variables loaded from .conf files in $PROJECT_DIR"

# Run the Flask app
run_app