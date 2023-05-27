from app.extensions import db


class Battery(db.Model):
    __tablename__ = 'battery_18650'
    batteryId = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.Integer, unique=True, nullable=False)
    title = db.Column(db.String(50))
    color = db.Column(db.String(15))
    voltage = db.Column(db.Float, nullable=False)
    resistance = db.Column(db.Float, nullable=False)
    battery_source = db.Column(db.String(50))
    datetime = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Barcode "{self.barcode}">'