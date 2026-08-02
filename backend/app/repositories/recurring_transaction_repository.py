from sqlalchemy.orm import Session

from backend.app.models.recurring_transaction import (
    RecurringTransaction,
)
from backend.app.schemas.recurring_transaction import (
    RecurringTransactionCreate,
)


class RecurringTransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        recurring_transaction: RecurringTransactionCreate,
    ) -> RecurringTransaction:
        db_recurring_transaction = RecurringTransaction(
            description=recurring_transaction.description,
            amount=recurring_transaction.amount,
            transaction_type=recurring_transaction.transaction_type,
            frequency=recurring_transaction.frequency,
            wallet_id=recurring_transaction.wallet_id,
            category_id=recurring_transaction.category_id,
        )

        self.db.add(db_recurring_transaction)
        self.db.commit()
        self.db.refresh(db_recurring_transaction)

        return db_recurring_transaction

    def get_by_id(self, recurring_transaction_id: int):
        return (
            self.db.query(RecurringTransaction)
            .filter(
                RecurringTransaction.id == recurring_transaction_id
            )
            .first()
        )

    def get_all(self):
        return self.db.query(RecurringTransaction).all()

    def delete(self, recurring_transaction_id: int):
        recurring_transaction = self.get_by_id(
            recurring_transaction_id
        )

        if recurring_transaction:
            self.db.delete(recurring_transaction)
            self.db.commit()

        return recurring_transaction