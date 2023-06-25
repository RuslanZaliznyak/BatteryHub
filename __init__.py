import logging
from flask import Flask
from waitress import serve
from app.config import Config
from app.battery_manager import bp as battery_manager_bp


def create_app(config_class=Config):
    # Flask App Initialization
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(battery_manager_bp)

    # Logs Initialization
    app.logger.setLevel(logging.DEBUG)

    return app


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app = create_app()
    serve(app, host='127.0.0.1', port=5001)
