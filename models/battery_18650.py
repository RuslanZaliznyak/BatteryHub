from app.extensions import db


class BatteryData(db.Model):
    __tablename__ = 'battery_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barcode = db.Column(db.Integer, unique=True, nullable=False)
    name_id = db.Column(db.Integer, db.ForeignKey('battery_name.id'))
    color_id = db.Column(db. Integer, db.ForeignKey('battery_color.id'))
    voltage_id = db.Column(db.Integer, db.ForeignKey('battery_voltage.id'))
    resistance_id = db.Column(db.Integer, db.ForeignKey('battery_resistance.id'))
    battery_source_id = db.Column(db. Integer, db.ForeignKey('battery_source.id'))
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Barcode "{self.barcode}">'


class BatteryName(db.Model):
    __tablename__ = 'battery_name'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    battery_name = db.Column(db.String(30))

    def __repr__(self):
        return f'<Name "{self.battery_name}">'


class BatteryColor(db.Model):
    __tablename__ = 'battery_color'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    battery_color = db.Column(db.String(12))

    def __repr__(self):
        return f'<Color "{self.battery_color}">'


class BatterySource(db.Model):
    __tablename__ = 'battery_source'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    battery_source = db.Column(db.String(30))

    def __repr__(self):
        return f'<Battery source "{self.battery_source}">'


class BatteryVoltage(db.Model):
    __tablename__ = 'battery_voltage'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    battery_voltage = db.Column(db.Float)

    def __repr__(self):
        return f'Battery voltage  "{self.battery_voltage}"'


class BatteryResistance(db.Model):
    __tablename__ = 'battery_resistance'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    battery_resistance = db.Column(db.Float)

    def __repr__(self):
        return f'Battery resistance "{self.battery_resistance}"'
