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
4. Asegúrate de que el archivo `backend/vercel_app.py` exista y esté correctamente configurado

## Desarrollo Local

Para ejecutar el proyecto localmente:

1. Crea un archivo `.env.local` en el directorio `backend` con las variables de entorno necesarias
2. Instala las dependencias: `pip install -r backend/requirements.txt`
3. Ejecuta el servidor: `uvicorn backend.app.main:app --reload`

## Estructura del Proyecto

```
backend/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── agents.py            # Agentic endpoints
│   │   │   ├── avatar.py            # Avatar management
│   │   │   ├── voice.py             # Voice operations
│   │   │   ├── livekit_webhooks.py  # LiveKit events
│   │   │   └── rooms.py             # Room management
│   │   └── dependencies.py          # Auth & validation
│   ├── core/
│   │   ├── config.py               # Environment config
│   │   ├── supabase.py             # Supabase client
│   │   └── livekit_client.py       # LiveKit integration
│   ├── services/
│   │   ├── livekit_service.py      # LiveKit room management
│   │   ├── audio_service.py        # STT processing
│   │   ├── agentic_service.py      # Multi-agent workflows
│   │   ├── tts_service.py          # Voice synthesis
│   │   ├── avatar_service.py       # ROI lipsync rendering
│   │   ├── stream_publisher.py     # LiveKit publishing
│   │   └── supabase_service.py     # Database operations
