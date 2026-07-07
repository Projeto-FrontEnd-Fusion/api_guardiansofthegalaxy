from fastapi import APIRouter, File, UploadFile

from app.schemas.error import ErrorResponse
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user, upload_avatar_service

router = APIRouter(prefix="/users", tags=["usuários"])


@router.post(
    "/",
    response_model=UserResponse,
    responses={500: {"model": ErrorResponse}},
)
async def create_user_route(user: UserCreate):
    created_user = create_user(user)
    return created_user


@router.post("/upload", responses={500: {"model": ErrorResponse}})
async def upload_avatar(file: UploadFile = File(...)):
    return upload_avatar_service(file)
