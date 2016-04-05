#!/usr/bin/python

import os
import requests
import simplejson as json
import subprocess
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACTIVITY_FILE = os.path.join(BASE_DIR, 'activity.json')
PUSH_URL = os.environ["SLACK_PUSH_URL"]
STACKEXCHANGE_API_KEY = os.environ["STACKEXCHANGE_API_KEY"]
print ACTIVITY_FILE

url = 'http://api.stackexchange.com/2.2/questions?pagesize=1&order=desc&sort=creation&tagged=javascript&site=stackoverflow&key=' + \
    STACKEXCHANGE_API_KEY
new_data = requests.get(url).json()
latest_creation_time = new_data['items'][0]['creation_date']

with open(ACTIVITY_FILE) as data_file:
    old_data = json.load(data_file)

last_creation_time = old_data['items'][0]['creation_date']

if latest_creation_time > last_creation_time:

    question = new_data['items'][0]['link']
    curl = 'curl -X POST --data-urlencode '
    p = "'"
    payload = 'payload={"channel": "#stackoverflow", "username": "plone-overflow", "text": "' + \
        'New question: '+question+'", "icon_emoji": ":pencil:"}'
    s = "' "
    test = subprocess.call([curl+p+payload+s+PUSH_URL], shell=True)
    print test

    with open(ACTIVITY_FILE, 'w') as data_file:
        json.dump(new_data, data_file)
