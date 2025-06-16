from typing import Optional
from pydantic import BaseModel
from datetime import date


class EventBase(BaseModel):
    title: str
    location: str
    event_date: date = date.today()


class EventCreate(EventBase):
    is_open: bool = True


class EventUpdate(EventBase):
    title: Optional[str] = None
    event_date: Optional[date] = None
    location: Optional[str] = None
    is_open:  Optional[bool] = None


class Event(EventBase):
    id: int
