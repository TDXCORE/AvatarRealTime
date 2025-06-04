import sys
import os

# Añadir el directorio raíz al path para que Python pueda encontrar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app.main import app

# Esto es necesario para Vercel
handler = app
