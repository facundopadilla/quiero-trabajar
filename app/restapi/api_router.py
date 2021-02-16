from fastapi import APIRouter

from app.restapi.routes import users

router = APIRouter(prefix="/api/v1")

router.include_router(users.router, tags=["users"])