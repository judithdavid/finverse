from backend.app.repositories.investment_repository import (
    InvestmentRepository,
)
from backend.app.schemas.investment import InvestmentCreate


class InvestmentService:
    def __init__(self, repository: InvestmentRepository):
        self.repository = repository

    def create_investment(
        self,
        investment: InvestmentCreate,
    ):
        return self.repository.create(investment)

    def get_investment(self, investment_id: int):
        return self.repository.get_by_id(investment_id)

    def get_investments(self):
        return self.repository.get_all()

    def delete_investment(self, investment_id: int):
        return self.repository.delete(investment_id)
