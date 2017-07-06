#!/usr/bin/env python
import json
import requests
requests.packages.urllib3.disable_warnings()
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--output", action="store", type="string", dest="output",
                  help="output to pushover", metavar="OUTPUT")
(options, args) = parser.parse_args()

url = 'http://zcash.deltapool.net/api/stats'
stats = requests.get(url)
stats_json = json.loads(stats.text)
pending_blocks = stats_json['pools']['zcash']['blocks']['pending']


if pending_blocks != 0:
    if options.output == 'pushover':
        pushover_url = 'https://api.pushover.net/1/messages.json'
        pushover_json = json.loads(open('pushover.json').read())

        headers = {
            'Content-Type'   : 'application/x-www-form-urlencoded',
            'Content-Length' : '180'
        }
       
        pushover_data = 'token=' + pushover_json['token'] + '&user=' + pushover_json['user'] + '&title=DeltaBlock&message=delta%20pool%20has%20a%20pending%20ZEC%20block!'
        push_to_pushover = requests.post(pushover_url, data=pushover_data)
        push_to_pushover.raw
        #print(push_to_pushover.status_code)
    else:
        print('delta pool has a pending ZEC block!')
#else:
#    print('no pending blocks')

