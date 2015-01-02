# Configuration file for generic settings.  Do not store secret / private data in this file, use instance/config.py
# instead.

import os

# Environment constants
APP_DIR = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = None  # Override this with instance config.

# Environment information (override with instance config)
DEBUG = False
TESTING = False
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Site information
SITE_NAME = "Lemon Dash"
SITE_DESCRIPTION = "Dashboard and management interface for Lemon"
SITE_CONTACT = "rob@rjackson.me"