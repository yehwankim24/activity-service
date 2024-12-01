#!/bin/bash

pkill -f ActicityService.py

rm -rf $HOME/ActivityService
mkdir $HOME/ActivityService
cd $HOME/ActivityService

mkdir Activities
curl https://raw.githubusercontent.com/yehwankim24/activity-service/refs/heads/main/requirements.txt > requirements.txt
curl https://raw.githubusercontent.com/yehwankim24/activity-service/refs/heads/main/TestActivityService.sh > TestActivityService.sh
curl https://raw.githubusercontent.com/yehwankim24/activity-service/refs/heads/main/TestActivityService.py > TestActivityService.py
curl https://raw.githubusercontent.com/yehwankim24/activity-service/refs/heads/main/ActivityService.sh > ActivityService.sh
curl https://raw.githubusercontent.com/yehwankim24/activity-service/refs/heads/main/ActivityService.py > ActivityService.py

chmod 777 Activities
chmod 777 requirements.txt
chmod 777 TestActivityService.sh
chmod 777 TestActivityService.py
chmod 777 ActivityService.sh
chmod 777 ActivityService.py

$(which pip3) install -r requirements.txt --upgrade
