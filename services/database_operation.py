import datetime
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from flask import request
from app.models.battery_18650 import BatteryData, RealParameters, StockParameters
from app.models.battery_params import Title, Color, Source, Resistance, Voltage, Capacity
from app.services.form_services import form_processing
from sqlalchemy.orm import joinedload
from sqlalchemy import func


def get_records(last_10=False, one_battery=False, barcode_item=None):
    query = db.session.query(
        BatteryData,
        RealParameters,
        Source). \
        join(RealParameters,
             BatteryData.
             real_params_id == RealParameters.id). \
        join(Source,
             BatteryData.source_id == Source.id). \
        options(joinedload(BatteryData.stock_params_id)). \
        options(joinedload(RealParameters.name_id)). \
        options(joinedload(RealParameters.color_id)). \
        options(joinedload(RealParameters.capacity_id)). \
        options(joinedload(RealParameters.resistance_id)). \
        options(joinedload(RealParameters.voltage_id))

    result = query.all()

    if last_10:
        query = query.order_by(BatteryData.timestamp.desc()).limit(10).all()
        return query

    if one_battery:
        query = query.filter(BatteryData.barcode == barcode_item).first()
        return query

    return query.all()


def add_battery(req):
    form = form_processing(req)
    if form:
        with db.session.begin_nested():
            existing_barcode = BatteryData.query.filter_by(barcode=form.barcode).first()
            if existing_barcode:
                barcode = existing_barcode.barcode

            name_id = get_or_create_record(Title, 'name', form.name)
            color_id = get_or_create_record(Color, 'color', form.color)
            source_id = get_or_create_record(Source, 'source', form.source)
            voltage_id = get_or_create_record(Voltage, 'voltage', form.voltage)
            resistance_id = get_or_create_record(Resistance, 'resistance', form.resistance)

            real_params = RealParameters.query.filter_by(
                name_id=name_id,
                color_id=color_id,
                resistance_id=resistance_id,
                voltage_id=voltage_id
            ).first()

            if real_params:
                real_params_id = real_params.id
            else:
                new_real_params = RealParameters(
                    name_id=name_id,
                    color_id=color_id,
                    resistance_id=resistance_id,
                    voltage_id=voltage_id
                )
                db.session.add(new_real_params)
                db.session.flush()
                real_params_id = new_real_params.id

            new_battery_data = BatteryData(
                barcode=form.barcode,
                real_params_id=real_params_id,
                source_id=source_id
            )
            db.session.add(new_battery_data)

            db.session.commit()


def get_or_create_record(model, field_name, value):
    record = model.query.filter_by(**{field_name: value}).first()
    if record is None:
        print(value)
        print(type(value))

        record_test = Voltage.query.filter(
            Voltage.voltage.between(value - 0.0000001, value + 0.00001)
        ).first()

        print(record_test)

        new_record = model(**{field_name: value})
        db.session.add(new_record)
        db.session.flush()
        return new_record.id

    else:
        print('else')
    return record.id




