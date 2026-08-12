from fastapi import APIRouter
from sqlalchemy import text

from app.database.session import engine

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "healthy", "service": "aec-ai-platform"}


@router.get("/ready")
def ready():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "ready", "database": "ok"}
    except Exception:
        return {"status": "degraded", "database": "unavailable"}
