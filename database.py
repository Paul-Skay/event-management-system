from models import User, Event, Speaker, Registration

users_db: dict[int, User] = {}
events_db: dict[int, Event] = {}
registrations_db: dict[int, Registration] = {}
speakers_db: dict[int, Speaker] = {
    1: Speaker(id=1, name="John Doe", topic="Expert in Python"),
    2: Speaker(id=2, name="Jane Smith", topic="AI Enthusiast")
}
