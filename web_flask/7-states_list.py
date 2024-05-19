#!/usr/bin/python3
"""
hello Flask!
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_route():
    """
    7 route states
    """
    states = storage.all('State')
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def closer(exception):
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
