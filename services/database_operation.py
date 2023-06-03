import datetime

from sqlalchemy.orm import sessionmaker, aliased

from app.extensions import db
from flask import request
from app.models.battery_18650 import \
    BatteryData, BatteryName, BatteryColor, \
    BatterySource, BatteryResistance, BatteryVoltage
from sqlalchemy.exc import SQLAlchemyError
from app.services.form_services import form_processing
from pydantic import ValidationError


def add_new_battery(req: request):
    battery_data = form_processing(req)
    if battery_data:
        try:
            with db.session.begin_nested():
                existing_name = \
                    BatteryName.query.filter_by(
                        battery_name=battery_data.name).first()
                if existing_name:
                    name_id = existing_name.id
                else:
                    new_name = BatteryName(
                        battery_name=battery_data.name)
                    db.session.add(new_name)
                    db.session.flush()
                    name_id = new_name.id

                existing_color = \
                    BatteryColor.query.filter_by(
                        battery_color=battery_data.color).first()
                if existing_color:
                    color_id = existing_color.id
                else:
                    new_color = BatteryColor(
                        battery_color=battery_data.color)
                    db.session.add(new_color)
                    db.session.flush()
                    color_id = new_color.id

                existing_source = \
                    BatterySource.query.filter_by(
                        battery_source=battery_data.source).first()
                if existing_source:
                    source_id = existing_source.id
                else:
                    new_source = BatterySource(
                        battery_source=battery_data.source)
                    db.session.add(new_source)
                    db.session.flush()
                    source_id = new_source.id

                existing_voltage = \
                    BatteryVoltage.query.filter_by(
                        battery_voltage=battery_data.voltage).first()
                if existing_voltage:
                    voltage_id = existing_voltage.id
                else:
                    new_voltage = BatteryVoltage(
                        battery_voltage=battery_data.voltage)
                    db.session.add(new_voltage)
                    db.session.flush()
                    voltage_id = new_voltage.id

                existing_resistance = \
                    BatteryResistance.query.filter_by(
                        battery_resistance=battery_data.resistance).first()
                if existing_resistance:
                    resistance_id = existing_resistance.id
                else:
                    new_resistance = BatteryResistance(
                        battery_resistance=battery_data.resistance)
                    db.session.add(new_resistance)
                    db.session.flush()
                    resistance_id = new_resistance.id

                insert_data = BatteryData(
                    barcode=battery_data.barcode,
                    name_id=name_id,
                    color_id=color_id,
                    voltage_id=voltage_id,
                    resistance_id=resistance_id,
                    battery_source_id=source_id,
                    timestamp=datetime.datetime.now()
                )
                db.session.add(insert_data)
            db.session.commit()

            return "Data has been successfully added to the database"
        except SQLAlchemyError as e:
            db.session.rollback()
            return "Error adding data to database " + str(e)


def get_for_main_page():
    session = db.session
    main = aliased(BatteryData)
    color = aliased(BatteryColor)
    name = aliased(BatteryName)
    source = aliased(BatterySource)
    resistance = aliased(BatteryResistance)
    voltage = aliased(BatteryVoltage)

    query = session.query(
        main.barcode,
        color.battery_color,
        name.battery_name,
        source.battery_source,
        resistance.battery_resistance,
        voltage.battery_voltage
    ).join(
        color, main.color_id == color.id
    ).join(
        name, main.name_id == name.id
    ).join(
        source, main.battery_source_id == source.id
    ).join(
        resistance, main.resistance_id == resistance.id
    ).join(
        voltage, main.voltage_id == voltage.id
    )

    results = query.all()

    print (results)
    return results

