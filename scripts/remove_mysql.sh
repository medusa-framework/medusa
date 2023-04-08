#!/bin/bash

# Stop the MySQL service
sudo systemctl stop mysql

# Remove all MySQL databases
sudo mysql -e "SELECT concat('DROP DATABASE IF EXISTS \`', SCHEMA_NAME, '\`;') FROM information_schema.SCHEMATA WHERE SCHEMA_NAME NOT IN ('mysql','information_schema','performance_schema');" | tail -n +2 | sudo mysql

# Remove MySQL packages
sudo apt-get remove --purge mysql-server mysql-client mysql-common -y
sudo apt-get autoremove -y
sudo apt-get autoclean

# Remove MySQL configuration files
sudo rm -rf /etc/mysql/
sudo rm -rf /var/lib/mysql/
sudo rm -rf /var/log/mysql/
sudo rm -rf /usr/share/mysql/
sudo rm -rf /usr/local/mysql/

# Remove MySQL user and group
sudo deluser --remove-home mysql
sudo delgroup mysql

# Remove MySQL user data and settings
sudo rm -rf /root/.mysql_history
sudo rm -rf /root/.mysql_secret
sudo rm -rf /var/lib/mysql/
sudo rm -rf /var/log/mysql/
sudo rm -rf /var/run/mysqld/

# Remove MySQL from PATH
sudo sed -i '/mysql/d' /etc/environment
sudo sed -i '/mysql/d' /etc/profile

echo "MySQL has been completely removed from your system."
