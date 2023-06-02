import datetime
from app.extensions import db
from flask import request
from app.models.battery_18650 import \
    BatteryData, BatteryName, BatteryColor, \
    BatterySource, BatteryResistance, BatteryVoltage
from sqlalchemy.exc import SQLAlchemyError


def add_new_battery(req: request):
    barcode = req.form.get('barcode')
    battery_name = req.form.get('title')
    color = req.form.get('color')
    voltage = req.form.get('voltage')
    resistance = req.form.get('resistance')
    battery_source = req.form.get('battery_source')
    timestamp = datetime.datetime.now()

    try:
        with db.session.begin_nested():
            existing_name = \
                BatteryName.query.filter_by(battery_name=battery_name).first()
            if existing_name:
                name_id = existing_name.id
            else:
                new_name = BatteryName(battery_name=battery_name)
                db.session.add(new_name)
                db.session.flush()
                name_id = new_name.id

            existing_color = \
                BatteryColor.query.filter_by(battery_color=color).first()
            if existing_color:
                color_id = existing_color.id
            else:
                new_color = BatteryColor(battery_color=color)
                db.session.add(new_color)
                db.session.flush()
                color_id = new_color.id

            existing_source = \
                BatterySource.query.filter_by(battery_source=battery_source).first()
            if existing_source:
                source_id = existing_source.id
            else:
                new_source = BatterySource(battery_source=battery_source)
                db.session.add(new_source)
                db.session.flush()
                source_id = new_source.id

            existing_voltage = \
                BatteryVoltage.query.filter_by(battery_voltage=voltage).first()
            if existing_voltage:
                voltage_id = existing_voltage.id
            else:
                new_voltage = BatteryVoltage(battery_voltage=voltage)
                db.session.add(new_voltage)
                db.session.flush()
                voltage_id = new_voltage.id

            existing_resistance = \
                BatteryResistance.query.filter_by(battery_resistance=resistance).first()
            if existing_resistance:
                resistance_id = existing_resistance.id
            else:
                new_resistance = BatteryResistance(battery_resistance=resistance)
                db.session.add(new_resistance)
                db.session.flush()
                resistance_id = new_resistance.id

            insert_data = BatteryData(
                barcode=barcode,
                name_id=name_id,
                color_id=color_id,
                voltage_id=voltage_id,
                resistance_id=resistance_id,
                battery_source_id=source_id,
                timestamp=timestamp
            )
            db.session.add(insert_data)

        db.session.commit()

        return "Data has been successfully added to the database"
    except SQLAlchemyError as e:
        db.session.rollback()
        return "Error adding data to database " + str(e)
