from app.database.supabase import get_supabase_client
from app.schemas.testimonial import TestimonialsSchema

supabase = get_supabase_client()

def create_testimonial_repository(testimonial: TestimonialsSchema):
    response = (supabase.table("testimonials").insert(testimonial.model_dump(mode="json")).execute())

    return response.data[0]

def list_testimonials_repository():
    response = (supabase.table("testimonials").select("*").order("created_at", desc=True).execute())
    
    return response.data