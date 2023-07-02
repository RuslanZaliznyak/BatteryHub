from app.battery_manager import bp
from flask import render_template, request, redirect
from app.services.api_utils import APIClient


@bp.route('/battery-manager')
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


@bp.route('/battery-manager/add', methods=['POST', 'GET'])
def add_battery():
    if request.method == 'POST':
        response = APIClient.add_record(request)
        if 'error' not in response:
            return render_template('battery-manager/add-battery.html')
    return render_template('battery-manager/add-battery.html')


@bp.route('/delete/<barcode>')
def delete(barcode):
    APIClient.record_delete(barcode=barcode)
    return redirect('/battery-manager')


@bp.route('/battery-manager/<barcode>')
def get_record_page(barcode):
    record = APIClient.get_record_by_barcode(barcode)
    return render_template('battery-manager/battery-page.html',
                           battery=record)
