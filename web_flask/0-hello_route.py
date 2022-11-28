#!/usr/bin/python3 __init__.py
"""flask app"""

from Flask import flask
app = Flask(__name__)


@app.route("/")
def hello_flask():
    """Retunr hello"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
