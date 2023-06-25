from pydantic import BaseModel, Field, root_validator


class Form(BaseModel):
    name: str = Field(default=None, description='Name', max_length=50)
    color: str = Field(description='Color', max_length=50)
    voltage: float = Field(default='', description='Voltage')
    resistance: float = Field(default='', description='Resistance')
    source: str = Field(default=None, description='Source', max_length=50)
    weight: float | str | None
    capacity: float | str | None

    @root_validator(pre=True)
    def convert_empty_strings(cls, values):
        for key, value in values.items():
            if isinstance(value, str) and value == '':
                values[key] = None
        return values