from fastapi import APIRouter, Body, Depends, HTTPException
from backend.app.api.dependencies import get_current_user
from backend.app.core.supabase import supabase
from backend.app.services.supabase_service import get_user_by_id, update_user_by_id

router = APIRouter()

@router.post("/register")
def register_user(email: str = Body(...), password: str = Body(...), username: str = Body(...)):
    # Registro en Supabase Auth
    auth_res = supabase.auth.sign_up({"email": email, "password": password})
    if auth_res.get("error"):
        raise HTTPException(status_code=400, detail=auth_res["error"]["message"])
    user_id = auth_res["user"]["id"]
    # Registro en tabla users
    db_res = supabase.table("users").insert({"id": user_id, "email": email, "username": username}).execute()
    if db_res.get("error"):
        raise HTTPException(status_code=400, detail=db_res["error"]["message"])
    return {"id": user_id, "email": email, "username": username}

@router.post("/login")
def login_user(email: str = Body(...), password: str = Body(...)):
    auth_res = supabase.auth.sign_in_with_password({"email": email, "password": password})
    if auth_res.get("error"):
        raise HTTPException(status_code=401, detail=auth_res["error"]["message"])
    return {"access_token": auth_res["session"]["access_token"], "user": auth_res["user"]}

@router.get("/profile")
def get_profile(user=Depends(get_current_user)):
    db_res = get_user_by_id(user["id"])
    if db_res.get("error"):
        raise HTTPException(status_code=404, detail=db_res["error"]["message"])
    return db_res["data"]

@router.put("/profile")
def update_profile(data: dict = Body(...), user=Depends(get_current_user)):
    db_res = update_user_by_id(user["id"], data)
    if db_res.get("error"):
        raise HTTPException(status_code=400, detail=db_res["error"]["message"])
    return db_res["data"]
