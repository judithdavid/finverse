from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.app.models.budget import Budget
from backend.app.models.investment import Investment
from backend.app.models.loan import Loan
from backend.app.models.savings_goal import SavingsGoal
from backend.app.models.transaction import Transaction
from backend.app.models.wallet import Wallet


class ReportService:
    def __init__(self, db: Session):
        self.db = db

    def get_report(self):
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

        total_balance = (
            self.db.query(func.sum(Wallet.balance)).scalar() or 0
        )

        total_budget = (
            self.db.query(func.sum(Budget.amount)).scalar() or 0
        )

        total_savings = (
            self.db.query(func.sum(SavingsGoal.current_amount)).scalar()
            or 0
        )

        total_investments = (
            self.db.query(func.sum(Investment.current_value)).scalar()
            or 0
        )

        total_loans = (
            self.db.query(func.sum(Loan.remaining_amount)).scalar()
            or 0
        )

        return {
            "total_income": total_income,
            "total_expense": total_expense,
            "total_balance": total_balance,
            "total_budget": total_budget,
            "total_savings": total_savings,
            "total_investments": total_investments,
            "total_loans": total_loans,
        }
