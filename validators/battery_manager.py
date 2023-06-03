import datetime

from pydantic import BaseModel, validator


class MainPage(BaseModel):
    barcode: int
    name: str | None
    color: str
    resistance: float
    voltage: float
    source: str | None

    @validator('barcode')
    def validate_barcode(cls, barcode):
        if len(str(barcode)) != 6:
            raise ValueError('Barcode must be a 6-digit number')
        return barcode

    @validator('color')
    def validate_color(cls, color):
        if not color:
            raise ValueError('Color is required')
        return color

    @validator('voltage', 'resistance')
    def validate_positive_value(cls, value):
        if value <= 0:
            raise ValueError('Value must be a positive number')
        return value



