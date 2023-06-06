from app.extensions import db


class BatteryData(db.Model):
    __tablename__ = 'battery_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barcode = db.Column(db.Integer, unique=True, nullable=False)
    name_id = db.Column(db.Integer, db.ForeignKey('battery_name.id'), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('battery_color.id'), nullable=False)
    voltage_id = db.Column(db.Integer, db.ForeignKey('battery_voltage.id'), nullable=False)
    resistance_id = db.Column(db.Integer, db.ForeignKey('battery_resistance.id'), nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey('battery_source.id'), nullable=False)
    photo_id = db.Column(db.Integer, db.ForeignKey('battery_photo.id'), nullable=False)
    capacity_id = db.Column(db.Integer, db.ForeignKey('battery_capacity.id'))
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Barcode "{self.barcode}">'


class BatteryName(db.Model):
    __tablename__ = 'battery_name'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     unique=True,
                     nullable=False)

    def __repr__(self):
        return f'<Name "{self.battery_name}">'


class BatteryColor(db.Model):
    __tablename__ = 'battery_color'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    color = db.Column(db.String(20),
                      unique=True,
                      nullable=False)

    def __repr__(self):
        return f'<Color "{self.battery_color}">'


class BatterySource(db.Model):
    __tablename__ = 'battery_source'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    source = db.Column(db.String(50),
                       unique=True,
                       nullable=False)

    def __repr__(self):
        return f'<Battery source "{self.battery_source}">'


class BatteryVoltage(db.Model):
    __tablename__ = 'battery_voltage'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    voltage = db.Column(db.Float,
                        unique=True,
                        nullable=False)

    def __repr__(self):
        return f'Battery voltage  "{self.battery_voltage}"'


class BatteryResistance(db.Model):
    __tablename__ = 'battery_resistance'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    resistance = db.Column(db.Float,
                           unique=True,
                           nullable=False)

    def __repr__(self):
        return f'Battery resistance "{self.battery_resistance}"'


class BatteryPhoto(db.Model):
    __tablename__ = 'battery_photo'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    battery_photo = db.Column(db.LargeBinary)


class BatteryCapacity(db.Model):
    __tablename__ = 'battery_capacity'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    capacity = db.Column(db.Float,
                         unique=True,
                         nullable=False)
