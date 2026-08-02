from sqlalchemy.orm import Session

from backend.app.models.transaction import Transaction
from backend.app.schemas.filter import TransactionFilter


class FilterService:
    def __init__(self, db: Session):
        self.db = db

    def filter_transactions(
        self,
        filters: TransactionFilter,
    ):
        query = self.db.query(Transaction)

        if filters.start_date:
            query = query.filter(
                Transaction.created_at >= filters.start_date
            )

        if filters.end_date:
            query = query.filter(
                Transaction.created_at <= filters.end_date
            )

        if filters.category_id:
            query = query.filter(
                Transaction.category_id == filters.category_id
            )

        if filters.wallet_id:
            query = query.filter(
                Transaction.wallet_id == filters.wallet_id
            )

        if filters.transaction_type:
            query = query.filter(
                Transaction.transaction_type == filters.transaction_type
            )

        return query.all()
