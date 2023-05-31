from app.extensions import db
from sqlalchemy import ForeignKey


class BatteryData(db.Model):
    __tablename__ = 'battery_data'
    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.Integer, unique=True, nullable=False)
    voltage = db.Column(db.Float, nullable=False)
    resistance = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Barcode "{self.barcode}">'


class BatteryName(db.Model):
    __tablename__ = 'battery_name'
    id = db.Column(db.Integer, primary_key=True)
    battery_id = db.Column(db.Integer, ForeignKey('battery_data.id'), nullable=False)
    battery_name = db.Column(db.String(30))

    def __repr__(self):
        return f'<Name "{self.battery_name}">'


class BatteryColor(db.Model):
    __tablename__ = 'battery_color'
    id = db.Column(db.Integer, primary_key=True)
    battery_id = db.Column(db.Integer, primary_key=True)
    battery_color = db.Column(db.String(12))

    def __repr__(self):
        return f'<Color "{self.battery_color}">'


class BatterySource(db. Model):
    __tablename__ = 'battery_source'
    id = db.Column(db.Integer, primary_key=True)
    battery_id = db.Column(db.Integer, primary_key=True)
    battery_source = db.Column(db.String(30))

    def __repr__(self):
        return f'<Battery source "{self.battery_source}">'