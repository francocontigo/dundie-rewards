from pydantic import BaseModel, field_validator
from decimal import Decimal
from datetime import datetime
from dundie.utils.email import check_valid_email


class InvalideEmailError(Exception): ...


class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str

    @field_validator("pk")
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise InvalideEmailError(f"Invalid email for {v!r}")
        return v

    def __str__(self):
        return f"{self.name} - {self.role}"


class Balance(BaseModel):
    person: Person
    value: Decimal

    @field_validator("value", mode="before")
    def value_logic(cls, v):
        return Decimal(v) * 2

    class Config:
        json_encoders = {Person: lambda p: p.name}


class Movement(BaseModel):
    person: Person
    date: datetime
    actor: str
    value: Decimal


import json
from dundie.database import connect

db = connect()

for pk, data in db["people"].items():
    p = Person(pk=pk, **data)

print(p)
print(json.dumps(p.model_dump()))
