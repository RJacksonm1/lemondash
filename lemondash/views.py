from . import app
from flask import render_template


@app.route('/')
def index():
    """ Index page for lemondash. TODO: Explain what it shows """
    return render_template("dashboard.html")