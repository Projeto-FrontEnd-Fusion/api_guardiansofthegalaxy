from fastapi import APIRouter, HTTPException

from app.database.supabase import get_supabase_client
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user

router = APIRouter(prefix="/users", tags=["usuários"])
supabase = get_supabase_client()


@router.post("/", response_model=UserResponse)
async def create_user_route(user: UserCreate):
    try:
        created_user = create_user(user)

        return created_user

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
