from datetime import datetime
from pydantic import BaseModel, Field
from pydantic import field_validator



class TestimonialSchema(BaseModel):
    name: str = Field(...,min_length=1, max_length=112, description="Nome do autor do depoimento")
    testimonial: str = Field(..., description="Campo de depoimento caracteres = [minimo: 32, maximo:244")

    @classmethod
    @field_validator("testimonial")
    def testimonial_validator(cls,v: str):
        if len(v) < 32 or len(v) > 244:
            raise ValueError("O campo do depoimento deve conter no minimo 32 caracteres e no maximo 244")
        return v



class TestimonialSchemaResponse(BaseModel):
    id: str
    name: str
    testimonial: str
    created_at: datetime