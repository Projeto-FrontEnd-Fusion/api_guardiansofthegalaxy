from better_profanity import profanity
from app.utils.bad_words import bad_w

from app.core.exceptions import TestimonialContentBlocked, TestimonialError
from app.repositories.testimonial_repository import (
    create_testimonial_repository,
    list_testimonials_repository,
)
from app.schemas.testimonial import TestimonialsSchema



profanity.load_censor_words(bad_w)


def create_testimonial(testimonial: TestimonialsSchema):
    try:
        if profanity.contains_profanity(testimonial.name) or \
           profanity.contains_profanity(testimonial.testimonial):
            raise TestimonialContentBlocked()

        return create_testimonial_repository(testimonial)

    except TestimonialContentBlocked:
        raise TestimonialContentBlocked()
    except Exception:
        raise TestimonialError()


def list_testimonials():
    try:
        return list_testimonials_repository()
    except Exception:
        raise TestimonialError()