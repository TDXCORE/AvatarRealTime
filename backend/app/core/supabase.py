import logging
from supabase import create_client, Client
from backend.app.core.config import settings

logger = logging.getLogger(__name__)

# Crear un cliente mock para desarrollo/pruebas cuando no hay credenciales
class MockSupabaseClient:
    def __init__(self):
        self.auth = MockAuth()
        self.storage = MockStorage()
        self._tables = {}
        logger.warning("Usando cliente Supabase simulado para desarrollo/pruebas")
    
    def table(self, name):
        if name not in self._tables:
            self._tables[name] = MockTable(name)
        return self._tables[name]

class MockAuth:
    def sign_up(self, credentials):
        return {"user": {"id": "mock-user-id"}, "session": {"access_token": "mock-token"}}
    
    def sign_in_with_password(self, credentials):
        return {"user": {"id": "mock-user-id"}, "session": {"access_token": "mock-token"}}

class MockStorage:
    def from_(self, bucket):
        return MockBucket(bucket)

class MockBucket:
    def __init__(self, name):
        self.name = name
    
    def upload(self, path, data, upsert=False):
        return {"path": path}
    
    def list(self, path):
        return {"data": []}
    
    def get_public_url(self, path):
        return {"publicURL": f"https://example.com/{path}"}

class MockTable:
    def __init__(self, name):
        self.name = name
        self._filters = []
    
    def select(self, *args):
        return self
    
    def insert(self, data):
        return self
    
    def update(self, data):
        return self
    
    def eq(self, field, value):
        return self
    
    def single(self):
        return self
    
    def execute(self):
        if "users" in self.name:
            return {"data": {"id": "mock-user-id", "email": "user@example.com", "username": "mock_user"}}
        return {"data": []}

# Intentar crear el cliente real, con fallback al mock si no hay credenciales
try:
    if not settings.SUPABASE_URL or not (settings.SUPABASE_SERVICE_ROLE or settings.SUPABASE_ANON_KEY):
        raise ValueError("Faltan credenciales de Supabase")
    
    supabase: Client = create_client(
        settings.SUPABASE_URL, 
        settings.SUPABASE_SERVICE_ROLE or settings.SUPABASE_ANON_KEY
    )
    logger.info("Cliente Supabase inicializado correctamente")
except Exception as e:
    logger.warning(f"Error al inicializar Supabase: {str(e)}")
    supabase = MockSupabaseClient()
