from datetime import datetime, timezone

from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    detail: str = Field(description="Mensagem descritiva do erro")
    error_code: str | None = Field(
        default=None, description="Código interno do erro para rastreamento"
    )
    timestamp: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Momento em que o erro ocorreu",
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "detail": "Usuário não encontrado",
                "error_code": "USER_NOT_FOUND",
                "timestamp": "2026-05-09T15:30:00Z",
            }
        }
    }


class ValidationErrorResponse(BaseModel):
    detail: list[dict] = Field(description="Lista de erros de validação")

    model_config = {
        "json_schema_extra": {
            "example": {
                "detail": [
                    {
                        "loc": ["body", "email"],
                        "msg": "value is not a valid email",
                        "type": "value_error",
                    }
                ]
            }
        }
    }
