from uuid import uuid4

from fastapi import HTTPException

from app.database.supabase import get_supabase_client

supabase = get_supabase_client()


def upload_avatar_service(file):
    try:
        file_extension = file.filename.split(".")[-1]

        file_name = f"{uuid4()}.{file_extension}"

        file_bytes = file.file.read()

        supabase.storage.from_("avatars").upload(
            path=file_name,
            file=file_bytes,
            file_options={"content-type": file.content_type},
        )

        public_url = supabase.storage.from_("avatars").get_public_url(file_name)

        return {"url": public_url}

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
