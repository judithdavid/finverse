from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.app.models.investment import Investment
from backend.app.models.loan import Loan
from backend.app.models.savings_goal import SavingsGoal
from backend.app.models.transaction import Transaction
from backend.app.models.wallet import Wallet


class FinancialSummaryService:
    def __init__(self, db: Session):
        self.db = db

    def get_financial_summary(self):
        wallet_balance = (
            self.db.query(func.sum(Wallet.balance))
            .scalar()
            or 0
        )

        investments = (
            self.db.query(func.sum(Investment.current_value))
            .scalar()
            or 0
        )

        savings = (
            self.db.query(func.sum(SavingsGoal.current_amount))
            .scalar()
            or 0
        )

        loans = (
            self.db.query(func.sum(Loan.remaining_amount))
            .scalar()
            or 0
        )

        income = (
            self.db.query(func.sum(Transaction.amount))
            .filter(Transaction.transaction_type == "income")
            .scalar()
            or 0
        )

        expense = (
            self.db.query(func.sum(Transaction.amount))
            .filter(Transaction.transaction_type == "expense")
            .scalar()
            or 0
        )

        total_assets = wallet_balance + investments + savings
        total_liabilities = loans
        net_worth = total_assets - total_liabilities

        savings_rate = (
            ((income - expense) / income) * 100
            if income > 0
            else 0
        )

        return {
            "total_assets": float(total_assets),
            "total_liabilities": float(total_liabilities),
            "net_worth": float(net_worth),
            "savings_rate": round(float(savings_rate), 2),
        }