from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("Application startup initiated.")

    yield

    logger.info("Application shutdown completed.")


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    lifespan = lifespan
)


@app.get("/health")
def health_check():

    logger.info("Health check endpoint called.")

    return {
        "status": "healthy",
        "environment": settings.environment,
        "application": settings.app_name,
        "delevoper": "Chand Saifi"
    }