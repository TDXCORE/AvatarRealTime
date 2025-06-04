from fastapi import APIRouter, Body, Depends
from app.api.dependencies import get_current_user

router = APIRouter()

# Aquí irán los endpoints de voz 

@router.post("/synthesize")
def synthesize_voice(text: str = Body(..., embed=True), user=Depends(get_current_user)):
    # Aquí se integrará Coqui TTS/XTTS-v2
    return {"audio_url": f"/mock/audio/{text}", "user": user} 