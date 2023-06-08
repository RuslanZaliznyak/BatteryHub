import datetime
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from flask import request
from app.models.battery_18650 import BatteryData, RealParameters, StockParameters
from app.models.battery_params import BatteryName, BatteryColor, BatterySource, BatteryResistance, BatteryVoltage, BatteryCapacity
from app.services.form_services import form_processing


def add_battery(req):
    form = form_processing(req)
    if form:
        with db.session.begin_nested():
            existing_barcode = BatteryData.query.filter_by(barcode=form.barcode).first()
            if existing_barcode is None:
                print("Stop code. Barcode exists")
                return 'Barcode exists - "Error message"'

            name_id = get_or_create_record(BatteryName, 'name', form.name)
            color_id = get_or_create_record(BatteryColor, 'color', form.color)
            source_id = get_or_create_record(BatterySource, 'source', form.source)
            voltage_id = get_or_create_record(BatteryVoltage, 'voltage', form.voltage)
            resistance_id = get_or_create_record(BatteryResistance, 'resistance', form.resistance)

            real_params = RealParameters.query.filter_by(name_id=name_id).first()
            if real_params:
                real_params_id = real_params.id
            else:
                new_real_params = RealParameters(name_id=name_id,
                                                 color_id=color_id,
                                                 resistance_id=resistance_id,
                                                 voltage_id=voltage_id)
                db.session.add(new_real_params)
                db.session.flush()
                real_params_id = new_real_params.id

            new_battery_data = BatteryData(barcode=form.barcode,
                                           real_params_id=real_params_id,
                                           source_id=source_id)
            db.session.add(new_battery_data)

            db.session.commit()


def get_or_create_record(model, field_name, value):
    record = model.query.filter_by(**{field_name: value}).first()
    if record:
        return record.id
    new_record = model(**{field_name: value})
    db.session.add(new_record)
    db.session.flush()
    return new_record.id
