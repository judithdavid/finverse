from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.report import ReportResponse
from backend.app.services.report_service import ReportService

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.get("/", response_model=ReportResponse)
def get_report(
    db: Session = Depends(get_db),
):
    service = ReportService(db)

    return service.get_report()
