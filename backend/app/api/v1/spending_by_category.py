from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.spending_by_category import CategorySpending
from backend.app.services.spending_by_category_service import (
    SpendingByCategoryService,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/spending-by-category",
    response_model=list[CategorySpending],
)
def get_spending_by_category(
    db: Session = Depends(get_db),
):
    service = SpendingByCategoryService(db)

    return service.get_spending_by_category()
