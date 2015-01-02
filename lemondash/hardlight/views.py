from . import hardlight
from .. import app
from flask import render_template, redirect, url_for, request
from phue import Bridge, Light, Group

BRIDGE_IP = '192.168.1.86'  # TODO: How to find the bridge IP dynamically?
bridge = Bridge(BRIDGE_IP)

# TODO: How to do authentication handshake betterer than calling "bridge.connect()" in every request?

@hardlight.route('/')
def index():
    """ Finds and lists information on Phillips Hue devices on the local network. """
    bridge.connect()

    return render_template("hardlight/index.html",
                           lights=bridge.lights,
                           groups=bridge.groups,
                           schedules=bridge.get_schedule())


@hardlight.route('/light/<int:_id>/')
def light(_id):
    """ Toggles the given light on and off. TODO: Be the AJAX endpoint for multiple interactions with the light.
    :param _id: Light ID
    :return: Redirects user back to where they came
    """
    bridge.connect()

    _light = Light(bridge, _id)
    _light.on = not _light.on

    return redirect(request.referrer or url_for('hardlight.index'))


@hardlight.route('/group/<int:_id>/')
def group(_id):
    """ Toggles the given light group on and off. TODO: Be the AJAX endpoint for multiple interactions with the group.
    :param _id: Group ID
    :return: Redirects user back to where they came
    """
    bridge.connect()

    _group = Group(bridge, _id)
    _group.on = not _group.on

    return redirect(request.referrer or url_for('hardlight.index'))
