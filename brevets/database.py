import json

import arrow
import requests
import flask

from flask_brevets import CONFIG

MGFMT = 'YYYY-MM-DDTHH:mm:ss'
api = f"{CONFIG['APILOC']}"

def insert_brevet(worksheet):
    ws = {
        'timestamp': arrow.utcnow().format(MGFMT),
        'start_time': worksheet['start_time'],
        'worksheet': worksheet['worksheet'],
        'brevet_dist': worksheet['brevet_dist'],
    }
    requests.post(f"{api}/brevets", data=json.dumps(ws))

def latest_brevet():
    brevets = requests.get(f"{api}/brevets").json()
    latest = None
    if len(brevets) > 0:
        latest = brevets[-1]
    return latest



