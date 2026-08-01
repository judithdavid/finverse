from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.financial_summary import (
    FinancialSummaryResponse,
)
from backend.app.services.financial_summary_service import (
    FinancialSummaryService,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/financial-summary",
    response_model=FinancialSummaryResponse,
)
def get_financial_summary(
    db: Session = Depends(get_db),
):
    service = FinancialSummaryService(db)

    return service.get_financial_summary()