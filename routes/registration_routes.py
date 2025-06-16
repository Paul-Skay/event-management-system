from fastapi import APIRouter, status, Form
from crud.registration_crud import register_crud
from schemas.registration_schema import RegistrationCreate
from services.registration_service import registration_service


router = APIRouter(prefix="/registrations", tags=["registrations"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def register_for_event(registration_data: RegistrationCreate = Form(...)):
    return register_crud.register_user(registration_data)


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_registrations():
    return register_crud.get_all_registrations()


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_registration_by_user_id(user_id: int):
    return register_crud.get_registration_for_user(user_id)


@router.put("/{event_id}/attendance", status_code=status.HTTP_200_OK)
def mark_attendance(user_id: int, event_id: int):
    return registration_service.mark_attendance(user_id, event_id)


@router.get("/attendee/{event_id}", status_code=status.HTTP_200_OK)
def get_attendees_for_an_event(event_id: int):
    return registration_service.get_all_attendance_for_event(event_id)


@router.get("/attendees/all", status_code=status.HTTP_200_OK)
def get_all_attendees():
    return registration_service.get_all_attendees()


@router.get("/attendee/event/users", status_code=status.HTTP_200_OK)
def get_users_who_attended_at_least_one_event():
    return registration_service.get_users_who_attended_at_least_one_event()
