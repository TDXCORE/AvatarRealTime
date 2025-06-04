import os
import jwt
import time
from backend.app.core.config import settings

LIVEKIT_API_KEY = settings.LIVEKIT_API_KEY
LIVEKIT_API_SECRET = settings.LIVEKIT_API_SECRET
LIVEKIT_URL = settings.LIVEKIT_URL

def create_room(room_name):
    """
    Simulación de creación de sala en LiveKit.
    En una implementación real, se usaría la API HTTP de LiveKit.
    """
    try:
        # En una implementación real, aquí se haría una llamada HTTP a la API de LiveKit
        # Por ahora, simplemente devolvemos un objeto simulado
        return {
            "name": room_name,
            "sid": f"RM_{room_name}_{int(time.time())}",
            "empty_timeout": 300,
            "created_at": int(time.time())
        }
    except Exception as e:
        print(f"Error creating room: {e}")
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
        return token
    except Exception as e:
        print(f"Error creating token: {e}")
        return None
