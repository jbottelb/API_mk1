#!/usr/bin/env python3
import flask
from flask import Flask
from flask import request
import json
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
'''
index, used mostly to test a connection to the API
'''
@app.route('/', methods=["get"])
def index():
    return "Hello, this is PhyAPI. My documentation will be up soon. "

'''
Sends a messages and stores it in a tsv file (people may want to use commas)
'''
@app.route('/sendmessage', methods=["POST"])
def send_message():
    try:
        message = request.get_json()
        name = message["name"]
        message = message["message"]
        if name and message:
            with open("messages.tsv", "a") as f:
                f.write(name + "%%%!!!%%%" + message + "\n")
        return "Sucess"
    except Exception as e:
        print(e)
        return "Failure"

'''
Sends all the messages stored in the tsv, converts to json first
Do the heavy lifting on the backend
'''
@app.route('/messages', methods=["get"])
def messages():
    # may have invented the "token seperated value" file type for this
    data = []
    with open("messages.tsv") as f:
        for line in f:
            name, message = line.strip().split("%%%!!!%%%")
            data.append({"name":name, "message":message})
    return json.dumps(data)

'''
Here for localost testing
'''
if __name__=="__main__":
    app.run()
