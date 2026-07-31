from backend.app.repositories.savings_goal_repository import (
    SavingsGoalRepository,
)
from backend.app.schemas.savings_goal import SavingsGoalCreate


class SavingsGoalService:
    def __init__(self, repository: SavingsGoalRepository):
        self.repository = repository

    def create_savings_goal(
        self,
        savings_goal: SavingsGoalCreate,
    ):
        return self.repository.create(savings_goal)

    def get_savings_goal(self, savings_goal_id: int):
        return self.repository.get_by_id(savings_goal_id)

    def get_savings_goals(self):
        return self.repository.get_all()

    def delete_savings_goal(self, savings_goal_id: int):
        return self.repository.delete(savings_goal_id)
