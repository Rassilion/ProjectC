#!/usr/bin/env bash

sudo apt-get update
sudo apt-get -y -q install python-dev build-essential python-pip


echo >&2 "===CUSTOM-MSG=== Setup THE DATABASE"
# installs postgresql database and creates "vagrant" superuser with password "somepass".
sudo apt-get -y install postgresql postgresql-client libpq-dev

echo >&2 "===CUSTOM-MSG=== Create role and login"
sudo su postgres -c "psql -c \"CREATE ROLE vagrant SUPERUSER LOGIN PASSWORD 'superpass'\" "
# create database 'mynewdb' for role (superuser) vagrant

#echo >&2 "===CUSTOM-MSG=== Create db"
sudo su postgres -c "createdb -E UTF8 -T template0 --locale=en_US.utf8 -O vagrant projectc"

# enable the db to listen from the host through tcp
sudo su postgres -c "printf \"\n\n# === CUSTOM VAGRANT SETTINGS === \n \" >> /etc/postgresql/*/main/postgresql.conf"
sudo su postgres -c "echo \" listen_addresses = '*' \" >> /etc/postgresql/*/main/postgresql.conf"
sudo su postgres -c "printf \"\n\n# === CUSTOM VAGRANT SETTINGS === \n \" >> /etc/postgresql/*/main/pg_hba.conf"
sudo su postgres -c "echo \" host    all             all             10.0.2.2/24             md5 \" >> /etc/postgresql/*/main/pg_hba.conf"

#restart
sudo /etc/init.d/postgresql restart

pip install -r /vagrant/requirements.txt
