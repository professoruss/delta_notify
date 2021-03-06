#!/usr/bin/env python
import json
import os
import requests
import sys
requests.packages.urllib3.disable_warnings()
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--coin", action="store", type="string", dest="coin",
                  help="coin type (zcash, zclassic, hush, etc)(must match api output)", metavar="COIN")
parser.add_option("-u", "--url", action="store", type="string", dest="url",
                  help="url of pool API", metavar="URL")
parser.add_option("-n", "--name", action="store", type="string", dest="name",
                  help="name of pool", metavar="NAME")
parser.add_option("-o", "--output", action="store", type="string", dest="output",
                  help="output to pushover(optional)", default="cli", metavar="OUTPUT")
(options, args) = parser.parse_args()

url = options.url
try: stats = requests.get(url, timeout=10)
except requests.exceptions.RequestException as e:
    sys.exit(1)
else:
    stats_json = json.loads(stats.text)
    pending_blocks = stats_json['pools'][options.coin]['blocks']['pending']

    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    old_pending = {}
    if not os.path.exists('status'):
            os.makedirs('status')
    if os.path.exists('status/' + options.name + '_' + options.coin + '_' + options.output + '.json'):
        old_pending = json.loads(open('status/' + options.name + '_' + options.coin + '_' + options.output + '.json').read())

    new_pending = str(pending_blocks)

    if pending_blocks > old_pending:
        if options.output == 'pushover':
            pushover_url = 'https://api.pushover.net/1/messages.json'
            pushover_json = json.loads(open('pushover.json').read())

            headers = {
                'Content-Type'   : 'application/x-www-form-urlencoded',
                'Content-Length' : '180'
            }

            pushover_data = 'token=' + pushover_json['token'] + '&user=' + pushover_json['user'] + '&title=' + options.name + ' Block&message=' + options.name + '%20pool%20has%20a%20new%20pending%20' + options.coin + '%20block! (' + new_pending + ')'
            push_to_pushover = requests.post(pushover_url, data=pushover_data)
            push_to_pushover.raw
            #print(push_to_pushover.status_code)
        else:
            print( options.name + 'pool has a new pending ' + options.coin + ' block! (' + new_pending + ')')

    with open('status/' + options.name + '_' + options.coin + '_' + options.output + '.json', 'w') as outfile:
        json.dump(pending_blocks, outfile)
    #else:
    #    print('no pending blocks')
