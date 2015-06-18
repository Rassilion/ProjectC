# Test server
Setup: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04

Link: http://107.191.111.139/

# Deploy script
githup base repo at ~/repo/ProjectC.git
work dir at ~/deploy
uwsgi an nginx server sym link ~/Websitesi

git post-recive

```
#!/usr/bin/env ruby
# post-receive

# 1. Read STDIN (Format: "from_commit to_commit branch_name")
from, to, branch = ARGF.read.split " "

# 2. Only deploy if master branch was pushed
if (branch =~ /master$/) == nil
    puts "Received branch #{branch}, not deploying."
    exit
end

# 3. Copy files to deploy directory
deploy_to_dir = File.expand_path('~/deploy')
`GIT_WORK_TREE="#{deploy_to_dir}" git checkout -f master`
puts "DEPLOY: master(#{to}) copied to '#{deploy_to_dir}'"
```

shell scripts to deoploy

```
#!/bin/bash

# get from git
cd /home/deniz/repo/ProjectC.git
git fetch origin

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