from sqlalchemy.orm import Session

from backend.app.models.transaction import Transaction


class SearchService:
    def __init__(self, db: Session):
        self.db = db

    def search_transactions(self, query: str):
        return (
            self.db.query(Transaction)
            .filter(Transaction.description.ilike(f"%{query}%"))
            .all()
        )
