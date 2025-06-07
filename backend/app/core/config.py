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

class Settings:
    # Usar valores por defecto solo en desarrollo
    is_development = os.getenv("ENVIRONMENT", "development") == "development"
    
    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_SERVICE_ROLE: str = os.getenv("SUPABASE_SERVICE_ROLE", "")
    SUPABASE_ANON_KEY: str = os.getenv("SUPABASE_ANON_KEY", "")
    
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

settings = Settings()
