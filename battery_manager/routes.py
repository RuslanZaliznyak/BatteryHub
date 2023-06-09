from app import db
from app.battery_manager import bp
from app.services.database_operation import add_battery, get_records
from flask import render_template, request, redirect


@bp.route('/')
def main_page():

    return render_template('battery-manager/all-battery.html',
                           templates_folder='battery-manager',
                           )


@bp.route('/add', methods=['POST', 'GET'])
def add_page():
    if request.method == 'POST':
        add_battery(req=request)
        return redirect('/add')

    return render_template(
        'battery-manager/add-battery.html',
        templates_folder='/battery-manager',
        batteries=[1, 2, 3]
    )



