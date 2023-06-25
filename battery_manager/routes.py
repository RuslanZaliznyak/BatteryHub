import json

from app.battery_manager import bp
from flask import render_template, request, redirect
import requests
from app.models.form_data import Form

TOKEN = 'test_token'


@bp.route('/battery-manager')
def battery_manager():
    all_battery = requests.get('http://127.0.0.1:5000/api/records',
                               headers={'Authorization': TOKEN})

    req_args = request.args

    if req_args:
        response_from_api = requests.get('http://127.0.0.1:5000/api/records',
                                         params=req_args,
                                         headers={'Authorization': TOKEN})

        if response_from_api.status_code == 200:
            return render_template('battery-manager/all-battery.html', batteries=response_from_api.json()[0])

    return render_template('battery-manager/all-battery.html', batteries=all_battery.json()[0])


@bp.route('/add', methods=['POST', 'GET'])
def add_battery():
    if request.method == 'POST':
        html_form = request.form.to_dict()
        form = Form(**html_form)
        requests.post('http://127.0.0.1:5000/api/records', json=form.json())
    return render_template('battery-manager/add-battery.html')


@bp.route('/delete/<barcode>')
def delete(barcode):
    requests.get('http://127.0.0.1:5000/api/records',
                               headers={'Authorization': TOKEN})
    requests.delete(f'http://127.0.0.1:5000/api/records/delete/{barcode}')
    return redirect('/battery-manager')


@bp.route('/battery-manager/<barcode>')
def get_record_page(barcode):
    record = requests.get(f'http://127.0.0.1:5000/api/records/{barcode}')
    return render_template('battery-manager/battery-page.html',
                           battery=record.json())