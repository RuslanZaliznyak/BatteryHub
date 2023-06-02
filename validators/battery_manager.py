from pydantic import BaseModel


class MainPage(BaseModel):
    barcode = int
    color = str
    name = str
    source = str
    resistance = float
    voltage = float


