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
    brevets_json = requests.get(f"{api}/brevets").json()
    brevets = sorted(flask.json.loads(brevets_json), reverse=True)
    if len(brevets) > 0:
        return brevets[0]
    else:
        return []

