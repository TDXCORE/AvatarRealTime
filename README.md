# Avatar IA Backend v2.0

Backend para la plataforma Avatar IA con integración de LiveKit, Supabase y procesamiento de audio/video en tiempo real.

## Despliegue en Vercel

### 1. Configuración de Variables de Entorno

Configura las siguientes variables de entorno en el panel de Vercel:

```
# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE=your-service-role-key
SUPABASE_ANON_KEY=your-anon-key

# LiveKit
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret

# OpenAI (opcional para esta versión)
OPENAI_API_KEY=your-openai-key
```

### 2. Despliegue

1. Conecta tu repositorio de GitHub a Vercel
2. Configura el directorio raíz como el directorio que contiene el archivo `vercel.json`
3. Asegúrate de que el framework preset sea "Other"
4. Configura el comando de build como vacío
5. Configura el directorio de salida como vacío
6. Haz clic en "Deploy"

### 3. Solución de Problemas

Si encuentras errores durante el despliegue:

1. Verifica los logs de construcción en Vercel
2. Asegúrate de que todas las variables de entorno estén configuradas correctamente
3. Verifica que el archivo `vercel.json` esté en la raíz del proyecto
4. Asegúrate de que los archivos `__init__.py` existan en todos los directorios del proyecto
5. Comprueba que las rutas de importación en `backend/index.py` sean correctas

### 4. Cambios Recientes para Solucionar Errores de Despliegue

Se han realizado los siguientes cambios para solucionar errores de despliegue en Vercel:

1. Corregido las rutas de importación en `backend/index.py` y `backend/vercel_app.py`
2. Añadido archivos `__init__.py` en todos los directorios para que Python los reconozca como paquetes
3. Simplificado `vercel.json` para usar solo un punto de entrada
4. Ajustado `requirements.txt` para evitar dependencias problemáticas en Vercel

## Desarrollo Local

Para ejecutar el proyecto localmente:

1. Crea un archivo `.env.local` en el directorio `backend` con las variables de entorno necesarias
2. Instala las dependencias: `pip install -r backend/requirements.txt`
3. Ejecuta el servidor: `uvicorn backend.app.main:app --reload`

## Estructura del Proyecto

```
backend/
├── __init__.py                    # Archivo para reconocer el directorio como paquete
├── index.py                       # Punto de entrada para Vercel
├── vercel_app.py                  # Punto de entrada alternativo
├── app/
│   ├── __init__.py                # Archivo para reconocer el directorio como paquete
│   ├── api/
│   │   ├── __init__.py            # Archivo para reconocer el directorio como paquete
│   │   ├── v1/
│   │   │   ├── __init__.py        # Archivo para reconocer el directorio como paquete
│   │   │   ├── agents.py          # Agentic endpoints
│   │   │   ├── avatar.py          # Avatar management
│   │   │   ├── voice.py           # Voice operations
│   │   │   ├── livekit_webhooks.py # LiveKit events
│   │   │   └── rooms.py           # Room management
│   │   └── dependencies.py        # Auth & validation
│   ├── core/
│   │   ├── __init__.py            # Archivo para reconocer el directorio como paquete
│   │   ├── config.py              # Environment config
│   │   ├── supabase.py            # Supabase client
│   │   └── livekit_client.py      # LiveKit integration
│   ├── services/
│   │   ├── __init__.py            # Archivo para reconocer el directorio como paquete
│   │   ├── livekit_service.py     # LiveKit room management
│   │   ├── audio_service.py       # STT processing
│   │   ├── agentic_service.py     # Multi-agent workflows
│   │   ├── tts_service.py         # Voice synthesis
│   │   ├── avatar_service.py      # ROI lipsync rendering
│   │   ├── stream_publisher.py    # LiveKit publishing
│   │   └── supabase_service.py    # Database operations
│   ├── agents/
│   │   ├── __init__.py            # Archivo para reconocer el directorio como paquete
│   │   ├── conversation_agent.py  # Chat agent
│   │   ├── automation_agent.py    # Workflow automation
│   │   └── memory_agent.py        # Context management
