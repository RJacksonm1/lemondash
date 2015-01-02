from . import hardlight
from .. import app
from .helpers import xy_to_hex, invert_colour
from functools import wraps
from flask import render_template, redirect, url_for, request, g, jsonify
from phue import Bridge, Light, Group, PhueRegistrationException

BRIDGE_IP = '192.168.1.86'  # TODO: How to find the bridge IP dynamically?


def requires_bridge(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        try:
            g.bridge = Bridge(BRIDGE_IP)
            g.bridge.connect()
            return func(*args, **kwargs)
        except PhueRegistrationException:
            return redirect(url_for('hardlight.connect_to_bridge'))
    return decorated_view


@hardlight.route('/connect/')
def connect_to_bridge():
    return render_template("hardlight/connect_to_bridge.html")


@hardlight.route('/')
@requires_bridge
def index():
    """ Finds and lists information on Phillips Hue devices on the local network. """
    return render_template("hardlight/index.html",
                           lights=g.bridge.lights,
                           groups=g.bridge.groups,
                           schedules=g.bridge.get_schedule())


@hardlight.route('/light/<int:_id>/', methods=["POST"])
@requires_bridge
def light(_id):
    """ Toggles the given light on and off. TODO: Be the AJAX endpoint for multiple interactions with the light.
    :param _id: Light ID
    :return: Redirects user back to where they came
    """

    _light = Light(g.bridge, _id)

    if 'on' in request.form.keys():
        _light.on = request.form.get('on') == "true"

    return jsonify({
        'on': _light.on,
        'colour': xy_to_hex(_light.xy),
        'inverted_colour': invert_colour(xy_to_hex(_light.xy)),
        'brightness': int(round((_light.brightness / 255.0) * 100.0))
    })


@hardlight.route('/group/<int:_id>/')
@requires_bridge
def group(_id):
    """ Toggles the given light group on and off. TODO: Be the AJAX endpoint for multiple interactions with the group.
    :param _id: Group ID
    :return: Redirects user back to where they came
    """

    _group = Group(g.bridge, _id)
    _group.on = not _group.on

    return redirect(request.referrer or url_for('hardlight.index'))
