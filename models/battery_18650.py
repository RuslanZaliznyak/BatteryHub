from app.extensions import db


class BatteryData(db.Model):
    __tablename__ = 'battery_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barcode = db.Column(db.Integer, unique=True, nullable=False)
    stock_params_id = db.Column(db.ForeignKey('stock_parameters.id'))
    real_params_id = db.Column(db.ForeignKey('real_parameters.id'))
    source_id = db.Column(db.Integer, db.ForeignKey('battery_source.id'), nullable=False)
    photo_id = db.Column(db.Integer, db.ForeignKey('battery_photo.id'))
    timestamp = db.Column(db.DateTime)


class StockParameters(db.Model):
    __tablename__ = 'stock_parameters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_id = db.Column(db.Integer, db.ForeignKey('battery_name.id'))
    capacity_id = db.Column(db. Integer, db.ForeignKey('battery_capacity.id'))
    resistance_id = db.Column(db.Integer, db.ForeignKey('battery_resistance.id'))
    charge_current_id = db.Column(db.Integer, db.ForeignKey('battery_current.id'))
    max_charge_current_id = db.Column(db. Integer, db.ForeignKey('battery_current.id'))
    discharge_current_id = db.Column(db.Integer, db.ForeignKey('battery_current.id'))
    max_discharge_current_id = db.Column(db.Integer, db.ForeignKey('battery_current.id'))


class RealParameters(db.Model):
    __tablename__ = 'real_parameters'
    id = db.Column(db. Integer, primary_key=True, autoincrement=True)
    name_id = db.Column(db.Integer, db.ForeignKey('battery_name.id'))
    color_id = db.Column(db.Integer, db.ForeignKey('battery_color.id'), nullable=False)
    capacity_id = db.Column(db.Integer, db.ForeignKey('battery_capacity.id'))
    resistance_id = db.Column(db.Integer, db.ForeignKey('battery_resistance.id'), nullable=False)
    voltage_id = db.Column(db.Integer, db.ForeignKey('battery_voltage.id'), nullable=False)

