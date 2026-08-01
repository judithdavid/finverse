from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.cash_flow import CashFlowResponse
from backend.app.services.cash_flow_service import CashFlowService

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/cash-flow",
    response_model=CashFlowResponse,
)
def get_cash_flow(
    db: Session = Depends(get_db),
):
    service = CashFlowService(db)

    return service.get_cash_flow()
