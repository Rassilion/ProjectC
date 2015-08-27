#!/usr/bin/env bash

sudo apt-get -q update
sudo apt-get -y -q install python-dev build-essential python-pip

sudo apt-get -y install nginx-full

# install uwsgi
sudo apt-get -y install python-dev build-essential python-pip uwsgi uwsgi-plugin-python

sudo rm /etc/nginx/sites-enabled/default

sudo cp /var/www/projectc/setup/projectc /etc/nginx/sites-available/projectc
sudo ln -s /etc/nginx/sites-available/projectc /etc/nginx/sites-enabled/projectc

sudo cp /var/www/projectc/setup/projectc.ini /etc/uwsgi/apps-available/projectc.ini
sudo ln -s /etc/uwsgi/apps-available/projectc.ini /etc/uwsgi/apps-enabled/projectc.ini


sudo service nginx restart
sudo service uwsgi restart


echo >&2 "===CUSTOM-MSG=== Setup THE DATABASE"
# installs postgresql database and creates "vagrant" superuser with password "somepass".
sudo apt-get -y install postgresql postgresql-client libpq-dev

echo >&2 "===CUSTOM-MSG=== Create role and login"
sudo su postgres -c "psql -c \"CREATE ROLE vagrant SUPERUSER LOGIN PASSWORD 'superpass'\" "
# create database 'mynewdb' for role (superuser) vagrant

#echo >&2 "===CUSTOM-MSG=== Create db"
sudo su postgres -c "createdb -E UTF8 -T template0 --locale=en_US.utf8 -O vagrant website"

#Replace .profile with .bashrc if required
source ~/.bashrc
if [ -z "$DATABASE_URL" ]; then # only checks if VAR is set, regardless of its value
    echo "export DATABASE_URL=postgresql://vagrant:superpass@localhost:5432/website" >> ~/.bashrc
fi
if [ -z "$PYTHONPATH" ]; then # only checks if VAR is set, regardless of its value
    echo "export PYTHONPATH="/var/www/projectc/"" >> ~/.bashrc
fi
echo"DATABASE_URL=postgresql://vagrant:superpass@localhost:5432/website" >> /etc/environment

# enable the db to listen from the host through tcp
sudo su postgres -c "printf \"\n\n# === CUSTOM VAGRANT SETTINGS === \n \" >> /etc/postgresql/*/main/postgresql.conf"
sudo su postgres -c "echo \" listen_addresses = '*' \" >> /etc/postgresql/*/main/postgresql.conf"
sudo su postgres -c "printf \"\n\n# === CUSTOM VAGRANT SETTINGS === \n \" >> /etc/postgresql/*/main/pg_hba.conf"
sudo su postgres -c "echo \" host    all             all             10.0.2.2/24             md5 \" >> /etc/postgresql/*/main/pg_hba.conf"

#restart
sudo /etc/init.d/postgresql restart

pip install -r /var/www/projectc/requirements.txt
