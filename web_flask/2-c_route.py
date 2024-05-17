#!/usr/bin/python3
"""
hello Flask!
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    hello HBNB
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def widlcard(text):
    """
    Widlcard usage
    """
    return f"C {text}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
