from fastapi import FastAPI

from app.core.lifespan import lifespan
from app.core.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(lifespan=lifespan)


@app.get("/health")
def healthcheck():
    logger.info("Health check endpoint called")
    return {"status": "ok"}
