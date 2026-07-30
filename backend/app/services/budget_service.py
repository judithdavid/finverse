from backend.app.repositories.budget_repository import BudgetRepository
from backend.app.schemas.budget import BudgetCreate


class BudgetService:
    def __init__(self, repository: BudgetRepository):
        self.repository = repository

    def create_budget(self, budget: BudgetCreate):
        return self.repository.create(budget)

    def get_budget(self, budget_id: int):
        return self.repository.get_by_id(budget_id)

    def get_budgets(self):
        return self.repository.get_all()

    def delete_budget(self, budget_id: int):
        return self.repository.delete(budget_id)
