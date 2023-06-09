from sqlalchemy import DECIMAL

from app.extensions import db


class Title(db.Model):
    __tablename__ = 'title'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     unique=True,
                     nullable=False)

    def __repr__(self):
        return f'<Name "{self.name}">'


class Color(db.Model):
    __tablename__ = 'color'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    color = db.Column(db.String(20),
                      unique=True,
                      nullable=False)

    def __repr__(self):
        return f'<Color "{self.color}">'


class Capacity(db.Model):
    __tablename__ = 'capacity'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    capacity = db.Column(db.Float,
                         unique=True,
                         nullable=False)


class Current(db.Model):
    __tablename__ = 'current'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    current = db.Column(DECIMAL(precision=3, scale=2),
                        unique=True
                        )


class Source(db.Model):
    __tablename__ = 'source'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    source = db.Column(db.String(50),
                       unique=True,
                       nullable=False)

    def __repr__(self):
        return f'<Battery source "{self.source}">'


class Voltage(db.Model):
    __tablename__ = 'voltage'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    voltage = db.Column(DECIMAL(precision=3, scale=2),
                        unique=True,
                        nullable=False
                        )

    def __repr__(self):
        return f'Battery voltage  "{self.voltage}"'


class Resistance(db.Model):
    __tablename__ = 'resistance'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    resistance = db.Column(DECIMAL(precision=4, scale=2),
                           unique=True,
                           nullable=False
                           )

    def __repr__(self):
        return f'Battery resistance "{self.resistance}"'


class Photo(db.Model):
    __tablename__ = 'photo'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    photo = db.Column(db.LargeBinary)


class Weight(db.Model):
    __tablename__ = 'weight'
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    weight = db.Column(DECIMAL(precision=4, scale=3),
                       unique=True,
                       nullable=False
                       )
