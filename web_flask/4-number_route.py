#!/usr/bin/python3
"""flask app"""

from flask import Flask
from markupsafe import escape
from flask import url_for
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Retunr hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_flask_hbnb():
    """Retunr hbnb"""
    return 'HBNB'


@app.route('/c/<text>')
def hello_flask_text(text):
    """Retunr hbnb"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def hello_flask_text2(text="is_cool"):
    """Retunr hbnb"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def hello_flask_number(n=None):
    """Retunr number"""
    if int: n

    return str(n) + ' is a number'


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
