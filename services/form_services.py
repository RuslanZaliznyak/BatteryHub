from app.validators import battery_manager
from flask import request
from datetime import datetime
from app.validators.battery_manager import MainPage
from pydantic import ValidationError


def form_processing(battery):
    try:
        battery_data = MainPage(
            barcode=int(battery.form.get('barcode')),
            name=battery.form.get('title'),
            color=battery.form.get('color'),
            voltage=float(battery.form.get('voltage')),
            resistance=float(battery.form.get('resistance')),
            source=battery.form.get('battery_source')
        )
        return battery_data
    except (ValueError, TypeError) as e:
        return str(e)
    except ValidationError as e:
        return str(e)
