from app.core.exceptions import UserCreationError
from app.database.supabase import get_supabase_client
from app.schemas.user import UserCreate

supabase = get_supabase_client()


def create_user(user: UserCreate):
    try:
        user_dict = user.model_dump(mode="json")

        response = supabase.table("users").insert(user_dict).execute()

        return response.data[0]

    except Exception:
        raise UserCreationError()
