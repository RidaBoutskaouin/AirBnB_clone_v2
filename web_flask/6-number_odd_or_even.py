#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """Hello Flask"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """HBNB"""
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    """C"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python")
@app.route("/python/<text>")
def python(text="is cool"):
    """Python"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """Number"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """Number template"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """Number odd or even"""
    if n % 2 == 0:
        oe = "even"
    else:
        oe = "odd"
    return render_template("6-number_odd_or_even.html", n=n, oe=oe)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
