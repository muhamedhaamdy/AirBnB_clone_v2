#!/usr/bin/python3
'''first task'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run()
