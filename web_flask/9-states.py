#!/usr/bin/python3
"""This module give the dates of the list the states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('states')
def states():
    """"""
    list_states = storage.all(State)
    return render_template('9-states.html', list_states=list_states,\
        mode="list_states")


@app.route('states/<id>')
def states_id(id):
    """This method return states and cities if exist"""
    list_states = storage.all(State)
    for state in list_states.values():
        if state.id == id:
            return render_template('9-states.html', list_states=list_states,\
                mode="state_id")
    return render_template('9-states.html', list_states=list_states,\
        mode="none")


@app.teardown_appcontext
def teardown_db(exception):
    """Close current session"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
