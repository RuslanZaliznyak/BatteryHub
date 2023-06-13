import logging

from flask import Flask
from app.config import Config
from app.extensions import db
from app.battery_manager import bp as battery_manager_bp
from waitress import serve


def create_app(config_class=Config):
    """
    The function create and initialises Flask app and Database.
    Here you to register your blueprint.


    :param config_class: Accepts a config class with SQLAlchemy configurations
    :return: Returns the Flask application - app
    """
    app = Flask(__name__)

    waitress_logger = logging.getLogger('waitress')
    waitress_logger.setLevel(logging.DEBUG)
    waitress_logger.addHandler(logging.StreamHandler())

    app.config.from_object(config_class)
    db.init_app(app)

    # Blueprint registration
    app.register_blueprint(battery_manager_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    serve(app, host='0.0.0.0', port='5000')


