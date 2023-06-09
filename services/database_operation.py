import datetime
from sqlalchemy.exc import SQLAlchemyError
from app.extensions import db
from flask import request, redirect
from app.models.battery_18650 import BatteryData, RealParameters, StockParameters
from app.models.battery_params import Name, Color, Source, Resistance, Voltage, Capacity, Weight
from app.services.form_services import form_processing
from sqlalchemy.orm import joinedload, aliased
from flask import render_template


def get_records(last_10=False, one_battery=False, barcode_item=None):
    db.engine.execute(
        """"""
    )


    if last_10:
        query = query.order_by(BatteryData.timestamp.desc()).limit(10).all()
        return query

    if one_battery:
        query = query.filter(BatteryData.barcode == barcode_item).first()
        return query

    return result


def add_battery(flask_req):
    """
    Process battery data from the request and add it to the database.

    Args:
        flask_req (request): The request object containing html form data with
        battery data.

    Returns:
        response: A redirect response if the battery data is successfully processed and added to the database.
        template: A rendered template for trying again if the battery data is invalid or the process fails.

    """
    form = form_processing(flask_req)
    if form:
        with db.session.begin_nested():
            name_id = get_or_create_record(Name, 'name', form.name)
            color_id = get_or_create_record(Color, 'color', form.color)
            source_id = get_or_create_record(Source, 'source', form.source)
            voltage_id = get_or_create_record(Voltage, 'voltage', form.voltage)
            resistance_id = get_or_create_record(Resistance, 'resistance', form.resistance)
            capacity_id = get_or_create_record(Capacity, 'capacity', form.capacity)
            weight_id = get_or_create_record(Weight, 'weight', form.weight)

            real_params = RealParameters.query.filter_by(
                name_id=name_id,
                color_id=color_id,
                resistance_id=resistance_id,
                voltage_id=voltage_id,
                capacity_id=capacity_id,
                weight_id=weight_id
            ).first()

            if real_params:
                real_params_id = real_params.id

            else:
                new_real_params = RealParameters(
                    name_id=name_id,
                    color_id=color_id,
                    resistance_id=resistance_id,
                    voltage_id=voltage_id,
                    capacity_id=capacity_id,
                    weight_id=weight_id
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
        return redirect('/add')
    else:
        return render_template('Try again')


def get_or_create_record(model, field_name, value) -> int:
    """
    Get an existing record from the specified model based on the field value,
    or create a new record if it doesn't exist.

    Args:
        model (db.Model): The SQLAlchemy model to query or create records from.
        field_name (str): The name of the field to check for matching values.
        value: The value to match against the field in the model.

    Returns:
        int: The ID of the existing record if found,
        or the ID of the newly created record.

    """
    record = model.query.filter_by(**{field_name: value}).first()
    if record is None:
        print(f'{record} is None. Create a new record in database')
        print(value)
        print(type(value))
        new_record = model(**{field_name: value})
        db.session.add(new_record)
        db.session.flush()
        db.session.refresh(new_record)
        return new_record.id

    else:
        print('else')
    return record.id
