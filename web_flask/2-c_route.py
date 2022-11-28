#!/usr/bin/python3
"""flask app"""

from flask import Flask
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
def hello_flask_hbnb():
    """Retunr hbnb"""
    return "C {escape(text)"


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
