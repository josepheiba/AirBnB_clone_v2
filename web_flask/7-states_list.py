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
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def closer(exception):
    """
    Closes the storage on teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
