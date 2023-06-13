import datetime
from app.extensions import db
from flask import request, redirect, jsonify
from app.models.battery_18650 import BatteryData, RealParameters, StockParameters
from app.models.battery_params import Name, Color, Source, Resistance, Voltage, Capacity, Weight
from app.services.form_services import form_processing
from flask import render_template
from sqlalchemy import exc


def get_records(last_10=False, retrieve_one=False, barcode=None):
    """
    Retrieve battery records from the database.

    Args:
        last_10 (bool, optional): Flag indicating whether to retrieve the last 10 battery records.
                                  Defaults to False.
        retrieve_one (bool, optional): Flag indicating whether to retrieve a single battery record.
                                       Defaults to False.
        barcode (int, optional): Barcode of the specific battery to retrieve.
                                 Required if `retrieve_one` is True.

    Returns:
        list or object: A list of battery records or a single battery record,
                        depending on the specified retrieval options.
    """
    query = db.session.query(
        BatteryData.barcode,
        Name.name,
        Color.color,
        Voltage.voltage,
        Resistance.resistance,
        Source.source,
        Weight.weight,
        Capacity.capacity
    ).join(
        RealParameters, BatteryData.real_params_id == RealParameters.id
    ).outerjoin(
        Source, BatteryData.source_id == Source.id
    ).outerjoin(
        Name, RealParameters.name_id == Name.id
    ).join(
        Color, RealParameters.color_id == Color.id
    ).join(
        Resistance, RealParameters.resistance_id == Resistance.id
    ).join(
        Voltage, RealParameters.voltage_id == Voltage.id
    ).outerjoin(
        Weight, RealParameters.weight_id == Weight.id
    ).outerjoin(
        Capacity, RealParameters.capacity_id == Capacity.id
    )

    if last_10:
        query = query.order_by(BatteryData.timestamp.desc()).limit(10).all()
    elif retrieve_one and barcode is not None:
        query = query.filter(BatteryData.barcode == barcode).first()
    else:
        query = query.all()

    return query


def add_record(flask_request):
    """
    Process battery data from the request and add it to the database.

    Args:
        flask_request (request): The request object containing HTML form data with battery data.

    Returns:
        response: A redirect response if the battery data is successfully processed and added to the database.
        template: A rendered template for trying again if the battery data is invalid or the process fails.

    """
    form = form_processing(flask_request)
    if form:
        # Get or create the IDs for the related records

        name_id = get_or_create_record(Name, 'name', form.name)
        color_id = get_or_create_record(Color, 'color', form.color)
        source_id = get_or_create_record(Source, 'source', form.source)
        voltage_id = get_or_create_record(Voltage, 'voltage', form.voltage)
        resistance_id = get_or_create_record(Resistance, 'resistance', form.resistance)
        capacity_id = get_or_create_record(Capacity, 'capacity', form.capacity)
        weight_id = get_or_create_record(Weight, 'weight', form.weight)

        # Check if the real parameters already exist in the database
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
            # Create a new real parameters record
            new_real_params = RealParameters(
                name_id=name_id,
                color_id=color_id,
                resistance_id=resistance_id,
                voltage_id=voltage_id,
                capacity_id=capacity_id,
                weight_id=weight_id
            )
            db.session.add(new_real_params)
            db.session.flush()  # Flush to get the ID before committing
            real_params_id = new_real_params.id

        # Create a new battery data record
        new_battery_data = BatteryData(
            barcode=form.barcode,
            real_params_id=real_params_id,
            source_id=source_id,
            timestamp=datetime.datetime.now()  # Save the current datetime
        )
        db.session.add(new_battery_data)
        db.session.commit()

        return redirect('/add')
    else:
        # To add error handling
        return render_template('try_again.html')


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
        new_record = model(**{field_name: value})
        db.session.add(new_record)
        db.session.flush()
        db.session.refresh(new_record)
        return new_record.id
    return record.id


def delete_record(item_barcode: int):
    try:
        record = \
            db.session.query(BatteryData).filter(
                BatteryData.barcode == item_barcode).first()
        db.session.delete(record)
        db.session.commit()
    except exc.IntegrityError as ex:
        db.session.rollback()
        print("Integrity error occurred:", str(ex))
        return jsonify({"error": "An error occurred while deleting the record."}), 500
