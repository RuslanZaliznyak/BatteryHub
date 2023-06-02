from app.battery_manager import bp
from app.extensions import db
from app.services.database_operation import add_new_battery
from flask import render_template, request


@bp.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        return add_new_battery(req=request)

    return render_template(
        'battery-manager/main.html',
        templates_folder='app/templates/battery-manager'
    )
