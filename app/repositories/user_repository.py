from uuid import uuid4

from app.database.supabase import get_supabase_client
from app.schemas.user import UserCreate

supabase = get_supabase_client()


def create_user_repository(user: UserCreate):
    user_dict = user.model_dump(mode="json")

    response = supabase.table("users").insert(user_dict).execute()

    return response.data[0]


def get_user_by_email(email: str):
    response = supabase.table("users").select("*").eq("email", email).execute()

    if response.data:
        return response.data[0]

    return None


def upload_avatar_repository(file):
    file_extension = file.filename.split(".")[-1]

    file_name = f"{uuid4()}.{file_extension}"

    file_bytes = file.file.read()

    supabase.storage.from_("avatars").upload(
        path=file_name,
        file=file_bytes,
        file_options={"content-type": file.content_type},
    )

    public_url = supabase.storage.from_("avatars").get_public_url(file_name)

    if public_url:
        return {"url": public_url}

    return None
