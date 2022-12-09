#!/usr/bin/python3
"""
This module give the dates of the list the states
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ This method return all states in the database"""
    list_states = storage.all(State)
    return render_template('7-states_list.html', list_states=list_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Close current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)