#!/bin/bash

# Check if PIP is installed
if ! command -v pip >/dev/null 2>&1 ; then
  echo "PIP is not installed, installing now..."
  sudo apt-get update
  sudo apt-get install python-pip -y
fi

# Find all requirements.txt files and install the dependencies
find $PROJECT_DIR -name 'requirements.txt' -type f -print0 | while IFS= read -r -d '' file; do
    echo "Verifying dependencies for $file"
    pip install -r "$file" > /dev/null 2>&1
done