from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Query
from backend.app.api.dependencies import get_current_user
from backend.app.services.supabase_service import upload_avatar_video, upload_avatar_voice, list_files, get_public_url

router = APIRouter()

# Aquí irán los endpoints de avatar (video, voz) 

@router.post("/video")
def upload_avatar_video_endpoint(file: UploadFile = File(...)):
    file_data = file.file.read()
    # Aquí debes decidir cómo manejar el user_id si ya no hay autenticación. Por ahora, lo dejo como 'anonymous' o similar.
    res = upload_avatar_video("anonymous", file.filename, file_data)
    if hasattr(res, "error") and res.error:
        raise HTTPException(status_code=500, detail=res.error)
    return {
        "filename": file.filename,
        "status": "video almacenado",
        "result": str(res)
    }

@router.post("/voice")
def upload_avatar_voice_endpoint(file: UploadFile = File(...)):
    file_data = file.file.read()
    res = upload_avatar_voice("anonymous", file.filename, file_data)
    if hasattr(res, "error") and res.error:
        raise HTTPException(status_code=500, detail=res.error)
    return {
        "filename": file.filename,
        "status": "voz almacenada",
        "result": str(res)
    }

@router.get("/video/list")
def list_avatar_videos():
    res = list_files("video", "anonymous")
    return {"files": res.get("data", [])}

@router.get("/voz/list")
def list_avatar_voices():
    res = list_files("voz", "anonymous")
    return {"files": res.get("data", [])}

@router.get("/video/url")
def get_video_url(file_name: str = Query(...)):
    res = get_public_url("video", "anonymous", file_name)
    return {"url": res.get("publicURL")}

@router.get("/voz/url")
def get_voz_url(file_name: str = Query(...)):
    res = get_public_url("voz", "anonymous", file_name)
    return {"url": res.get("publicURL")}
