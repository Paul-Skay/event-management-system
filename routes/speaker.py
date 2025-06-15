from fastapi import APIRouter, status
from services.speaker import speaker_service


router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def view_all_speakers():
    return speaker_service.preload_speakers()
