#!/usr/bin/python3 __init__.py
"""flask app"""

import Flask from flask
app = Flask(__name__)


@app.route("/")
def hello_flask():
    """Retunr hello"""
    return 'Hello HBNB!'
