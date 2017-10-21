from __future__ import print_function

import os
import json
import socket
import requests
import datetime

import pdb

from flask import Flask
from flask import request
from flask import jsonify

URL = 'http://192.241.193.9:3000'

app = Flask(__name__)

def createDocument(obj):
    return
def checkIn(obj):
    return
def createEvent(obj):

    return

@app.route('/getInfo', methods=['POST'])
def main():

    message = None

    if request.form['data'] == 'test':
        message = 'Got it!'
    elif request.form['check-in'] == True:
        message = "You have been checked in!"

    resp = app.make_response(message)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if (__name__ == "__main__"):
    app.run(host='192.241.193.9', port=3001)
