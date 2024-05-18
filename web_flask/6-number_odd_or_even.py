#!/usr/bin/python3
"""
hello Flask!
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    hello HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def widlcard(text):
    """
    Widlcard usage
    """
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def widlcard_two(text):
    """
    Wildcard second
    """
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:num>', strict_slashes=False)
def number_route(num):
    """
    number wildcard
    """
    return f'{num} is a number'


@app.route('/number_template/<int:num>', strict_slashes=False)
def number_trois(num):
    """
    number wildcard
    """
    return render_template('5-number.html', num=num)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def number_even_odd(num):
    """
    number wildcard
    """
    if num % 2 == 0:
        msg = f"{num} is even"
    else:
        msg = f"{num} is odd"

    return render_template('6-number_odd_or_even.html', msg=msg)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
