#!/usr/bin/python
import requests
import json
import time
import os

while True:

 r = requests.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&id=CHANNEL_ID&key=YOUTUBE_DATA_API_V3')
 j = r.json()

 subs = j['items'][0]['statistics']['subscriberCount']
 views = j['items'][0]['statistics']['viewCount']

#while True:

 time.sleep(60)
 os.system('clear')
 print "YOUR CHANNEL Channel Stats:"
 print "Total number of subscribers: %s" % (subs)
 print "Total number of views: %s" % (views)

