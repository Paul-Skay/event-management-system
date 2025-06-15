from datetime import date
from pydantic import BaseModel


class RegistrationBase(BaseModel):
    user_id: int
    event_id: int


class RegistrationCreate(RegistrationBase):
    pass


class RegistrationUpdate(RegistrationBase):
    user_id: int | None = None
    event_id: int | None = None
    attended: bool | None = None
    registration_date: date | None = None


class Registration(RegistrationBase):
    id: str
    registration_date: date = date.today()
    attended: bool = False
