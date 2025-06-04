from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, Query
from app.api.dependencies import get_current_user
from app.services.supabase_service import upload_avatar_video, upload_avatar_voice, list_files, get_public_url

router = APIRouter()

# Aquí irán los endpoints de avatar (video, voz) 

@router.post("/video")
def upload_avatar_video_endpoint(file: UploadFile = File(...), user=Depends(get_current_user)):
    file_data = file.file.read()
    res = upload_avatar_video(str(user["id"]), file.filename, file_data)
    if res.get("error"):
        raise HTTPException(status_code=500, detail=res["error"])
    return {"filename": file.filename, "status": "video almacenado", "path": res.get("path")}

@router.post("/voice")
def upload_avatar_voice_endpoint(file: UploadFile = File(...), user=Depends(get_current_user)):
    file_data = file.file.read()
    res = upload_avatar_voice(str(user["id"]), file.filename, file_data)
    if res.get("error"):
        raise HTTPException(status_code=500, detail=res["error"])
    return {"filename": file.filename, "status": "voz almacenada", "path": res.get("path")}

@router.get("/video/list")
def list_avatar_videos(user=Depends(get_current_user)):
    res = list_files("video", str(user["id"]))
    return {"files": res.get("data", [])}

@router.get("/voz/list")
def list_avatar_voices(user=Depends(get_current_user)):
    res = list_files("voz", str(user["id"]))
    return {"files": res.get("data", [])}

@router.get("/video/url")
def get_video_url(file_name: str = Query(...), user=Depends(get_current_user)):
    res = get_public_url("video", str(user["id"]), file_name)
    return {"url": res.get("publicURL")}

@router.get("/voz/url")
def get_voz_url(file_name: str = Query(...), user=Depends(get_current_user)):
    res = get_public_url("voz", str(user["id"]), file_name)
    return {"url": res.get("publicURL")} 