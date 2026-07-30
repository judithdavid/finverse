from sqlalchemy.orm import Session

from backend.app.models.transaction import Transaction
from backend.app.schemas.transaction import TransactionCreate


class TransactionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, transaction: TransactionCreate) -> Transaction:
        db_transaction = Transaction(
            amount=transaction.amount,
            description=transaction.description,
            transaction_type=transaction.transaction_type,
            wallet_id=transaction.wallet_id,
        )

        self.db.add(db_transaction)
        self.db.commit()
        self.db.refresh(db_transaction)

        return db_transaction

    def get_by_id(self, transaction_id: int):
        return (
            self.db.query(Transaction)
            .filter(Transaction.id == transaction_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Transaction).all()

    def delete(self, transaction_id: int):
        transaction = self.get_by_id(transaction_id)

        if transaction:
            self.db.delete(transaction)
            self.db.commit()

        return transaction
