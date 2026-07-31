from sqlalchemy.orm import Session

from backend.app.models.loan import Loan
from backend.app.schemas.loan import LoanCreate


class LoanRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, loan: LoanCreate) -> Loan:
        db_loan = Loan(
            lender=loan.lender,
            amount=loan.amount,
            remaining_amount=loan.remaining_amount,
            interest_rate=loan.interest_rate,
            user_id=loan.user_id,
        )

        self.db.add(db_loan)
        self.db.commit()
        self.db.refresh(db_loan)

        return db_loan

    def get_by_id(self, loan_id: int):
        return (
            self.db.query(Loan)
            .filter(Loan.id == loan_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Loan).all()

    def delete(self, loan_id: int):
        loan = self.get_by_id(loan_id)

        if loan:
            self.db.delete(loan)
            self.db.commit()

        return loan
