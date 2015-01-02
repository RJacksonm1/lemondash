from . import app


@app.route('/')
def index():
    """ Index page for lemondash. TODO: Explain what it shows """
    return "Hello world"