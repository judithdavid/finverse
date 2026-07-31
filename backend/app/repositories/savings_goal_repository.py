from sqlalchemy.orm import Session

from backend.app.models.savings_goal import SavingsGoal
from backend.app.schemas.savings_goal import SavingsGoalCreate


class SavingsGoalRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, savings_goal: SavingsGoalCreate) -> SavingsGoal:
        db_savings_goal = SavingsGoal(
            name=savings_goal.name,
            target_amount=savings_goal.target_amount,
            current_amount=savings_goal.current_amount,
            user_id=savings_goal.user_id,
        )

        self.db.add(db_savings_goal)
        self.db.commit()
        self.db.refresh(db_savings_goal)

        return db_savings_goal

    def get_by_id(self, savings_goal_id: int):
        return (
            self.db.query(SavingsGoal)
            .filter(SavingsGoal.id == savings_goal_id)
            .first()
        )

    def get_all(self):
        return self.db.query(SavingsGoal).all()

    def delete(self, savings_goal_id: int):
        savings_goal = self.get_by_id(savings_goal_id)

        if savings_goal:
            self.db.delete(savings_goal)
            self.db.commit()

        return savings_goal
