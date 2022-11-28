#!/usr/bin/python3 __init__.py
"""flask app"""

import Flask from flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    """Retunr hello"""
    return "<p>Hello HBNB!</p>"
