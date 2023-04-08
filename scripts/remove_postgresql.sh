#!/bin/bash

# Stop PostgreSQL service
sudo service postgresql stop

# Drop all databases
sudo -u postgres psql -c "SELECT 'DROP DATABASE IF EXISTS ' || datname || ';' FROM pg_database WHERE datistemplate = false;" | sudo -u postgres psql

# Remove PostgreSQL packages
sudo apt-get --purge -y remove postgresql\*
sudo apt-get -y autoremove

# Remove PostgreSQL data directories and configuration files
sudo rm -rf /etc/postgresql/
sudo rm -rf /etc/postgresql-common/
sudo rm -rf /var/lib/postgresql/
sudo userdel -r postgres
sudo groupdel postgres
