#!/usr/bin/env python
import json
import requests
requests.packages.urllib3.disable_warnings()

url = 'http://zcash.deltapool.net/api/stats'
stats = requests.get(url)
stats_json = json.loads(stats.text)

pending_blocks = stats_json['pools']['zcash']['blocks']['pending']

if pending_blocks != 0:
    print('delta has a pending block!')
else:
    #print('no pending blocks')

