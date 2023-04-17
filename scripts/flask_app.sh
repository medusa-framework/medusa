#!/bin/bash


flask_app() {
    # ENVIRONMENT
    export FLASK_APP="${PROJECT_DIR}/app.py"
    export SECRET_KEY=$(openssl rand -hex 16)
    log "Flask environment variables set"

    # DATABASE
    if [ -d "$PROJECT_DIR/migrations" ]; then
        log "Migrations directory exists"
    else
        log "Migrations directory does not exist. Creating..."
        flask db init
    fi
    log "Migrating database"
    flask db migrate
    log "Upgrading database"
    flask db upgrade
    log "Seeding database"
    flask seed run

    # APPLICATION
    log "Launching framework"
    if [ "$APP_ENV" = "production" ]; then
        gunicorn -w 4 app:app
    else
        flask run -h 0.0.0.0 --reload
    fi
}
