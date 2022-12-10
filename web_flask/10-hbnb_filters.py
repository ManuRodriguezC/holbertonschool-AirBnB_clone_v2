#!/urs/bin/python3
"""This module start session flask whit db"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('hbnb_filters')
def hbnb():
    """This method created list of amenitis and states"""
    states = storage.all(State)
    ame = storage.all(Amenity)
    return render_template('10-hbnb_filters', states=states, ame=ame)


@app.teardown_appcontext
def teardown(exception):
    """This method close current session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")
