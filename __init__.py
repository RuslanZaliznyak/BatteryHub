from flask import Flask
from app.config import Config
from app.extensions import db
from app.battery_manager import bp as battery_manager_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    app.register_blueprint(battery_manager_bp)

    return app


if __name__ == '__main__':

    create_app().run()



