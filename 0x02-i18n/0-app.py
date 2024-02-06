from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """
    defines a '/' route
    """
    title = "Welcome to Holberton"
    greet = "Hello world"

    return render_template("0-index.html", title=title, greet=greet)
