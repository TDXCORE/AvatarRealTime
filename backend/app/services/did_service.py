import httpx
import asyncio
import logging
from typing import Optional, Dict, Any
from app.core.did_config import did_settings

logger = logging.getLogger(__name__)

class DIDService:
    def __init__(self):
        self.api_key = did_settings.API_KEY
        self.base_url = did_settings.BASE_URL
        self.headers = {
            "Authorization": f"Basic {self.api_key}",
            "Content-Type": "application/json"
        }

    async def create_stream(self, session_id: str, config: Optional[Dict[str, Any]] = None) -> Dict:
        default_config = {
            "agent_id": did_settings.DEFAULT_AGENT_ID,
            "session_id": session_id,
            "session_timeout": did_settings.SESSION_TIMEOUT,
            "output_resolution": did_settings.DEFAULT_RESOLUTION,
            "warmup": did_settings.WARMUP_ENABLED
        }
        config = {**default_config, **(config or {})}
        for attempt in range(did_settings.MAX_RETRIES):
            try:
                async with httpx.AsyncClient() as client:
                    r = await client.post(
                        f"{self.base_url}/agents/streams",
                        headers=self.headers,
                        json=config
                    )
                    r.raise_for_status()
                    return r.json()
            except Exception as e:
                if attempt == did_settings.MAX_RETRIES - 1:
                    raise
                await asyncio.sleep(did_settings.RETRY_DELAY)

    async def send_audio(self, stream_id: str, audio_data: bytes) -> Dict:
        for attempt in range(did_settings.MAX_RETRIES):
            try:
                async with httpx.AsyncClient() as client:
                    r = await client.post(
                        f"{self.base_url}/agents/streams/{stream_id}/audio",
                        headers=self.headers,
                        files={"audio": audio_data}
                    )
                    r.raise_for_status()
                    return r.json()
            except Exception as e:
                if attempt == did_settings.MAX_RETRIES - 1:
                    raise
                await asyncio.sleep(did_settings.RETRY_DELAY)

    async def close_stream(self, stream_id: str) -> Dict:
        async with httpx.AsyncClient() as client:
            r = await client.delete(
                f"{self.base_url}/agents/streams/{stream_id}",
                headers=self.headers
            )
            r.raise_for_status()
            return r.json()

    async def get_stream_status(self, stream_id: str) -> Dict:
        async with httpx.AsyncClient() as client:
            r = await client.get(
                f"{self.base_url}/agents/streams/{stream_id}",
                headers=self.headers
            )
            r.raise_for_status()
            return r.json() 