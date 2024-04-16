#!/usr/bin/python3
'''first task'''
from flask import Flask
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)

all_states = storage.all(State)

@app.route("/", strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"


@app.route("/states_list", strict_slashes=False)
def list_of_cities(all_states):
    return render_template('7-states_list.html', all_states=all_states)


@app.teardown_appcontext
def remove_session():
    storage.close()


if __name__ == "__main__":
    app.run()
