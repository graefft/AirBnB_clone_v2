#!/usr/bin/python3
'''Starts Flask web application, displays cities by state
'''
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states/', strict_slashes=False, defaults={'state_id': None})
@app.route('/states/<state_id>')
def states(state_id):
    '''lists all states in db'''
    states = storage.all(State)
    if state_id:
        state_id = "{}.{}".format('State', state_id)
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def clean_up(self):
    '''closes storage'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
