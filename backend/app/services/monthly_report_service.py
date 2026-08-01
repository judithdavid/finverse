from sqlalchemy import extract, func
from sqlalchemy.orm import Session

from backend.app.models.transaction import Transaction


class MonthlyReportService:
    def __init__(self, db: Session):
        self.db = db

    def get_monthly_report(self):
        results = (
            self.db.query(
                extract("month", Transaction.created_at).label("month"),
                Transaction.transaction_type,
                func.sum(Transaction.amount).label("total"),
            )
            .group_by(
                extract("month", Transaction.created_at),
                Transaction.transaction_type,
            )
            .order_by(
                extract("month", Transaction.created_at)
            )
            .all()
        )

        report = {}

        for month, transaction_type, total in results:
            month = str(int(month))

            if month not in report:
                report[month] = {
                    "month": month,
                    "income": 0.0,
                    "expense": 0.0,
                }

            report[month][transaction_type] = float(total)

        return list(report.values())
