# znomp_notify

Notify via CLI or pushover when a znomp powered pool has a block pending

**Usage:**
```python main.py -c zcash -n Delta -u http://zcash.deltapool.net/api/stats```

**For use with pushover:**
* add user and token to pushover.json (see pushover.json.example)

```python main.py -c zcash -n delta -u http://zcash.deltapool.net/api/stats -o pushover```

**Help:**
```Usage: main.py [options]
Options:
  -h,        --help          show this help message and exit
  -c COIN,   --coin=COIN     coin type (zcash, zclassic, hush, etc)(must match api output)
  -u URL,    --url=URL       url of pool API
  -n NAME,   --name=NAME     name of pool
  -o OUTPUT, --output=OUTPUT output to pushover(optional)```
