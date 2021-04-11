import flask
from flask import request

import pandas as pd

data = pd.read_csv('data.csv', names=['name', 'id', 'thing']).set_index('id')

app = flask.Flask(__name__)

@app.route('/', methods=["get"])
def home():
    return "Hello"
    '''try:
        key = int(request.args['id'])

        return "I thought of an example and it was a " + key['thing']
    except KeyError:
        return "Bad"'''
