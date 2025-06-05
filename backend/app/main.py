from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.v1 import agents, avatar, voice, livekit_webhooks, rooms, user

app = FastAPI(title="Avatar IA Backend v2.0")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://virtual-voice-hub.onrender.com"],  # Origen específico en lugar de "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agents.router, prefix="/agents", tags=["agents"])
app.include_router(avatar.router, prefix="/avatar", tags=["avatar"])
app.include_router(voice.router, prefix="/voice", tags=["voice"])
app.include_router(livekit_webhooks.router, prefix="/livekit", tags=["livekit"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(user.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "Avatar IA Backend v2.0 running"}
