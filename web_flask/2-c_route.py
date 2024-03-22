#!/usr/bin/python3
"""
In this module we intrduce escaping in flask
"""


from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """ Returns an html page that displays hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ Returns an html page that displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """ Returns "C" followed by the value of the text variable """
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
