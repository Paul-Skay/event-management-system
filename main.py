from fastapi import FastAPI
from routes import (
    event_routes,
    registration_routes,
    speaker_routes,
    user_routes,
)
from services.speaker_service import speaker_service


app = FastAPI(
    title="Event Management API System",
    description="API for managing events, registrations, and speakers"
)

app.include_router(user_routes.router)
app.include_router(event_routes.router)
app.include_router(registration_routes.router)
app.include_router(speaker_routes.router)


@app.get("/")
async def home():
    return {
        "message": "Welcome to the Event Management API",
        "version": "1.0.0",
        "speakers": speaker_service.preload_speakers()
    }
speaker_service.preload_speakers()
