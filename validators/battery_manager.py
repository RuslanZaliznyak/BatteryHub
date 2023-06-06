from pydantic import BaseModel, validator
import datetime


class MainPage(BaseModel):
    barcode: int
    name: str | None
    color: str
    resistance: float
    voltage: float
    source: str | None
    timestamp: None | datetime.datetime
    last_voltage: None | float
    last_charge_date: None | datetime.datetime
    last_resistance: None | float
    last_resistance_date: None | datetime.datetime



