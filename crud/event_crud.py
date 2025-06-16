from fastapi import HTTPException, status
from models import Event
from database import events_db
from schemas.event_schema import EventCreate, EventUpdate


# CRUD operations for Event management
class EventCrud:

    @staticmethod
    def create_event(event_data: EventCreate):
        # Check if event exists
        for existing_event in events_db.values():
            if existing_event.title == event_data.title:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Event with this title already exists"
                )
        event_id = len(events_db) + 1
        new_event = Event(id=event_id, **event_data.model_dump())
        events_db[event_id] = new_event
        return {"message": "Event created successfully", "event": new_event}

    @staticmethod
    def get_event_by_id(id: int):
        if id not in events_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        return events_db[id]

    @staticmethod
    def get_all_events():
        return {"events": list(events_db.values())}

    @staticmethod
    def update_event(id: int, event: EventUpdate):
        update_event = events_db.get(id)
        if not update_event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Event with id {id} not found"
            )
        for field, value in event.model_dump(exclude_unset=True).items():
            setattr(update_event, field, value)
        return {"detail": "Event updated successfully", "Event": update_event}

    @staticmethod
    def delete_event(id: int):
        if id not in events_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        del events_db[id]
        return {"message": "Event deleted successfully"}


event_crud = EventCrud()
