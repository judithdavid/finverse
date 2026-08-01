
from fastapi import APIRouter

from backend.app.api.v1.users import router as users_router
from backend.app.api.v1.wallets import router as wallets_router
from backend.app.api.v1.transactions import router as transactions_router
from backend.app.api.v1.categories import router as categories_router
from backend.app.api.v1.budgets import router as budgets_router
from backend.app.api.v1.dashboard import router as dashboard_router
from backend.app.api.v1.savings_goals import (
    router as savings_goals_router,
)
from backend.app.api.v1.bills import router as bills_router
from backend.app.api.v1.investments import (
    router as investments_router,
)
from backend.app.api.v1.loans import router as loans_router
from backend.app.api.v1.reports import router as reports_router
from backend.app.api.v1.spending_by_category import (
    router as spending_by_category_router,
)

from backend.app.api.v1.monthly_report import (
    router as monthly_report_router,
)
from backend.app.api.v1.cash_flow import (
    router as cash_flow_router,
)
from backend.app.api.v1.financial_summary import (
    router as financial_summary_router,
)


router = APIRouter()

router.include_router(users_router)
router.include_router(wallets_router)
router.include_router(transactions_router)
router.include_router(categories_router)
router.include_router(budgets_router)
router.include_router(dashboard_router)
router.include_router(savings_goals_router)
router.include_router(bills_router)
router.include_router(investments_router)
router.include_router(loans_router)
router.include_router(reports_router)
router.include_router(spending_by_category_router)
router.include_router(monthly_report_router)
router.include_router(cash_flow_router)
router.include_router(financial_summary_router)