from __future__ import print_function

import os
import json
import socket
import requests
import datetime
import uuid

import pdb

from flask import Flask
from flask import request
from flask import jsonify

URL = 'http://192.241.193.9:3000'

app = Flask(__name__)

@app.route('/checkIn', methods=['POST'])
def checkIn(obj):

    currentTime = datetime.datetime.now();

    with open('events.jsonl', 'r+') as fin:
        for line in fin:
            json_doc = json.loads(line):
            if json_doc['uuid'] == obj['uid']:
                compareTime = json_doc['event']['openWindow']
                break

    if currentTime < compareTime:
        message = 'Not open yet'

    else:
        message = obj['name'] + 'has checked in!'

    resp = app.make_response(message)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

def createUserEvent(obj, uid):

    doc = {}

    for names in obj:
        with open(names + '.jsonl', 'a') as fout:
            doc['event'] = uid
            fout.write(json.dumps(doc) + '\n')

    return

@app.route('/createEvent', methods=['POST'])
def createEvent():

    content = request.form.to_dict()
    print(content)

    location = content['loc']
    date = datetime.datetime.strptime(content['date'], "%m/%d/%Y %H:%M")
    openTime = content['time']
    description = content['description']
    invite = eval(content['invite'])

    uid = str(uuid.uuid4()).strip('-')[0]

    pdb.set_trace()
    createUserEvent(invite, uid)

    doc = {'uuid': uid, 'event':{'location': location, 'date': date, 'openWindow': openTime, 'description': description}}

    with open('events.jsonl', 'a') as fout:
        fout.write(json.dumps(doc) + '\n')

    message = 'Event successfully created with uuid: ' + uid

    resp = app.make_response(message)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/getInfo', methods=['POST'])
def main():

    message = None

    if request.form.to_dict()['data'] == 'test':
        message = 'Got it!'
    elif request.form.to_dict()['createEvent'] == True:
        message = "You have been checked in!"

    resp = app.make_response(message)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if (__name__ == "__main__"):
    app.run(host='192.241.193.9', port=3001)
