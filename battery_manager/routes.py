from app.battery_manager import bp
from app.services.database_operation import add_new_battery, get_records, battery_delete as delete
from flask import render_template, request, redirect


@bp.route('/')
def main_page():
    return render_template('battery-manager/all-battery.html',
                           templates_folder='/battery-manager',
                           batteries=get_records(last_10=False))


@bp.route('/add', methods=['POST', 'GET'])
def add_page():
    if request.method == 'POST':
        add_new_battery(req=request)
        return redirect('/add')

    return render_template(
        'battery-manager/add-battery.html',
        templates_folder='/battery-manager',
        batteries=get_records(last_10=True)
    )


@bp.route('/delete/<barcode>')
def battery_delete(barcode):
    delete(barcode)
    return redirect('/')



