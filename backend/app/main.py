from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.organizations import router as organizations_router
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="AEC AI Platform API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router, tags=["System"])
app.include_router(
    organizations_router,
    prefix="/api/organizations",
    tags=["Organizations"],
)


@app.get("/")
def root():
    return {
        "name": settings.app_name,
        "version": "0.1.0",
        "status": "running",
        "phase": 1,
    }
