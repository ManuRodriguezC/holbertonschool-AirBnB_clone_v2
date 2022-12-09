#!/usr/bin/python3
"""Conecting the flask with dbstorage, and return list states"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def state_list():
    """This method display list of the states"""
    states = storage.all(State)
    return render_template("9-states.html", states=states, mode="state")


@app.route("/states/<id>")
def states_id(id):
    """This method display states for the id"""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state,
                                   mode="state_id")
    return render_template("9-states.html", state=state, mode="none")


@app.teardown_appcontext
def teardown(execption):
    """This method close the curren session"""
    return storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
