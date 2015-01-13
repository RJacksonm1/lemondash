from rgb_cie import Converter, ColorHelper
from math import fabs


def xy_to_hex(xy):
    """ Converts CIE 1931 coordinates into an approximate RGB hex representation.
    :param xy: Array or tuple of CIE1931 X and Y coordinates.
    :return: A hexadecimal string.
    """
    c = Converter()
    return c.CIE1931ToHex(*xy)


def hex_to_xy(hex):
    """ Converts RGX hex colour into CIE 1931 coordinates.
    :param hex: Hex colour string
    :return: Tuple of X, Y coordinates
    """
    c = Converter()
    return c.hexToCIE1931(hex)