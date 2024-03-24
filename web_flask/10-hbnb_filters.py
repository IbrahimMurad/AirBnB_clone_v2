#!/usr/bin/python3
"""
starts a Flask web application and lists all states
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """removes the current SQLAlchemy Session after each request"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filter():
    """ Returns an html of hbnb clone page """
    return render_template(
        "10-hbnb_filters.html",
        states=storage.all(State).values(),
        amenities=storage.all(Amenity).values()
        )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
