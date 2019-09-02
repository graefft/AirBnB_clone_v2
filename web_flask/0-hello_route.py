#!/usr/bin/python3
'''Starts Flask web app'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    '''prints Hello HBNB'''
    return 'Hello HBNB!'
app.run(host='0.0.0.0', port=5000)
