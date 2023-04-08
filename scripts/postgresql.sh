#!/bin/bash

# Check if DATABASE_TYPE is set to postgresql
if [[ "$DATABASE_TYPE" != "postgres" && "$DATABASE_TYPE" != "postgresql" ]]; then
  exit 1
fi

# Check if PostgreSQL is installed
if ! command -v psql >/dev/null 2>&1 ; then
  # Install PostgreSQL
  echo "PostgreSQL is not installed, installing now..."
  sudo apt-get update
  sudo apt-get install postgresql postgresql-contrib -y 
fi

# Check if postgres superuser with the same name as the logged in user exists
if [ -z "$(psql -qAt -c "SELECT usename FROM pg_user WHERE usename = '$USER'" postgres)" ]; then
echo "Creating postgres superuser $USER..."
sudo -u postgres createuser --superuser "$USER"
fi

# Check if the databases exist, create them if they don't
for db_name in "$DATABASE_NAME" "$DATABASE_NAME_DEVELOPMENT" "$DATABASE_NAME_TESTING"; do
if [ -z "$(psql -qAt -c "SELECT datname FROM pg_database WHERE datname = '$db_name'" postgres)" ]; then
    echo "Creating database $db_name..."
    if [[ -z "$DB_USER" ]] || [[ -z "$DB_PASSWORD" ]]; then
    createdb -O "$USER" "$db_name"
    else
    createdb -U "$DB_USER" -W "$DB_PASSWORD" -O "$DB_USER" "$db_name"
    fi
fi
done