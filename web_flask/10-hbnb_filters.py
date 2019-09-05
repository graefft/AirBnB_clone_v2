#!/usr/bin/python3
'''Starts Flask web application, displays cities by state
'''
from flask import Flask, render_template
from models import storage, State, Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    '''lists all states in db'''
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def clean_up(self):
    '''closes storage'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
