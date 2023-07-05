import json

from app.battery_manager import bp
from flask import render_template, request, redirect
from app.services.api_utils import APIClient


@bp.route('/')
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
def add_battery():
    response = APIClient.get_last_record()
    if request.method == 'POST':
        response = APIClient.add_record(request)
        if 'error' not in response:
            return redirect('/battery-manager/add')
    return render_template('battery-manager/add-battery.html',
                           battery=response[0])


@bp.route('/update/<barcode>', methods=['GET', 'POST'])
def update(barcode):
    response = APIClient.get_record_by_barcode(barcode)

    if request.method == 'POST':

        new_params = request.form.to_dict()

        #TEST FUNCTION!

        result = {}
        for key in response:
            if key == 'barcode' or key == 'datetime' or key == 'id':
                continue
            result[key] = new_params[key]

        response_ = APIClient.update_record(barcode, result)

        return redirect('/battery-manager/update/<barcode>')

    return render_template('battery-manager/update-page.html',
                           battery=response)


@bp.route('/delete/<barcode>')
def delete(barcode):
    APIClient.record_delete(barcode=barcode)
    return redirect('/battery-manager')


@bp.route('/<barcode>')
def get_record_page(barcode):
    record = APIClient.get_record_by_barcode(barcode)
    return render_template('battery-manager/battery-page.html',
                           battery=record)
