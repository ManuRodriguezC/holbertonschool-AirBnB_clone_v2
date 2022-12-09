#!/usr/bin/python3
"""Conecting the flask with dbstorage, and return list states"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """This method display list of the states"""
    list_states = storage.all(State)
    return render_template('9-states.html', list_states=list_states,\
        mode="state")


@app.route('states/<id>')
def states_id(id):
    """This method display states for the id"""
    list_states = storage.all(State)
    for state in list_states.value():
        if state.id == id:
            return render_template('9-state.html', list_states,\
                mode="state_id")
    return render_template('9-states.html', list_states=list_states,\
        mode="none")


@app.teardown_appcontext
def teardown(exception):
    """This method close the curren session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
