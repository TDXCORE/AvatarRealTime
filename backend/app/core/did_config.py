from pydantic import BaseSettings
from typing import Optional

class DIDSettings(BaseSettings):
    API_KEY: str
    BASE_URL: str = "https://api.d-id.com"
    DEFAULT_RESOLUTION: int = 720
    SESSION_TIMEOUT: int = 300
    WARMUP_ENABLED: bool = True
    MAX_RETRIES: int = 3
    RETRY_DELAY: int = 1
    DEFAULT_AGENT_ID: str = "custom"
    AUDIO_SAMPLE_RATE: int = 16000
    AUDIO_CHUNK_SIZE: int = 1024

    class Config:
        env_prefix = "DID_"

did_settings = DIDSettings() 