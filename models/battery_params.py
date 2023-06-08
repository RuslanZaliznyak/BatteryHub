from app.extensions import db


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


class BatteryCapacity(db.Model):
    __tablename__ = 'battery_capacity'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    capacity = db.Column(db.Float,
                         unique=True,
                         nullable=False)


class BatteryCurrent(db. Model):
    __tablename__ = 'battery_current'
    id = db.Column(db. Integer,
                   primary_key=True,
                   autoincrement=True)
    current = db.Column(db. Float)


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



