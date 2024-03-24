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


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Returns an html page that displays hello HBNB! """
    all_states = storage.all(State).values()
    states = sorted(all_states, key=lambda x: x.name)
    return render_template("7-states_list.html",
                           states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_in_states():
    """ Returns an html page that displays hello HBNB! """
    all_states = storage.all(State).values()
    states = sorted(all_states, key=lambda x: x.name)
    states_and_cities = [(
        x,
        sorted(x.cities, key=lambda y: y.name)
        ) for x in all_states]
    return render_template("8-cities_by_states.html",
                           states=states_and_cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
