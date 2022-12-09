#!/usr/bin/python3
"""This module give the dates of the list the states"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.route('cities_by_states', strict_slashes=True)
def cities_by_state():
    """This methos return od the cities and states in db"""
    list_state = storage.all(State)
    return render_template('8-cities_by_states.html', list_state=list_state)


@app.teardown_appcontext
def teardown(exception):
    """This method close current session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
