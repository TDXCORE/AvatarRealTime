from fastapi import WebSocket
from app.services.audio_service import transcribe_audio_bytes
from app.services.agentic_service import ask_llm
from app.services.tts_service import synthesize_voice
from app.services.did_service import DIDService

class WebSocketManager:
    def __init__(self):
        self.did_service = DIDService()
        self.connections = {}
        self.stream_ids = {}

    async def connect(self, websocket: WebSocket, session_id: str):
        await websocket.accept()
        self.connections[session_id] = websocket
        stream = await self.did_service.create_stream(session_id)
        self.stream_ids[session_id] = stream.get("id") or stream.get("stream_id")
        return stream

    async def disconnect(self, session_id: str):
        self.connections.pop(session_id, None)
        self.stream_ids.pop(session_id, None)

    async def process_audio(self, session_id: str, audio_data: bytes):
        text = transcribe_audio_bytes(audio_data)
        response = await ask_llm(text)
        tts_audio = synthesize_voice(response)
        stream_id = self.stream_ids.get(session_id)
        if stream_id:
            await self.did_service.send_audio(stream_id, tts_audio)
        await self.connections[session_id].send_json({"text": response}) 