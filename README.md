# Avatar IA Backend v2.0

Backend para la plataforma Avatar IA con integración de LiveKit, Supabase y procesamiento de audio/video en tiempo real.

## Despliegue en Render

### 1. Configuración de Variables de Entorno

Configura las siguientes variables de entorno en el panel de Render:

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

### 2. Despliegue en Render

1. Inicia sesión en tu cuenta de Render (https://dashboard.render.com/)
2. Haz clic en "New" y selecciona "Web Service"
3. Conecta tu repositorio de GitHub
4. Configura el servicio:
   - **Name**: Un nombre único para tu servicio (ej. AvatarRealTime)
   - **Region**: Selecciona la región más cercana a tus usuarios
   - **Branch**: main (o la rama que desees desplegar)
   - **Root Directory**: Deja en blanco (usará la raíz del repositorio)
   - **Runtime Environment**: Docker
   - **Instance Type**: Selecciona según tus necesidades (Free para pruebas)
5. Haz clic en "Create Web Service"

### 3. Configuración Adicional

- **Health Check Path**: /
- **Auto-Deploy**: Actívalo si deseas que Render despliegue automáticamente cuando haya cambios en el repositorio

### 4. Solución de Problemas

Si encuentras errores durante el despliegue:

1. Verifica los logs de construcción en Render
2. Asegúrate de que todas las variables de entorno estén configuradas correctamente
3. Verifica que el Dockerfile esté en la raíz del proyecto
4. Comprueba que el comando para iniciar la aplicación en el Dockerfile sea correcto

### 5. Cambios Realizados para el Despliegue en Render

1. Creado Dockerfile en la raíz del proyecto
2. Añadido .dockerignore para optimizar la construcción
3. Configurado el comando de inicio para usar la ruta correcta de importación
4. Añadido archivos `__init__.py` en todos los directorios para que Python los reconozca como paquetes

## Desarrollo Local

Para ejecutar el proyecto localmente:

1. Crea un archivo `.env.local` en el directorio `backend` con las variables de entorno necesarias
2. Instala las dependencias: `pip install -r backend/requirements.txt`
3. Ejecuta el servidor: `uvicorn backend.app.main:app --reload`

## Estructura del Proyecto

```
Dockerfile                         # Configuración para Docker/Render
.dockerignore                      # Archivos a ignorar en la construcción de Docker
backend/
├── __init__.py                    # Archivo para reconocer el directorio como paquete
├── index.py                       # Punto de entrada alternativo
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
