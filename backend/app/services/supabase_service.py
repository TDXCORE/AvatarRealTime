# Aquí irá la lógica de operaciones de base de datos con Supabase 

from backend.app.core.supabase import supabase
import logging

logger = logging.getLogger(__name__)

BUCKET_AVATAR = "avatar"
FOLDER_VIDEO = "video"
FOLDER_VOZ = "voz"

def ensure_folder_exists(bucket: str, folder: str):
    """Asegura que una carpeta exista en el bucket de Supabase"""
    try:
        # Intentar listar la carpeta para ver si existe
        supabase.storage.from_(bucket).list(folder)
        logger.info(f"Carpeta {folder} ya existe en bucket {bucket}")
    except Exception as e:
        logger.warning(f"Error al verificar carpeta {folder}: {str(e)}")
        try:
            # Crear un archivo vacío en la carpeta para crearla
            supabase.storage.from_(bucket).upload(f"{folder}/.keep", b"")
            logger.info(f"Carpeta {folder} creada en bucket {bucket}")
        except Exception as e:
            logger.error(f"Error al crear carpeta {folder}: {str(e)}")

def upload_avatar_video(user_id: str, file_name: str, file_data: bytes):
    # Asegurar que la carpeta exista
    folder_path = f"{FOLDER_VIDEO}/{user_id}"
    ensure_folder_exists(BUCKET_AVATAR, folder_path)
    
    path = f"{folder_path}/{file_name}"
    logger.info(f"Subiendo video a {path}")
    res = supabase.storage.from_(BUCKET_AVATAR).upload(path, file_data, file_options={"contentType": "video/webm"})
    return res

def upload_avatar_voice(user_id: str, file_name: str, file_data: bytes):
    # Asegurar que la carpeta exista
    folder_path = f"{FOLDER_VOZ}/{user_id}"
    ensure_folder_exists(BUCKET_AVATAR, folder_path)
    
    path = f"{folder_path}/{file_name}"
    logger.info(f"Subiendo voz a {path}")
    res = supabase.storage.from_(BUCKET_AVATAR).upload(path, file_data, file_options={"contentType": "audio/webm"})
    return res

def get_user_by_id(user_id: str):
    return supabase.table("users").select("*").eq("id", user_id).single().execute()

def update_user_by_id(user_id: str, data: dict):
    return supabase.table("users").update(data).eq("id", user_id).execute()

def list_files(folder: str, user_id: str):
    path = f"{folder}/{user_id}"
    return supabase.storage.from_(BUCKET_AVATAR).list(path)

def get_public_url(folder: str, user_id: str, file_name: str):
    path = f"{folder}/{user_id}/{file_name}"
    return supabase.storage.from_(BUCKET_AVATAR).get_public_url(path)
