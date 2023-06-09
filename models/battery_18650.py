from app.extensions import db


class BatteryData(db.Model):
    __tablename__ = 'battery_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barcode = db.Column(db.Integer, unique=True, nullable=False)
    stock_params_id = db.Column(db.ForeignKey('stock_parameters.id'))
    real_params_id = db.Column(db.ForeignKey('real_parameters.id'))
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable=False)
    photo_id = db.Column(db.Integer, db.ForeignKey('photo.id'))
    timestamp = db.Column(db.DateTime)


class StockParameters(db.Model):
    __tablename__ = 'stock_parameters'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_id = db.Column(db.Integer, db.ForeignKey('title.id'))
    capacity_id = db.Column(db. Integer, db.ForeignKey('capacity.id'))
    resistance_id = db.Column(db.Integer, db.ForeignKey('resistance.id'))
    charge_current_id = db.Column(db.Integer, db.ForeignKey('current.id'))
    max_charge_current_id = db.Column(db. Integer, db.ForeignKey('current.id'))
    discharge_current_id = db.Column(db.Integer, db.ForeignKey('current.id'))
    max_discharge_current_id = db.Column(db.Integer, db.ForeignKey('current.id'))


class RealParameters(db.Model):
    __tablename__ = 'real_parameters'
    id = db.Column(db. Integer, primary_key=True, autoincrement=True)
    name_id = db.Column(db.Integer, db.ForeignKey('title.id'))
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)
    capacity_id = db.Column(db.Integer, db.ForeignKey('capacity.id'))
    resistance_id = db.Column(db.Integer, db.ForeignKey('resistance.id'), nullable=False)
    voltage_id = db.Column(db.Integer, db.ForeignKey('voltage.id'), nullable=False)
    weight_id = db.Column(db.Integer, db.ForeignKey('weight.id'))

