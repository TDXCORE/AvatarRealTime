from fastapi import WebSocket
import logging
from typing import Dict
from app.services.audio_service import transcribe_audio_bytes
from app.services.agentic_service import ask_llm
from app.services.tts_service import synthesize_voice
from app.services.did_service import DIDService
from app.core.did_config import did_settings

logger = logging.getLogger(__name__)

class WebSocketManager:
    def __init__(self):
        self.did_service = DIDService()
        self.connections: Dict[str, WebSocket] = {}
        self.stream_ids: Dict[str, str] = {}
        self.session_timeouts: Dict[str, int] = {}

    async def connect(self, websocket: WebSocket, session_id: str) -> Dict:
        await websocket.accept()
        self.connections[session_id] = websocket
        try:
            stream = await self.did_service.create_stream(session_id)
            self.stream_ids[session_id] = stream.get("id")
            return stream
        except Exception as e:
            logger.error(f"Error creating stream: {str(e)}")
            await websocket.close()
            raise

    async def disconnect(self, session_id: str):
        try:
            self.connections.pop(session_id, None)
            stream_id = self.stream_ids.pop(session_id, None)
            if stream_id:
                await self.did_service.close_stream(stream_id)
        except Exception as e:
            logger.error(f"Error in disconnect: {str(e)}")

    async def process_audio(self, session_id: str, audio_data: bytes):
        try:
            text = transcribe_audio_bytes(audio_data)
            response = await ask_llm(text)
            tts_audio = synthesize_voice(response)
            stream_id = self.stream_ids.get(session_id)
            if not stream_id:
                raise Exception("Stream ID not found")
            await self.did_service.send_audio(stream_id, tts_audio)
            await self.connections[session_id].send_json({
                "type": "response",
                "text": response,
                "status": "success"
            })
        except Exception as e:
            logger.error(f"Error processing audio: {str(e)}")
            await self.connections[session_id].send_json({
                "type": "error",
                "message": str(e)
            }) 