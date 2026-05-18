from fastapi import APIRouter, File, UploadFile

from app.database.supabase import get_supabase_client
from app.services.upload_avatar_service import upload_avatar_service

router = APIRouter(prefix="/upload", tags=["usuários"])
supabase = get_supabase_client()


@router.post("/avatar")
async def upload_avatar(file: UploadFile = File(...)):
    return upload_avatar_service(file)
