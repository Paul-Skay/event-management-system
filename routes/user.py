from fastapi import APIRouter, status, Form
from schemas.user import UserCreate, UserUpdate
from services.user import user_service
from crud.user import user_crud

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate = Form(...)):
    return user_crud.create_user(user_data)


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_users():
    return user_crud.get_all_users()


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user_by_id(user_id: int):
    return user_crud.get_user_by_id(user_id)


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_data: UserUpdate = Form(...)):
    return user_crud.update_user(user_id, user_data)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    return user_crud.delete_user(user_id)


@router.patch("/{user_id}/deactivate", status_code=status.HTTP_200_OK)
def deactivate_user(user_id: int):
    return user_service.deactivate_user(user_id)
