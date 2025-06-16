from database import speakers_db
from models import Speaker


class SpeakerService:
    @staticmethod
    def preload_speakers():
        if not speakers_db:
            speakers_db[1] = Speaker(
                id=1,
                name="John Doe",
                topic="Expert in Python"
            )
            speakers_db[2] = Speaker(
                id=2,
                name="Jane Smith",
                topic="AI Enthusiast"
            )
        return speakers_db


speaker_service = SpeakerService()
