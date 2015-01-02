from rgb_cie import Converter, ColorHelper
from math import fabs


def xy_to_hex(xy):
    """ Converts CIE 1931 coordinates into an approximate RGB hex representation.
    :param xy: Array or tuple of CIE1931 X and Y coordinates.
    :return: A hexadecimal string.
    """
    c = Converter()
    return c.CIE1931ToHex(*xy)

def invert_colour(hex_string):
    ch = ColorHelper()

    # Turn hex into REGEBE so we can mathemagic it
    rgb = ch.hexToRGB(hex_string)

    # Invert the colours
    for i in xrange(0, len(rgb)):
        rgb[i] = fabs(rgb[i] - 255)

    # Turn back into hex and return
    return ch.rgbToHex(*rgb)