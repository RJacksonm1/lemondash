from flask import Blueprint

# Create mod
hardlight = Blueprint("hardlight", __name__, url_prefix="/hardlight")

# Import views
import views

# Import filters
from helpers import hue_light_to_rgb
hardlight.add_app_template_filter(hue_light_to_rgb)