from datetime import datetime
from pydantic import BaseModel, Field



class TestimonialsSchema(BaseModel):
    name: str = Field(...,min_length=1, max_length=112, description="Nome do autor do depoimento"),
    testimonial: str = Field(...,min_length=32, max_length=244, description="Campo de depoimento caracteres = [minimo: 32, maximo:244")



class TestimonialSchemaResponse(BaseModel):
    id: int
    name: str
    testimonial: str
    created_at: datetime