# Test server
Setup: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04

Link: http://107.191.111.139/

# Deploy script
githup base repo at ~/repo/ProjectC.git
work dir at ~/deploy
uwsgi an nginx server sym link ~/Websitesi

shell scripts to deoploy

```
#!/bin/bash

# get from git
cd /home/deniz/repo/ProjectC.git
git fetch origin master:master
GIT_WORK_TREE="/home/deniz/deploy" git checkout -f master

source /home/deniz/.env/bin/activate

pip install -r /home/deniz/deploy/Website/requirements.txt

deactivate

echo "`sudo bash /home/deniz/restart.sh`"
```

```
#!/bin/bash
#restart servers
/etc/init.d/nginx stop
/etc/init.d/nginx start
stop website
start website

```