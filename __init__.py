import logging
from flask import Flask
from app.config import Config
from app.battery_manager import bp as battery_manager_bp
from waitress import serve


def create_app(config_class=Config):
    app = Flask(__name__)

    app.logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    app.logger.addHandler(console_handler)

    waitress_logger = logging.getLogger('waitress')
    waitress_logger.setLevel(logging.DEBUG)
    waitress_logger.addHandler(logging.StreamHandler())

    app.config.from_object(config_class)

    app.register_blueprint(battery_manager_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5001)
