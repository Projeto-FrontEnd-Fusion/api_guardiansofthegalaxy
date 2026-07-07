from fastapi import UploadFile

from app.core.exceptions import UploadFailedError, UserCreationError, UserInvalidError
from app.repositories.user_repository import (
    create_user_repository,
    get_user_by_email,
    upload_avatar_repository,
)
from app.schemas.user import UserCreate


def create_user(user: UserCreate):
    try:
        checking_email = get_user_by_email(user.email)

        if checking_email:
            raise UserInvalidError()

        return create_user_repository(user)

    except Exception:
        raise UserCreationError()


def upload_avatar_service(file: UploadFile):
    try:
        return upload_avatar_repository(file)

    except Exception:
        raise UploadFailedError()
