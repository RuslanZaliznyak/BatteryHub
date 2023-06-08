from app.validators.battery_manager import MainPage
from pydantic import ValidationError
from app.extensions import db
from app.models.battery_18650 import BatteryData
import random


def barcode_gen():
    existing_barcodes = db.session.query(BatteryData.barcode).all()
    existing_barcodes = set(barcode[0] for barcode in existing_barcodes)

    while True:
        barcode = random.randint(100000, 999999)
        if barcode not in existing_barcodes:
            return barcode


def form_processing(battery):
    global capacity
    try:
        capacity_existing = battery.form.get('capacity')
        if capacity_existing is not None:
            capacity = capacity_existing
        else:
            capacity = 0

        battery_data = MainPage(
            barcode=barcode_gen(),
            name=battery.form.get('name'),
            color=battery.form.get('color'),
            voltage=float(battery.form.get('voltage')),
            resistance=float(battery.form.get('resistance')),
            source=battery.form.get('source')
        )
        return battery_data
    except (ValueError, TypeError) as e:
        return str(e)
    except ValidationError as e:
        return str(e)
