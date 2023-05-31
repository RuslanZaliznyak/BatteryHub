from flask import Blueprint
from app.extensions import db

bp = Blueprint('battery_manager', __name__)


from app.battery_manager import routes
