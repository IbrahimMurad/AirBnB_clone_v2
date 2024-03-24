#!/usr/bin/python3
"""
starts a Flask web application and lists all states
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """removes the current SQLAlchemy Session after each request"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ Returns an html page that displays hello HBNB! """
    states = storage.all(State).values()
    return render_template("9-states.html",
                           states=states, id=None)


@app.route("/states/<id>", strict_slashes=False)
def cities_in_state(id):
    """ Returns an html page that displays hello HBNB! """
    states = storage.all(State).values()
    return render_template("9-states.html",
                           states=states, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
