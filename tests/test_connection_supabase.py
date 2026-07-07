from app.database.supabase import get_supabase_client


def test_supabase_connection():
    supabase = get_supabase_client()

    assert hasattr(supabase, "table")

    response = supabase.table("users").select("id").limit(1).execute()

    assert response is not None
