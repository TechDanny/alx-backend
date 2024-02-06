#!/usr/bin/env python3
"""
Basic Babel setup
"""


from flask import Flask, render_template
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
