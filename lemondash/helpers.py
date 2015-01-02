from subprocess import check_output, CalledProcessError
from config import APP_DIR

def escape_every_character(text):
    """ Returns the string provided encoded as html-entities.
    Sets up a generator iterating through `text`, formatting the ordinal of each character as a HTML entity.
    This generator is then passed to the str.join function to construct a new string of these encoded entities.
    :param text: The string to be encoded.
    :return: A string of html-entities representing the given `text`.
    """
    return "".join("&#{};".format(ord(x)) for x in text)


def current_version():
    """
    Queries the CWD git repository to get the latest tag if available, otherwise falling back to the latest commit hash.
    If an exception is thrown this method will simply return an empty string.
    :return: str
    """
    try:
        return check_output(['git', 'describe', '--always'], cwd=APP_DIR)
    except CalledProcessError:
        return ""