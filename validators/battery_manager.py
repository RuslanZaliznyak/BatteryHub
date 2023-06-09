from pydantic import BaseModel
import datetime


class MainPage(BaseModel):
    """
    HTML validator of the form for adding a new battery
    """
    barcode: int
    name: None | str
    color: str
    resistance: float
    voltage: float
    source: str | None
    capacity: None | float
    weight: None | float
    timestamp: None | datetime.datetime





