from app.battery_manager import bp
from app.services.database_operation import add_record, get_records, delete_record
from flask import render_template, request, redirect


@bp.route('/')
def main_page():
    return render_template('battery-manager/dashboard-page.html',
                           batteries=get_records(last_10=True))


@bp.route('/battery-manager', methods=['POST', 'GET'])
def manager_page():
    if request.method == 'POST':
        battery = get_records(
            retrieve_one=True, barcode=request.form.get('barcode'))
        print(battery)
        if battery:
            return render_template('battery-manager/battery-page.html',
                                   battery=battery)
        else:
            return redirect('/battery-manager')
    return render_template('battery-manager/all-battery.html',
                           templates_folder='battery-manager',
                           batteries=get_records()
                           )


@bp.route('/add', methods=['POST', 'GET'])
def add_page():
    if request.method == 'POST':
        return add_record(flask_request=request)
    return render_template(
        'battery-manager/add-battery.html',
        templates_folder='/battery-manager',
        batteries=get_records(last_10=True)
    )


@bp.route('/<barcode>')
def item_page(barcode):
    battery = get_records(retrieve_one=True, barcode=barcode)
    return render_template('battery-manager/battery-page.html',
                           battery=battery)


@bp.route('/delete/<item_barcode>')
def item_delete(item_barcode):
    delete_record(item_barcode)
    return redirect('/')

