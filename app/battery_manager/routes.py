from flask_login import login_required

from app.battery_manager import bp
from flask import render_template, request, redirect
from app.services.api_utils import APIClient


@bp.route('/')
@login_required
def battery_manager():
    all_battery_records = APIClient.get_all_records()

    filtered_battery_records = APIClient.get_records_with_args(request)
    if filtered_battery_records:
        return render_template(
            'battery-manager/all-battery.html',
            batteries=filtered_battery_records['data'])

    return render_template(
        'battery-manager/all-battery.html',
        batteries=all_battery_records)


@bp.route('/add', methods=['POST', 'GET'])
@login_required
def add_battery():
    response = APIClient.get_last_record()
    if request.method == 'POST':
        response = APIClient.add_record(request)
        if 'error' not in response:
            return redirect('/battery-manager/add')
    print(response)
    return render_template('battery-manager/add-battery.html',
                           batteries=response)


@bp.route('/update/<barcode>', methods=['GET', 'POST'])
@login_required
def update(barcode):
    response = APIClient.get_record_by_barcode(barcode)

    if request.method == 'POST':
        result = {key: request.form.to_dict()[key]
                  for key in response if key not in ['barcode', 'datetime', 'id']}
        APIClient.update_record(barcode, result)

        return redirect('/battery-manager/update/<barcode>')

    return render_template('battery-manager/update-page.html',
                           battery=response)


@bp.route('/delete/<barcode>')
@login_required
def delete(barcode):
    APIClient.record_delete(barcode=barcode)
    return redirect('/battery-manager')


@bp.route('/<barcode>')
@login_required
def get_record_page(barcode):
    record = APIClient.get_record_by_barcode(barcode)
    return render_template('battery-manager/battery-page.html',
                           battery=record)
