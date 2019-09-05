#!/usr/bin/python3
'''Starts Flask web application, uses storage for
   fetching data from storage engine
'''
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)

@app.teardown_appcontext
def clean_up(self):
    '''closes storage'''
    storage.close()

@app.route('/states_list', strict_slashes=False)
def state_list():
    '''lists all states in db'''
    state_dict = storage.all(State)
    return render_template('7-states_list.html', state_dict=state_dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
