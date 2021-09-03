#!/usr/bin/env python3
import flask
from flask import Flask
from flask import request
app = Flask(__name__)

import pandas as pd

data = pd.read_csv('data.csv', names=['name', 'id', 'thing']).set_index('id')

app = flask.Flask(__name__)

@app.route('/', methods=["get"])
def index():
    return "Hello"


@app.route('/blog', methods=["get"])
def messages():
    return "Message Text"

if __name__=="__main__":
    app.run()
