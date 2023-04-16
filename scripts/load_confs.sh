#!/bin/bash

load_conf_file() {
    local conf_file="$1"

    while IFS="=" read -r name value; do
        # Ignore lines starting with # and empty lines
        if [[ $name = \#* || -z $name ]]; then
            continue
        fi

        # Remove leading/trailing whitespace
        name="$(echo "$name" | { read x; echo "$x"; })"
        value="$(echo "$value" | { read x; echo "$x"; })"

        # Remove any enclosing quotes (if present)
        value="${value%\"}"
        value="${value#\"}"

        # Set the variable in the environment
        export "$name"="$value"
    done < <(grep -v '^#\|^[[:space:]]*$' "$conf_file")
}

load_conf_files() {
    local defaults_conf_file="$PROJECT_DIR/config/medusa.conf"
    local conf_files="$(find "$PROJECT_DIR" -type f -name "*.conf" ! -name "medusa.conf")"

    # Load variables from defaults.conf (if present)
    if [ -f "$defaults_conf_file" ]; then
        load_conf_file "$defaults_conf_file"
    fi

    # Load variables from all other .conf files
    for conf_file in $conf_files; do
        load_conf_file "$conf_file"
    done
}