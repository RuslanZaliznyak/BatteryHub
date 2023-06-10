"""
Module Description: This module contains the configuration settings for
the SQLAlchemy ORM database used in the application.

Config: Represents the configuration class for the SQLAlchemy ORM database.
Attributes:

SQLALCHEMY_DATABASE_URI: Specifies the URI for connecting to the MySQL database.
It includes the username, password, host, port, and database name.

SQLALCHEMY_TRACK_MODIFICATIONS: Determines whether to track modifications
in the database models. If set to True, changes will be tracked.
Note: The basedir variable is defined but not used in this class.
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pabxy6-rIqtow-hisbum@localhost:3306/BatteryHubAlpha'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


