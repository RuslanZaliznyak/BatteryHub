"""
This file defines a Python module that contains the blueprint for the battery manager functionality.

The `Blueprint` class is imported from the `flask` module to create a blueprint object named 'battery_manager' within
this module.

The blueprint serves as a way to organize and group related routes and views for battery management. It can be
registered with a Flask application to handle specific URLs and requests related to battery management.

The blueprint defined in this module can be used by importing it into other parts of the application and registering
it with the Flask application.

This module acts as the entry point for importing the 'bp' blueprint in other parts of the application.
"""


from flask import Blueprint

bp = Blueprint('battery_manager', __name__)

from app.battery_manager import routes
