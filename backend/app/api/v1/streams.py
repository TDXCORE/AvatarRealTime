from fastapi import APIRouter, HTTPException, Depends
from app.services.did_service import DIDService
from app.api.dependencies import get_current_user

router = APIRouter()
did_service = DIDService()

@router.post("/streams/{stream_id}/close")
async def close_stream(
    stream_id: str,
    user = Depends(get_current_user)
):
    try:
        result = await did_service.close_stream(stream_id)
        return {"status": "success", "data": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/streams/{stream_id}/status")
async def get_stream_status(
    stream_id: str,
    user = Depends(get_current_user)
):
    try:
        status = await did_service.get_stream_status(stream_id)
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 