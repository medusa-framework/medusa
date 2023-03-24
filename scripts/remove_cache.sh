#!/bin/bash

# Remove all __pycache__ directories and *.pyc files in all subdirectories
find $PROJECT_DIR -type d -name "__pycache__" -print0 | xargs -0 rm -rf
find $PROJECT_DIR -type f -name "*.pyc" -print0 | xargs -0 rm -f

echo "Cleared Python cache files."