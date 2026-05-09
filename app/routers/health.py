from fastapi import APIRouter

from app.core.logger import get_logger

logger = get_logger(__name__)

router = APIRouter(tags=["health"])


@router.get("/health")
def healthcheck():
    logger.info("Health check endpoint called")
    return {"status": "ok"}
