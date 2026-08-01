from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.monthly_report import MonthlyReport
from backend.app.services.monthly_report_service import (
    MonthlyReportService,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/monthly-report",
    response_model=list[MonthlyReport],
)
def get_monthly_report(
    db: Session = Depends(get_db),
):
    service = MonthlyReportService(db)

    return service.get_monthly_report()
