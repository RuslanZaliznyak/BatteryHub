from app.battery_manager import bp
from app.services.database_operation import add_battery, get_records
from flask import render_template, request, redirect
from app import db
from app.models.battery_18650 import BatteryData


@bp.route('/')
def main_page():
    return render_template('battery-manager/all-battery.html',
                           templates_folder='battery-manager',
                           batteries=get_records()
                           )


@bp.route('/add', methods=['POST', 'GET'])
def add_page():
    if request.method == 'POST':
        return add_battery(flask_request=request)
    return render_template(
        'battery-manager/add-battery.html',
        templates_folder='/battery-manager',
        batteries=get_records(last_10=True)
    )


@bp.route('/delete/<item_barcode>')
def item_delete(item_barcode):
    element_to_delete = \
        db.session.query(BatteryData).filter(BatteryData.barcode == item_barcode).first()
    db.session.delete(element_to_delete)
    db.session.commit()
    return redirect('/')


