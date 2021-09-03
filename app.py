import flask
from flask import request

import pandas as pd

data = pd.read_csv('data.csv', names=['name', 'id', 'thing']).set_index('id')

app = flask.Flask(__name__)

@app.route('/', methods=["get"])
def home():
    return "Hello"


@app.route('/blog', methods=["get"])
def messages():
    return ["messages", "more messages"]
