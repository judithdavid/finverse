
from fastapi import APIRouter

from backend.app.api.v1.users import router as users_router

router = APIRouter()

router.include_router(users_router)