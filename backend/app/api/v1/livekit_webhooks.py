from fastapi import APIRouter, Request

router = APIRouter()

# Aquí irán los endpoints de webhooks de LiveKit 

@router.post("/webhook")
async def livekit_webhook(request: Request):
    data = await request.json()
    # Aquí se procesarán los eventos de LiveKit
    return {"received": data} 