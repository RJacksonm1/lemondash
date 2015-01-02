"""
Manager script :)
Takes the following commands:
- runserver
- shell
"""

from lemondash import app
from flask.ext.script import Manager

manager = Manager(app)

if __name__ == "__main__":
    manager.run()