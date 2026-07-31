from sqlalchemy.orm import Session

from backend.app.models.investment import Investment
from backend.app.schemas.investment import InvestmentCreate


class InvestmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, investment: InvestmentCreate) -> Investment:
        db_investment = Investment(
            name=investment.name,
            investment_type=investment.investment_type,
            amount=investment.amount,
            current_value=investment.current_value,
            user_id=investment.user_id,
        )

        self.db.add(db_investment)
        self.db.commit()
        self.db.refresh(db_investment)

        return db_investment

    def get_by_id(self, investment_id: int):
        return (
            self.db.query(Investment)
            .filter(Investment.id == investment_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Investment).all()

    def delete(self, investment_id: int):
        investment = self.get_by_id(investment_id)

        if investment:
            self.db.delete(investment)
            self.db.commit()

        return investment
