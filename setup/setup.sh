#!/usr/bin/env bash
# this is only for c/p. Not tested for script run

sudo apt-get -q update
sudo apt-get -y -q install python-dev build-essential python-pip

sudo apt-get -y install nginx-full

# install uwsgi
sudo apt-get -y install python-dev build-essential python-pip uwsgi uwsgi-plugin-python
# rm default conf
sudo rm /etc/nginx/sites-enabled/default

sudo cp /var/www/projectc/projectc /etc/nginx/sites-available/projectc
sudo ln -s /etc/nginx/sites-available/projectc /etc/nginx/sites-enabled/projectc

sudo cp /var/www/projectc/projectc.ini /etc/uwsgi/apps-available/projectc.ini
sudo ln -s /etc/uwsgi/apps-available/projectc.ini /etc/uwsgi/apps-enabled/projectc.ini

sudo pip install virtualenv
sudo virtualenv /var/www/env
source /var/www/env/bin/activate
pip install -r /var/www/projectc/requirements.txt

sudo service nginx restart
sudo service uwsgi restart
