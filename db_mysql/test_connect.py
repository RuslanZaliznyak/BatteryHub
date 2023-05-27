from app.extensions import db
from app.db_mysql import bp


@bp.route('/check-connection')
def check_db_connection():
    try:
        db.session.connection()
        return 'Connection to MySQL database is successful'
    except Exception as ex:
        return f'{ex} \nFailed to connected to MySQL database'

