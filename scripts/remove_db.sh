#!/bin/bash


# Remove all *.db files in all subdirectories
find $PROJECT_DIR -type f -name "*.db" -print0 | xargs -0 rm -f

# Remove all directories named "database" and their contents
find $PROJECT_DIR -type d -name "database" -print0 | xargs -0 rm -rf

echo "All *.db files and 'database' directories deleted."