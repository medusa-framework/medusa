#!/bin/bash

mysql(){
    # Check if DATABASE_TYPE is set to mysql
    if [[ "$DATABASE_TYPE" != "mysql+pymysql" && "$DATABASE_TYPE" != "mysql" ]]; then
    exit 1
    fi

    # Check if MySQL is installed
    if ! dpkg -s mysql-server >/dev/null 2>&1 ; then
    # Install MySQL server and client
    echo "MySQL is not installed, installing now..."
    sudo apt-get update
    sudo apt-get install mysql-server -y
    sudo apt-get install mysql-client -y

    # Check if MYSQL_ROOT_PASSWORD environment variable is set
    if [ -z "$MYSQL_ROOT_PASSWORD" ]; then
        echo "MYSQL_ROOT_PASSWORD environment variable not set. Please set MYSQL_ROOT_PASSWORD."
        exit 1
    fi

    # Set root password for MySQL
    sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '$MYSQL_ROOT_PASSWORD'; FLUSH PRIVILEGES;"
    
    # Create new user and grant privileges
    sudo mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "CREATE USER '$USER'@'localhost' IDENTIFIED WITH mysql_native_password BY '$USER_PASSWORD'; GRANT ALL PRIVILEGES ON *.* TO '$USER'@'localhost' WITH GRANT OPTION; FLUSH PRIVILEGES;"
    else
    echo "MySQL is already installed."
    fi

    for db_name in "$DATABASE_NAME" "$DATABASE_NAME_DEVELOPMENT" "$DATABASE_NAME_TESTING"; do
    if ! mysql -e "use $db_name" >/dev/null 2>&1 ; then
        echo "Creating database $db_name..."
        if [ -z "$DB_USER" ] || [ -z "$DB_PASSWORD" ]; then
        mysql -e "CREATE DATABASE $db_name"
        mysql -e "GRANT ALL PRIVILEGES ON $db_name.* TO '$USER'@'localhost'"
        else
        mysql -e "CREATE DATABASE $db_name"
        mysql -e "GRANT ALL PRIVILEGES ON $db_name.* TO '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD'"
        fi
    fi
    done
}