#!/usr/bin/python3
'''first task'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

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


@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template('5-number.html', num=n)


@app.route("/number_odd_or_even/<int:n>")
def even_or_odd(n):
    return render_template('6-number_odd_or_even.html', num=n)
 
@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def html_fetch_states():
    state_objs = [s for s in storage.all("State").values()]
    state_objs = sorted(state_objs, key=lambda x: x.name)
    return render_template('7-states_list.html',
                           all_states=state_objs)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    state_objs = [s for s in storage.all("State").values()]
    state_objs = sorted(state_objs, key=lambda x: x.name)
    return render_template('8-cities_by_states.html',
                           all_states=state_objs)

@app.route('/states/<id>', strict_slashes=False)
def fetch_state_by_id(id):
    state = storage.get("State", id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', state=None)


@app.teardown_appcontext
def remove_session(self):
    storage.close()


if __name__ == "__main__":
    app.run()
