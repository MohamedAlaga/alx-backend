#!/usr/bin/env python3
'''Task 2: Get locale from request
'''

from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    '''Config class'''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    select the best locale from request
    """
    return request.accept_languages.best_match(["fr", "en"])


@app.route('/')
def index():
    """
    first page
    """
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(debug=True)
