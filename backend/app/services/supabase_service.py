# Aquí irá la lógica de operaciones de base de datos con Supabase 

from backend.app.core.supabase import supabase

BUCKET_AVATAR = "avatar"
FOLDER_VIDEO = "video"
FOLDER_VOZ = "voz"


def upload_avatar_video(user_id: str, file_name: str, file_data: bytes):
    path = f"{FOLDER_VIDEO}/{user_id}/{file_name}"
    res = supabase.storage.from_(BUCKET_AVATAR).upload(path, file_data, upsert=True)
    return res

def upload_avatar_voice(user_id: str, file_name: str, file_data: bytes):
    path = f"{FOLDER_VOZ}/{user_id}/{file_name}"
    res = supabase.storage.from_(BUCKET_AVATAR).upload(path, file_data, upsert=True)
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
