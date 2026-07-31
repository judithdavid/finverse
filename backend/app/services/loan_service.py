
from backend.app.repositories.loan_repository import LoanRepository
from backend.app.schemas.loan import LoanCreate


class LoanService:
    def __init__(self, repository: LoanRepository):
        self.repository = repository

    def create_loan(self, loan: LoanCreate):
        return self.repository.create(loan)

    def get_loan(self, loan_id: int):
        return self.repository.get_by_id(loan_id)

    def get_loans(self):
        return self.repository.get_all()

    def delete_loan(self, loan_id: int):
        return self.repository.delete(loan_id)

