from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.pagination import PaginationParams
from backend.app.schemas.transaction import TransactionResponse
from backend.app.services.pagination_service import PaginationService

router = APIRouter(
    prefix="/pagination",
    tags=["Pagination"],
)


@router.get(
    "/transactions",
    response_model=list[TransactionResponse],
)
def get_transactions(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    sort_by: str = Query("id"),
    order: str = Query("asc"),
    db: Session = Depends(get_db),
):
    params = PaginationParams(
        page=page,
        page_size=page_size,
        sort_by=sort_by,
        order=order,
    )

    service = PaginationService(db)

    return service.get_transactions(params)
