import logging
from flask import Flask
from app.config import Config
from app.extensions import db
from app.battery_manager import bp as battery_manager_bp
from waitress import serve


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return make_response(jsonify({"message": "Відсутній дійсний токен!"}), 401)
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except:
            return make_response(jsonify({"message": "Недійсний токен!"}), 401)

        # Повернення функції f
        return f(*args, **kwargs)

    return decorator

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
    db.init_app(app)

    app.register_blueprint(battery_manager_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    serve(app, host='0.0.0.0', port='5001')
