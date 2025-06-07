from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.websocket_manager import WebSocketManager

router = APIRouter()
manager = WebSocketManager()

@router.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await manager.connect(websocket, session_id)
    try:
        while True:
            audio_data = await websocket.receive_bytes()
            await manager.process_audio(session_id, audio_data)
    except WebSocketDisconnect:
        await manager.disconnect(session_id) 