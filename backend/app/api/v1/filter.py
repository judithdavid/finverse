from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.filter import TransactionFilter
from backend.app.schemas.transaction import TransactionResponse
from backend.app.services.filter_service import FilterService

router = APIRouter(
    prefix="/filters",
    tags=["Filters"],
)


@router.get(
    "/transactions",
    response_model=list[TransactionResponse],
)
def filter_transactions(
    start_date: date | None = Query(None),
    end_date: date | None = Query(None),
    category_id: int | None = Query(None),
    wallet_id: int | None = Query(None),
    transaction_type: str | None = Query(None),
    db: Session = Depends(get_db),
):
    filters = TransactionFilter(
        start_date=start_date,
        end_date=end_date,
        category_id=category_id,
        wallet_id=wallet_id,
        transaction_type=transaction_type,
    )

    service = FilterService(db)

    return service.filter_transactions(filters)
