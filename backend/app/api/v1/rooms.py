from fastapi import APIRouter, Body, Depends, HTTPException
from backend.app.api.dependencies import get_current_user

router = APIRouter()

# El endpoint de creación de sala ya no es necesario, pero si quieres mantenerlo para lógica futura, puedes dejarlo vacío o con un mensaje deprecado.
@router.post("/create")
async def create_room(room_name: str = Body(..., embed=True), user=Depends(get_current_user)):
    return {"message": "LiveKit integration deprecated. Use D-ID streaming."}

@router.get("/profile")
def get_user_profile(user=Depends(get_current_user)):
    # Devuelve el perfil del usuario autenticado
    return {"profile": user}
