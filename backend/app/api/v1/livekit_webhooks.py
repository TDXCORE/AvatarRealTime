from fastapi import APIRouter, Request, Depends, HTTPException
from backend.app.services.livekit_service import handle_webhook_event
from backend.app.api.dependencies import get_current_user

router = APIRouter()

@router.post("/webhook")
async def livekit_webhook(request: Request):
    try:
        data = await request.json()
        result = await handle_webhook_event(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
