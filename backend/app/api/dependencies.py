# Aquí irán las dependencias de autenticación y validación 

from fastapi import Depends, HTTPException, status, Header

def get_current_user(authorization: str = Header(None)):
    # Mock de usuario autenticado
    # Acepta cualquier token, incluyendo el 'Bearer mock-token' que enviamos desde el frontend
    if authorization is None:
        # Si no hay token, aún devolvemos un usuario de prueba para facilitar el desarrollo
        print("Advertencia: No se proporcionó token de autorización")
    else:
        print(f"Token recibido: {authorization}")
    
    # Devolvemos un usuario de prueba independientemente del token
    return {"id": 1, "username": "demo_user"}
