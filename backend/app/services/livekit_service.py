from backend.app.core.livekit_client import create_room, create_token

async def create_livekit_room(room_name):
    """Crea una sala en LiveKit"""
    return create_room(room_name)

async def generate_participant_token(room_name, participant_name, permissions=None):
    """Genera un token para un participante"""
    return create_token(room_name, participant_name, permissions)

async def handle_webhook_event(event_data):
    """Procesa eventos de webhook de LiveKit"""
    event_type = event_data.get("event")
    if not event_type:
        return {"error": "Invalid event data"}
    
    # Aquí procesaríamos diferentes tipos de eventos
    if event_type == "participant_joined":
        # Lógica para cuando un participante se une
        pass
    elif event_type == "participant_left":
        # Lógica para cuando un participante se va
        pass
    elif event_type == "track_published":
        # Lógica para cuando se publica un track
        pass
    
    return {"processed": True, "event_type": event_type}
