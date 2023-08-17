#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask
from sys import argv

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    '''First function. Prints on /'''
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Second function. Prints on /hbnb'''
    return "HBNB"

@app.route("c/<text>", strict_slashes=False)
def c(text):
    '''Third function. Prints on /c/anything'''
    return f"C {text.replace('_', ' ')}"

@app.route("/python/<text>", strict_slashes=False)
def pyton(text):
    '''Fourth function. Prints on /python/anything'''
    return f"Python { text.replace('_', ' ')}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
