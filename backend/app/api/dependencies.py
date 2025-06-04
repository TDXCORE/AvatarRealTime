# Aquí irán las dependencias de autenticación y validación 

from fastapi import Depends, HTTPException, status

def get_current_user():
    # Mock de usuario autenticado
    return {"id": 1, "username": "demo_user"} 