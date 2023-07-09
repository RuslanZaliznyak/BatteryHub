import logging
from flask import Flask
from app.config import Config
from app.battery_manager import bp as battery_manager_bp
from app.extensions import db, login_manager, bcrypt
from app.models.auth import User
from app.auth import auth_bp
from app.core import core_bp


def create_app(config_class=Config):
    # Flask App Initialization
    app = Flask(__name__)
    app.config.from_object(config_class)

    login_manager.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(battery_manager_bp, url_prefix='/battery-manager/')

    # Logs Initialization
    app.logger.setLevel(logging.DEBUG)

    app.register_blueprint(auth_bp)
    app.register_blueprint(core_bp)

    return app


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()