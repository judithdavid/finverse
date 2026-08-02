from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from backend.app.models.transaction import Transaction
from backend.app.schemas.pagination import PaginationParams


class PaginationService:
    def __init__(self, db: Session):
        self.db = db

    def get_transactions(
        self,
        params: PaginationParams,
    ):
        query = self.db.query(Transaction)

        sort_column = getattr(
            Transaction,
            params.sort_by,
            Transaction.id,
        )

        if params.order.lower() == "desc":
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))

        offset = (params.page - 1) * params.page_size

        return (
            query.offset(offset)
            .limit(params.page_size)
            .all()
        )
