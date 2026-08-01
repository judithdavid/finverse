from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.app.models.transaction import Transaction


class CashFlowService:
    def __init__(self, db: Session):
        self.db = db

    def get_cash_flow(self):
        total_income = (
            self.db.query(func.sum(Transaction.amount))
            .filter(Transaction.transaction_type == "income")
            .scalar()
            or 0
        )

        total_expense = (
            self.db.query(func.sum(Transaction.amount))
            .filter(Transaction.transaction_type == "expense")
            .scalar()
            or 0
        )

        return {
            "total_income": float(total_income),
            "total_expense": float(total_expense),
            "net_cash_flow": float(total_income - total_expense),
        }
