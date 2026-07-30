
from fastapi import APIRouter

from backend.app.api.v1.users import router as users_router
from backend.app.api.v1.wallets import router as wallets_router
from backend.app.api.v1.transactions import router as transactions_router


router = APIRouter()

router.include_router(users_router)
router.include_router(wallets_router)
router.include_router(transactions_router)
