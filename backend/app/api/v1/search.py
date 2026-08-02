from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.schemas.search import TransactionSearchResponse
from backend.app.services.search_service import SearchService

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.get(
    "/transactions",
    response_model=list[TransactionSearchResponse],
)
def search_transactions(
    query: str,
    db: Session = Depends(get_db),
):
    service = SearchService(db)

    return service.search_transactions(query)
