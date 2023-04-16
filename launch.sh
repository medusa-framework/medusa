#!/bin/bash

# Set PROJECT_DIR environment variable to current directory
export PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# ENVIRONMENT
source "$PROJECT_DIR/scripts/load_confs.sh"
load_conf_files
echo "Environment variables loaded from .conf files in $PROJECT_DIR"
if [[ -z "${FLASK_APP}" ]]; then
  export FLASK_APP="${PROJECT_DIR}/app.py"
fi
export SECRET_KEY=$(openssl rand -hex 16)
source "$PROJECT_DIR/scripts/pip.sh"
pip_init

# DATABSE
source "$PROJECT_DIR/scripts/postgresql.sh"
postgresql
if [ -d "$PROJECT_DIR/migrations" ]; then
    echo "The migrations directory exists in $PROJECT_DIR"
else
    echo "The migrations directory does not exist in $PROJECT_DIR"
    flask db init
fi
# source "$PROJECT_DIR/scripts/mysql.sh"
# mysql
flask db migrate
flask db upgrade

# APPLICATION
if [ "$APP_ENV" = "production" ]; then
    gunicorn -w 4 app:app
else
    flask run -h 0.0.0.0 --reload
fi