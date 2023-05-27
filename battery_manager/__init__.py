from flask import Blueprint

bp = Blueprint('battery_manager', __name__)

from app.battery_manager import routes
