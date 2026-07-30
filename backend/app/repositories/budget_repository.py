from sqlalchemy.orm import Session

from backend.app.models.budget import Budget
from backend.app.schemas.budget import BudgetCreate


class BudgetRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, budget: BudgetCreate) -> Budget:
        db_budget = Budget(
            amount=budget.amount,
            category_id=budget.category_id,
            user_id=budget.user_id,
        )

        self.db.add(db_budget)
        self.db.commit()
        self.db.refresh(db_budget)

        return db_budget

    def get_by_id(self, budget_id: int):
        return (
            self.db.query(Budget)
            .filter(Budget.id == budget_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Budget).all()

    def delete(self, budget_id: int):
        budget = self.get_by_id(budget_id)

        if budget:
            self.db.delete(budget)
            self.db.commit()

        return budget
