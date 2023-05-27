from flask import Blueprint

bp = Blueprint('db_mysql-check', __name__)

from app.db_mysql import test_connect
