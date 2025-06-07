from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.v1 import agents, avatar, voice, rooms, user
from backend.app.api.v1 import websocket as ws_router

app = FastAPI(title="Avatar IA Backend v2.0")

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://virtual-voice-hub.onrender.com"],  # Permitir todos los orígenes temporalmente
    allow_credentials=True,  # Debe ser False cuando allow_origins=["*"]
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(agents.router, prefix="/agents", tags=["agents"])
app.include_router(avatar.router, prefix="/avatar", tags=["avatar"])
app.include_router(voice.router, prefix="/voice", tags=["voice"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(user.router, prefix="/auth", tags=["auth"])
app.include_router(ws_router.router, prefix="", tags=["websocket"])

@app.get("/")
def root():
    return {"message": "Avatar IA Backend v2.0 running"}
