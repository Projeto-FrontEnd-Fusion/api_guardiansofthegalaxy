from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import field_validator



class TestimonialSchema(BaseModel):
    name: str = Field(...,min_length=1, max_length=112, description="Nome do autor do depoimento")
    testimonial: str = Field(..., description="Campo de depoimento caracteres = [minimo: 32, maximo:244]", min_length=32, max_length=244)

    



class TestimonialSchemaResponse(BaseModel):
    id: str
    name: str
    testimonial: str
    created_at: datetime