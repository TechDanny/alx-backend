#!/usr/bin/env python3
"""
Basic Babel setup
"""


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config():
    """
    set up babel configurations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel(app)
app.config.from_object(Config)
babel.init_app(app)


@babel.localeselector
def get_locale():
    """
    determines the best match with our supported languages.
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """
    define route index
    """
    return render_template("4-index.html")
