from fastapi import APIRouter

from app.schemas.error import ErrorResponse
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user

router = APIRouter(prefix="/users", tags=["usuários"])


@router.post(
    "/",
    response_model=UserResponse,
    responses={500: {"model": ErrorResponse}},
)
async def create_user_route(user: UserCreate):
    created_user = create_user(user)
    return created_user
