#!/usr/bin/python3
"""
This module give the dates of the list the states and cities
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)

@app.route('cities_by_states')
def cities_by_state():
    """This methos return od the cities and states in db"""
    list_states = storage.all(State)
    list_cities = storage.all(City)
    return render_template('8-cities_by_states.html',\
        list_cities=list_cities, list_states=list_states)


@app.teardown_appcontext
def teardown(exception):
    """This method close current session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
