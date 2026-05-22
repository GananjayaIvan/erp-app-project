from fastapi import APIRouter

from app.api.v1.hris.routes.health import router as health_router
from app.api.v1.auth.routes import router as auth_router

api_router = APIRouter()

api_router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]
)