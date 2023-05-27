from flask import Flask
from app.config import Config
from app.extensions import db
from app.db_mysql import bp as bp_db_test


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    app.register_blueprint(bp_db_test)

    return app


if __name__ == '__main__':
    create_app().run()
