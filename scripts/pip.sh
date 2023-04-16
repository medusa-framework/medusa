#!/bin/bash

pip_init() {
    # Check if PIP is installed
    if ! command -v pip >/dev/null 2>&1 ; then
        echo "PIP is not installed, installing now..."
        sudo apt-get update
        sudo apt-get install python-pip -y
    fi

    # Find all requirements.txt files and install the dependencies
    for file in $(find "$PROJECT_DIR" -name 'requirements.txt'); do
        echo "Verifying dependencies for $file"
        pip install -r "$file" > /tmp/pip_output
        if grep -q 'Successfully installed' /tmp/pip_output; then
            cat /tmp/pip_output
        fi
        rm /tmp/pip_output
    done
}