from fastapi import FastAPI
from routes import event, registration, speaker, user
from services.speaker import speaker_service


app = FastAPI(title="Event Management API System")

app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(event.router, prefix="/event", tags=["event"])
app.include_router(registration.router, prefix="/register", tags=["register"])
app.include_router(speaker.router, prefix="/speaker", tags=["speaker"])


@app.get("/")
async def home():
    return {
        "message": "Welcome to the Event Management API",
        "version": "1.0",
        "speakers": speaker_service.preload_speakers()
    }
speaker_service.preload_speakers()
