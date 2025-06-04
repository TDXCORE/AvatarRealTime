# Avatar IA Backend

Backend para la aplicación Avatar IA, que proporciona servicios de avatares virtuales con inteligencia artificial.

## Características

- API RESTful con FastAPI
- Integración con Supabase para autenticación y almacenamiento
- Integración con LiveKit para streaming de video y audio en tiempo real
- Agentes de IA para conversación y automatización
- Síntesis de voz para avatares

## Estructura del Proyecto

```
backend/
├── app/
│   ├── agents/             # Agentes de IA
│   ├── api/                # Endpoints de la API
│   │   └── v1/             # Versión 1 de la API
│   ├── core/               # Configuración y clientes
│   ├── services/           # Servicios de la aplicación
│   └── main.py             # Punto de entrada de la aplicación
├── .env.example            # Ejemplo de variables de entorno
├── requirements.txt        # Dependencias de Python
└── Dockerfile              # Configuración de Docker
```

## Requisitos

- Python 3.9+
- Cuenta en Supabase
- Cuenta en LiveKit (opcional para streaming en tiempo real)
- Cuenta en OpenAI (opcional para funcionalidades de IA)

## Instalación y Ejecución Local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/avatar-ia-backend.git
   cd avatar-ia-backend
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r backend/requirements.txt
   ```

3. Copia el archivo `.env.example` a `.env.local` y configura tus variables de entorno:
   ```bash
   cp .env.example backend/.env.local
   ```

4. Inicia el servidor de desarrollo:
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```

5. Accede a la documentación de la API en [http://localhost:8000/docs](http://localhost:8000/docs)

## Despliegue en GitHub

1. Crea un nuevo repositorio en GitHub
2. Inicializa Git en tu proyecto local (si aún no lo has hecho):
   ```bash
   git init
   ```

3. Añade los archivos al repositorio:
   ```bash
   git add .
   ```

4. Haz el primer commit:
   ```bash
   git commit -m "Versión inicial del backend de Avatar IA"
   ```

5. Conecta tu repositorio local con el remoto:
   ```bash
   git remote add origin https://github.com/tu-usuario/avatar-ia-backend.git
   ```

6. Sube los cambios:
   ```bash
   git push -u origin main
   ```

## Despliegue en Render

1. Crea una cuenta en [Render](https://render.com/) si aún no tienes una
2. Conecta tu repositorio de GitHub a Render
3. Crea un nuevo Web Service:
   - Selecciona tu repositorio
   - Selecciona "Docker" como Runtime Environment
   - Deja el Root Directory en blanco (usará la raíz del repositorio)
   - Selecciona el tipo de instancia según tus necesidades

4. Configura las variables de entorno en el panel de Render:
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_SERVICE_ROLE=your-service-role-key
   SUPABASE_ANON_KEY=your-anon-key
   LIVEKIT_URL=wss://your-project.livekit.cloud
   LIVEKIT_API_KEY=your-api-key
   LIVEKIT_API_SECRET=your-api-secret
   OPENAI_API_KEY=your-openai-key (opcional)
   ENVIRONMENT=production
   ```

5. Haz clic en "Create Web Service"

## Desarrollo

### Estructura de la API

- `/agents`: Endpoints relacionados con los agentes de IA
- `/avatar`: Endpoints para gestionar avatares (video, voz)
- `/voice`: Endpoints para síntesis de voz
- `/livekit`: Webhooks de LiveKit
- `/rooms`: Gestión de salas de LiveKit
- `/user`: Autenticación y gestión de usuarios

### Modo de Desarrollo

El proyecto incluye un modo de desarrollo que simula servicios externos cuando no se proporcionan credenciales. Esto facilita el desarrollo y las pruebas sin necesidad de configurar todas las integraciones.

## Licencia

[MIT](LICENSE)
