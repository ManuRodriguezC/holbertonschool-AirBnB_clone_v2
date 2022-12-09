#!/usr/bin/python3
"""This module give the dates of the list the states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_state():
    """ This method return all states in the database"""
    list_state = storage.all(State)
    return render_template('8-cities_by_states.html', list_state=list_state)


@app.teardown_appcontext
def teardown_db(exception):
    """Close current session"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
