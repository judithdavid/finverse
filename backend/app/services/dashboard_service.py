
from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.app.models.budget import Budget
from backend.app.models.transaction import Transaction
from backend.app.models.wallet import Wallet


class DashboardService:
    def __init__(self, db: Session):
        self.db = db

    def get_dashboard(self):
        total_balance = (
            self.db.query(func.sum(Wallet.balance))
            .scalar()
            or 0
        )

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

        total_budget = (
            self.db.query(func.sum(Budget.amount))
            .scalar()
            or 0
        )

        return {
            "total_balance": float(total_balance),
            "total_income": float(total_income),
            "total_expense": float(total_expense),
            "total_budget": float(total_budget),
        }
