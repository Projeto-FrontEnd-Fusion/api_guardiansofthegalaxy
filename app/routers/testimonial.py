from app.schemas.error import ErrorResponse
from app.schemas.testimonial import TestimonialSchemaResponse, TestimonialsSchema
from app.services.testimonials_service import create_testimonial, list_testimonials

from fastapi import APIRouter


router = APIRouter(prefix="/testimonials", tags="Depoimentos")

@router.post(
    "/",
    response_model=TestimonialSchemaResponse,
    status_code=201,
    responses={
        400: {"model": ErrorResponse, "description": "Conteúdo bloqueado ou dados inválidos"},
        500: {"model": ErrorResponse},
    },
)
def create_testimonial_route(testimonial: TestimonialsSchema):
    return create_testimonial(testimonial)


@router.get(
    "/",
    response_model=list[TestimonialSchemaResponse],
    responses={500: {"model": ErrorResponse}},
)
def list_testimonials_route():
    return list_testimonials()