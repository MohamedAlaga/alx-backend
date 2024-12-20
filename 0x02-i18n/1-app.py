#!/usr/bin/env python3
"""
task 1: Basic Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    class used to add configuration options
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    first page
    """
    return render_template("1-index.html")


if __name__ == '__main__':
    app.run(debug=True)
