from enum import Enum

from pydantic import BaseModel, EmailStr, Field, HttpUrl


class RoleEnum(str, Enum):
    BACKEND = "backend"
    FRONTEND = "frontend"
    FULLSTACK = "fullstack"
    SCRUM_MASTER = "scrum_master"
    PRODUCT_OWNER = "product_owner"
    UI_UX = "ui_ux"
    QA = "qa"


class AvatarCreate(BaseModel):
    profile_photo: HttpUrl = Field(
        description="Recebe arquivo em formato UploadProfile"
    )


class UserCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=200,
        examples="João Nascimento dos Santos Silva",
        description="Nome completo do usuário",
    )

    email: EmailStr = Field(
        ..., examples="Joaonascimento@email.com", description="Email do usuário"
    )

    role: RoleEnum = Field(..., description="Cargos disponíveis para se inscrever")

    profile_photo_url: str = Field(..., description="URL da foto do perfil")

    bio: str = Field(..., max_length=244, description="Breve definição sobre o usuário")

    skills: list[str] = Field(
        ...,
        min_length=1,
        description="Lista de habilidades do usuários",
        examples=["Python", "FastAPI", "PostgreSQL"],
    )

    linkedin_url: HttpUrl = Field(..., description="URL Linkedin")

    github_url: HttpUrl | None = Field(default=None, description="URL GitHub")

    portfolio_url: HttpUrl | None = Field(default=None, description="URL portfólio")

    instagram_url: HttpUrl | None = Field(default=None, description="URL Instagram")


class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: RoleEnum
    profile_photo_url: str
    bio: str
    skills: list[str]
    linkedin_url: HttpUrl
    github_url: HttpUrl | None
    portfolio_url: HttpUrl | None
    instagram_url: HttpUrl | None
