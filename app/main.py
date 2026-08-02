from fastapi import FastAPI

from app.core.exception_handler import app_exception_handler
from app.core.exceptions import AppException
from app.core.lifespan import lifespan
from app.core.logger import get_logger
from app.routers import health, user, testimonial

logger = get_logger(__name__)

openapi_tags = [
    {
        "name": "health",
        "description": "Endpoints de monitoramento e health check da aplicação",
    },
    {
        "name": "usuários",
        "description": "Gestão de usuários da plataforma",
    },
    {
        "name": "perfil",
        "description": "Gerenciamento do perfil do usuário autenticado",
    },
    {
        "name": "habilidades",
        "description": "CRUD de habilidades e competências",
    },
    {
        "name": "autenticação",
        "description": "Endpoints de autenticação e autorização",
    },
    {
        "name": "depoimentos",
        "description": "Envio e listagem de depoimentos da seção Deixe seu Depoimento",
    },
]

app = FastAPI(
    title="Guardiões da Galáxia API",
    description=(
        "API da squad Guardiões da Galáxia para gestão de usuários, "
        "perfis, habilidades e autenticação."
    ),
    version="0.1.0",
    lifespan=lifespan,
    openapi_tags=openapi_tags,
    contact={
        "name": "KaioMendonca",
        "email": "kaiomendonca.dev@hotmail.com",
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.add_exception_handler(AppException, app_exception_handler)


app.include_router(health.router)
app.include_router(user.router)
app.include_router(testimonial.router)
