from flask import Blueprint

# Create mod
hardlight = Blueprint("hardlight", __name__, url_prefix="/hardlight")

# Import views
import views

# Import filters
from helpers import xy_to_hex
hardlight.add_app_template_filter(xy_to_hex)