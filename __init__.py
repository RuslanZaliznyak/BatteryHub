import logging
from flask import Flask
from waitress import serve
from app.config import Config
from app.battery_manager import bp as battery_manager_bp


def create_app(config_class=Config):
    # Flask App Initialization
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(battery_manager_bp, url_prefix='/battery-manager/')

    # Logs Initialization
    app.logger.setLevel(logging.DEBUG)

    return app



