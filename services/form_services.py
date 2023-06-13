from app.validators.battery_manager import MainPage
from pydantic import ValidationError
from app.extensions import db
from app.models.battery_18650 import BatteryData
import random


def barcode_gen() -> int:
    """
      Generate a unique barcode number.

      This function checks for the presence of a barcode in the database table.
      If no barcode exists, it generates a unique barcode number and returns it.

      Returns:
          int: Unique barcode number.
      """
    existing_barcodes = db.session.query(BatteryData.barcode).all()
    existing_barcodes = set(barcode[0] for barcode in existing_barcodes)

    while True:
        barcode = random.randint(100000, 999999)
        if barcode not in existing_barcodes:
            return barcode


def form_processing(request):
    """
     Process HTML forms and validate the data.

     This function provides processing of HTML forms. It validates
     the form data and constructs a MainPage object with the validated data.

     If the form data is valid, it returns the MainPage object.
     If the form data is invalid, it returns False
     along with the corresponding validation error.

     Parameters:
         request (flask.request): The Flask request object containing the form data.

     Returns:
         MainPage or tuple: If the form data is valid, returns a MainPage object with the validated data.
         If the form data is invalid, returns False along with the corresponding validation error.
         The validation error can be a ValueError, TypeError, or ValidationError.
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

