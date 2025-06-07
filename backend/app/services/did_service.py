import httpx
import os

class DIDService:
    def __init__(self):
        self.api_key = os.getenv("DID_API_KEY")
        self.base_url = "https://api.d-id.com"
        self.headers = {"Authorization": f"Basic {self.api_key}"}

    async def create_stream(self, session_id: str):
        async with httpx.AsyncClient() as client:
            r = await client.post(
                f"{self.base_url}/agents/streams",
                headers=self.headers,
                json={"agent_id": "custom", "session_id": session_id}
            )
            return r.json()

    async def send_audio(self, stream_id: str, audio_data: bytes):
        async with httpx.AsyncClient() as client:
            r = await client.post(
                f"{self.base_url}/agents/streams/{stream_id}/audio",
                headers=self.headers,
                files={"audio": audio_data}
            )
            return r.json() 