import os
from dotenv import load_dotenv
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Intentar cargar variables de entorno desde .env.local en desarrollo
env_file_path = os.path.join(os.path.dirname(__file__), '../../.env.local')
if os.path.exists(env_file_path):
    logger.info(f"Cargando variables de entorno desde {env_file_path}")
    load_dotenv(dotenv_path=env_file_path)
else:
    logger.info("No se encontró archivo .env.local, usando variables de entorno del sistema")

# Valores por defecto para desarrollo local
DEFAULT_SUPABASE_URL = "https://example.supabase.co"
DEFAULT_SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.example"
DEFAULT_LIVEKIT_URL = "wss://example.livekit.cloud"
DEFAULT_LIVEKIT_API_KEY = "APIKey"
DEFAULT_LIVEKIT_API_SECRET = "APISecret"

class Settings:
    # Usar valores por defecto solo en desarrollo
    is_development = os.getenv("ENVIRONMENT", "development") == "development"
    
    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", DEFAULT_SUPABASE_URL if is_development else "")
    SUPABASE_SERVICE_ROLE: str = os.getenv("SUPABASE_SERVICE_ROLE", DEFAULT_SUPABASE_KEY if is_development else "")
    SUPABASE_ANON_KEY: str = os.getenv("SUPABASE_ANON_KEY", DEFAULT_SUPABASE_KEY if is_development else "")
    
    # LiveKit
    LIVEKIT_URL: str = os.getenv("LIVEKIT_URL", DEFAULT_LIVEKIT_URL if is_development else "")
    LIVEKIT_API_KEY: str = os.getenv("LIVEKIT_API_KEY", DEFAULT_LIVEKIT_API_KEY if is_development else "")
    LIVEKIT_API_SECRET: str = os.getenv("LIVEKIT_API_SECRET", DEFAULT_LIVEKIT_API_SECRET if is_development else "")
    
    # Otros
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    REDIS_URL: str = os.getenv("REDIS_URL", "")
    
    def __init__(self):
        # Registrar valores de configuración (sin mostrar claves completas por seguridad)
        logger.info(f"SUPABASE_URL: {self.SUPABASE_URL}")
        if self.SUPABASE_SERVICE_ROLE:
            logger.info(f"SUPABASE_SERVICE_ROLE: {'*' * (len(self.SUPABASE_SERVICE_ROLE) - 4) + self.SUPABASE_SERVICE_ROLE[-4:]}")
        if self.SUPABASE_ANON_KEY:
            logger.info(f"SUPABASE_ANON_KEY: {'*' * (len(self.SUPABASE_ANON_KEY) - 4) + self.SUPABASE_ANON_KEY[-4:]}")
        logger.info(f"LIVEKIT_URL: {self.LIVEKIT_URL}")

settings = Settings()
