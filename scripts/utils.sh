# Load variables from defaults.conf (if present)
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
    local defaults_conf_file="$PROJECT_DIR/defaults.conf"
    local config_conf_file="$PROJECT_DIR/config.conf"
    local conf_files="$(find "$PROJECT_DIR" -type f -name "*.conf" ! -name "defaults.conf" ! -name "config.conf")"

    # Load variables from defaults.conf (if present)
    if [ -f "$defaults_conf_file" ]; then
        load_conf_file "$defaults_conf_file"
    fi

    # Load variables from config.conf (if present)
    if [ -f "$config_conf_file" ]; then
        load_conf_file "$config_conf_file"
    fi

    # Load variables from all other .conf files
    for conf_file in $conf_files; do
        load_conf_file "$conf_file"
    done
}

run_app() {
    # Set FLASK_APP environment variable if it is not already set
    if [ -z "$FLASK_APP" ]; then
        export FLASK_APP="run.py"
    fi

    # Install PostgreSQL and Python packages
    $PROJECT_DIR/scripts/postgresql.sh
    $PROJECT_DIR/scripts/pip.sh

    # Upgrade database
    if [ -d "$PROJECT_DIR/migrations" ]; then
        echo "The migrations directory exists in $PROJECT_DIR"
    else
        echo "The migrations directory does not exist in $PROJECT_DIR"
        flask db init
    fi
    
    flask db migrate
    flask db upgrade

    # Run the Flask app using either Gunicorn or the Flask development server
    if [ "$APP_ENV" = "production" ]; then
        gunicorn -w 4 run:app
    else
        flask run -h 0.0.0.0 --reload
    fi
}