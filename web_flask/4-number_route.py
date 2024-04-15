#!/usr/bin/python3
'''first task'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def just_HBNB():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    text_with_spaces = text.replace('_', ' ')
    return "C {}".format(text_with_spaces)


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    text_with_spaces = text.replace('_', ' ')
    return "Python {}".format(text_with_spaces)

@app.route("/number/<int:n>", strict_slashes=False)
def display_num(n):
    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run()
