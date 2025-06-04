from fastapi import APIRouter, Body, Depends, HTTPException
from backend.app.api.dependencies import get_current_user
from backend.app.services.livekit_service import create_livekit_room, generate_participant_token

router = APIRouter()

@router.post("/create")
async def create_room(room_name: str = Body(..., embed=True), user=Depends(get_current_user)):
    """Crea una nueva sala en LiveKit"""
    result = await create_livekit_room(room_name)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to create room")
    return {"room": result, "created_by": user["id"]}

@router.post("/token")
async def generate_livekit_token(
    room_name: str = Body(...), 
    identity: str = Body(...), 
    user=Depends(get_current_user)
):
    """Genera un token JWT para un participante"""
    token = await generate_participant_token(room_name, identity)
    if not token:
        raise HTTPException(status_code=500, detail="Failed to generate token")
    return {"token": token, "room": room_name, "identity": identity}

@router.get("/profile")
def get_user_profile(user=Depends(get_current_user)):
    # Devuelve el perfil del usuario autenticado
    return {"profile": user}
