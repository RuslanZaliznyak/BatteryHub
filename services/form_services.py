from app.validators.battery_manager import MainPage
from pydantic import ValidationError
from app.extensions import db
from app.models.battery_18650 import BatteryData
import random


def barcode_gen() -> int:
    """
    This function checks for a barcode in the database table,
    if not creates a unique barcode and returns it
    :return: unique barcode number
    """
    existing_barcodes = db.session.query(BatteryData.barcode).all()
    existing_barcodes = set(barcode[0] for barcode in existing_barcodes)

    while True:
        barcode = random.randint(100000, 999999)
        if barcode not in existing_barcodes:
            return barcode


def form_processing(request):
    """
    This function provides processing of HTML forms.
    It validates the data and sends it, checks to the validator that everything is OK, returns a MainPage object with the data
    :param flask request:
    :return:
    """
    try:
        battery_data = MainPage(
            barcode=barcode_gen(),
            name=request.form.get('name'),
            color=request.form.get('color'),
            voltage=request.form.get('voltage'),
            resistance=request.form.get('resistance'),
            source=request.form.get('source'),
            capacity=request.form.get('capacity'),
            weight=request.form.get('weight')
        )
        return battery_data

    except (ValueError, TypeError) as e:
        return False, e
    except ValidationError as e:
        return False, e

