import os
from flask import Flask
from flask.ext.debugtoolbar import DebugToolbarExtension
from .helpers import escape_every_character
from .helpers import current_version

app = Flask(__name__,
            instance_relative_config=True,
            instance_path=os.path.join(os.path.abspath(os.path.dirname(__file__)), '../instance/'))

# Load default config
app.config.from_object("config")

# Load instance config
app.config.from_pyfile("config.py")

# Load extensions
toolbar = DebugToolbarExtension(app)

# Set up jinja2 filters.
app.add_template_filter(escape_every_character)

# Load current app version into globals
app.config['VERSION'] = current_version()

# Load views
import views

# Load blueprints
# TODO

if __name__ == '__main__':
    app.run()
