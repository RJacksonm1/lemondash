from rgb_cie import Converter


def xy_to_hex(xy):
    """ Converts CIE 1931 coordinates into an approximate RGB hex representation.
    :param xy: Array or tuple of CIE1931 X and Y coordinates.
    :return: A hexadecimal string.
    """
    c = Converter()
    return c.CIE1931ToHex(*xy)