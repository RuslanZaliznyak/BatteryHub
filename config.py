import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pabxy6-rIqtow-hisbum@localhost:3306/BatteryHub'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


