import os
from livekit import api
from app.core.config import settings

LIVEKIT_API_KEY = settings.LIVEKIT_API_KEY
LIVEKIT_API_SECRET = settings.LIVEKIT_API_SECRET
LIVEKIT_URL = settings.LIVEKIT_URL

def create_room(room_name):
    """Crea una sala en LiveKit"""
    try:
        room_service = api.RoomServiceClient(
            LIVEKIT_URL, 
            api_key=LIVEKIT_API_KEY, 
            api_secret=LIVEKIT_API_SECRET
        )
        return room_service.create_room(room_name)
    except Exception as e:
        print(f"Error creating room: {e}")
        return None

def create_token(room_name, participant_name, permissions=None):
    """Crea un token JWT para un participante"""
    try:
        token = api.AccessToken(
            api_key=LIVEKIT_API_KEY,
            api_secret=LIVEKIT_API_SECRET
        )
        token.add_grant(
            room_name=room_name,
            participant_name=participant_name,
            permissions=permissions or {
                "can_publish": True,
                "can_subscribe": True,
                "can_publish_data": True
            }
        )
        return token.to_jwt()
    except Exception as e:
        print(f"Error creating token: {e}")
        return None
