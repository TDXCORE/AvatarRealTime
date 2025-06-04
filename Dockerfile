FROM python:3.11-slim

WORKDIR /app

# Copiar los archivos de requisitos primero para aprovechar la caché de Docker
COPY backend/requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Crear archivos __init__.py si no existen
RUN find /app -type d -exec touch {}/__init__.py \; 2>/dev/null || true

# Exponer el puerto que usará la aplicación
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
