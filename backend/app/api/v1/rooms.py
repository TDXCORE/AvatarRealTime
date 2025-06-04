from fastapi import APIRouter, Body, Depends
from app.api.dependencies import get_current_user

router = APIRouter()

# Aquí irán los endpoints de gestión de salas 

@router.post("/token")
def generate_livekit_token(identity: str = Body(..., embed=True), user=Depends(get_current_user)):
    # Aquí se generará el token JWT usando la API Key/Secret de LiveKit
    return {"token": f"mock-token-for-{identity}", "user": user}

@router.get("/profile")
def get_user_profile(user=Depends(get_current_user)):
    # Devuelve el perfil del usuario autenticado
    return {"profile": user} 