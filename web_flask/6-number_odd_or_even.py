#!/usr/bin/python3
"""
In this module we intrduce escaping in flask
"""


from flask import Flask, render_template
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """ Returns “Python ”, followed by the value of the text variable """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_number(n):
    """ Returns "n is a number" only if n is an integer """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_in_temp(n):
    """ Returns "n is a number" only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def even_or_odd(n):
    """ Returns a HTML page only if n is an integer """
    odd_even = "odd"
    if n % 2 == 0:
        odd_even = "even"
    return render_template('6-number_odd_or_even.html', n=n, o_or_e=odd_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
