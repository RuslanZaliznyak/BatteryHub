import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    This class contains the basic configuration of the SQLAlchemy ORM database
    """
    # Connected to database
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:pabxy6-rIqtow-hisbum@localhost:3306/BatteryHubAlpha'
    # Track any changes in database models
    # True - tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = True


