import os
import jwt
import time
import logging
from backend.app.core.config import settings

logger = logging.getLogger(__name__)

# Obtener credenciales de LiveKit
LIVEKIT_API_KEY = settings.LIVEKIT_API_KEY
LIVEKIT_API_SECRET = settings.LIVEKIT_API_SECRET
LIVEKIT_URL = settings.LIVEKIT_URL

# Verificar si tenemos credenciales válidas
has_valid_credentials = bool(LIVEKIT_API_KEY and LIVEKIT_API_SECRET and LIVEKIT_URL)
if not has_valid_credentials:
    logger.warning("Credenciales de LiveKit no disponibles o incompletas. Usando modo simulado.")
else:
    logger.info(f"Usando LiveKit URL: {LIVEKIT_URL}")

def create_room(room_name):
    """
    Simulación de creación de sala en LiveKit.
    En una implementación real, se usaría la API HTTP de LiveKit.
    """
    try:
        # En una implementación real, aquí se haría una llamada HTTP a la API de LiveKit
        # Por ahora, simplemente devolvemos un objeto simulado
        room_id = f"RM_{room_name}_{int(time.time())}"
        logger.info(f"Creando sala simulada: {room_name} (ID: {room_id})")
        return {
            "name": room_name,
            "sid": room_id,
            "empty_timeout": 300,
            "created_at": int(time.time())
        }
    except Exception as e:
        logger.error(f"Error creating room: {str(e)}")
        return None

def create_token(room_name, participant_name, permissions=None):
    """Crea un token JWT para un participante usando PyJWT"""
    try:
        if not permissions:
            permissions = {
                "can_publish": True,
                "can_subscribe": True,
                "can_publish_data": True
            }
        
        # Si no tenemos credenciales válidas, devolver un token simulado
        if not has_valid_credentials:
            logger.warning(f"Generando token simulado para {participant_name} en sala {room_name}")
            return f"mock-token-{room_name}-{participant_name}-{int(time.time())}"
        
        # Crear el payload del token
        now = int(time.time())
        payload = {
            "iss": LIVEKIT_API_KEY,
            "nbf": now,
            "exp": now + 86400,  # 24 horas
            "sub": participant_name,
            "video": {
                "room": room_name,
                "room_join": True,
                "can_publish": permissions.get("can_publish", True),
                "can_subscribe": permissions.get("can_subscribe", True),
                "can_publish_data": permissions.get("can_publish_data", True)
            }
        }
        
        # Firmar el token con el secreto
        token = jwt.encode(payload, LIVEKIT_API_SECRET, algorithm="HS256")
        logger.info(f"Token generado para {participant_name} en sala {room_name}")
        return token
    except Exception as e:
        logger.error(f"Error creating token: {str(e)}")
        return f"error-token-{room_name}-{participant_name}"
