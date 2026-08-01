from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.app.models.category import Category
from backend.app.models.transaction import Transaction


class SpendingByCategoryService:
    def __init__(self, db: Session):
        self.db = db

    def get_spending_by_category(self):
        results = (
            self.db.query(
                Category.name,
                func.sum(Transaction.amount).label("total_amount"),
            )
            .join(
                Transaction,
                Category.id == Transaction.category_id,
            )
            .filter(
                Transaction.transaction_type == "expense"
            )
            .group_by(Category.name)
            .all()
        )

        return [
            {
                "category": name,
                "total_amount": float(total_amount),
            }
            for name, total_amount in results
        ]
