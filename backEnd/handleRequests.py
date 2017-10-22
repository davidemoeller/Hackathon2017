from __future__ import print_function

import os
import json
import socket
import requests
import datetime
import uuid
import glob

import pdb

from flask import Flask
from flask import request
from flask import jsonify

URL = 'http://192.241.193.9:3000'

app = Flask(__name__)

@app.route('/getAllData')
def getAll():

    masterArray = []
    subArray = []

    files = glob.glob('/users/*')

    for file in files:
        with open(file, 'r+') as fin:
                for line in fin:
                    json_doc = json.loads(line)
                    subArray.append(json_doc)
        masterArray.append(subArray)

    message = jsonify(list=masterArray)

    resp = app.make_response(message)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/getPersonData', methods=['POST'])
def getPerson():

    obj = request.form.to_dict()

    personData = []

    with open('users/' + obj['name'] + '.jsonl', 'r+') as fin:
        for line in fin:
            json_doc = json.loads(line)
            personData.append(json_doc)

    message = jsonify(list=personData)

    resp = app.make_response(message)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/getEventData', methods=['POST'])
def getEvent():

    obj = request.form.to_dict()

    with open('event/events.jsonl', 'r+') as fin:
        for line in fin:
            json_doc = json.loads(line)
            if obj['uuid'] == json['uuid']:
                break

    message = str(json_doc)

    resp = app.make_response(message)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/login', methods=['POST'])
def login():

    obj = request.form.to_dict()

    eventList = []

    with open('users/' + obj['name'] + '.jsonl', 'r+') as fin:
        for line in fin:
            json_doc = json.loads(line)
            eventList.append(json_doc['event'])

    print(eventList)

    responseDict = {}
    responseList = []

    if len(eventList) > 0:
        with open('event/events.jsonl', 'r+') as fin:
            for line in fin:
                json_doc = json.loads(line)
                for event in eventList:
                    if event == json_doc['uuid']:
                        responseDict['uuid'] = event
                        loc = json_doc['event']['location'].split(' ')
                        responseDict['p1'] = loc[0]
                        responseDict['p2'] = loc[1]
                        responseDict['p3'] = loc[2]
                        responseDict['p4'] = loc[3]
                        responseList.append(responseDict)
                responseDict = {}


    print(responseList)
    message = jsonify(list=responseList)

    resp = app.make_response(message)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/checkIn', methods=['POST'])
def checkIn(obj):

    currentTime = datetime.datetime.now();

    with open('event/events.jsonl', 'r+') as fin:
        for line in fin:
            json_doc = json.loads(line)
            if json_doc['uuid'] == obj['uid']:
                x = json_doc['event']['openWindow']
                compareTime = datetime.datetime.strptime(
                    x.split('-')[1] + '/' + x.split('-')[2].split('T')[0] + '/' + x.split('-')[0] + ' ' +
                    x.split('-')[2].split('T')[1], "%m/%d/%Y %H:%M")
                x = json_doc['event']['closeWindow']
                endTime = datetime.datetime.strptime(
                    x.split('-')[1] + '/' + x.split('-')[2].split('T')[0] + '/' + x.split('-')[0] + ' ' +
                    x.split('-')[2].split('T')[1], "%m/%d/%Y %H:%M")
                break

    if currentTime < compareTime:
        message = 'Not open yet'

    elif currentTime > compareTime and currenTime < endTime:
        message = obj['name'] + 'has checked in!'
        fin = open('event/events.jsonl', 'r+')
        lines = fin.readlines()
        fin.close()
        fout = open('event/events.jsonl', 'w+')
        for line in lines:
            json_doc = eval(line)
            if json_doc['uuid'] == obj['uid']:
                json_doc['attendList'].append(obj['name'])
                fout.write(str(json_doc))
            else:
                fout.write(str(json_doc))
        fout.close()

    else:
        message = obj['name'] + 'missed the time window'
        fin = open('event/events.jsonl', 'r+')
        lines = fin.readlines()
        fin.close()
        fout = open('event/events.jsonl', 'w+')
        for line in lines:
            json_doc = eval(line)
            if json_doc['uuid'] == obj['uid']:
                json_doc['absentList'].append(obj['name'])
                fout.write(str(json_doc))
            else:
                fout.write(str(json_doc))
        fout.close()


    resp = app.make_response(message)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

def createUserEvent(obj, uid):

    doc = {}

    for names in obj:
        with open('users/' + names + '.jsonl', 'a') as fout:
            doc['event'] = uid
            fout.write(json.dumps(doc) + '\n')

    return

@app.route('/createEvent', methods=['POST'])
def createEvent():

    content = request.form.to_dict()
    print(content)

    location = content['loc']
    openTime = content['openTime']
    closeTime = content['closeTime']
    description = content['description']
    invite = eval(content['invite'])

    uid = str(uuid.uuid4()).split('-')[0]

    pdb.set_trace()
    createUserEvent(invite, uid)

    doc = {'uuid': uid, 'event':{'attendList': [], 'absentList': [], 'location': location, 'openWindow': openTime, 'closeWindow': closeTime, 'description': description}}

    with open('event/events.jsonl', 'a') as fout:
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
