import json

from app.battery_manager import bp
from flask import render_template, request, redirect
import requests
from app.models.form_data import Form
from app.config import Config as c
from app.services.api_utils import APIClient


@bp.route('/battery-manager/dashboard')
def dashboard():
    # NOTE: This function is still under development
    return render_template('battery-manager/dashboard-page.html')


@bp.route('/battery-manager')
# ARGS Search not works
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
    if request.method == 'POST':
        response = APIClient.add_record(request)
        if 'error' not in response:
            return render_template('battery-manager/add-battery.html')
    return render_template('battery-manager/add-battery.html')


@bp.route('/delete/<barcode>')
def delete(barcode):
    requests.get(c.API_URL,
                 headers={'Authorization': c.TOKEN})
    requests.delete(f'{c.API_URL}/delete/{barcode}')
    return redirect('/battery-manager')


@bp.route('/battery-manager/<barcode>')
def get_record_page(barcode):
    record = requests.get(f'{c.API_URL}/{barcode}')
    return render_template('battery-manager/battery-page.html',
                           battery=record.json())
