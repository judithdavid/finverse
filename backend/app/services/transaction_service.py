from backend.app.repositories.transaction_repository import TransactionRepository
from backend.app.schemas.transaction import TransactionCreate


class TransactionService:
    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    def create_transaction(self, transaction: TransactionCreate):
        return self.repository.create(transaction)

    def get_transaction(self, transaction_id: int):
        return self.repository.get_by_id(transaction_id)

    def get_transactions(self):
        return self.repository.get_all()

    def delete_transaction(self, transaction_id: int):
        return self.repository.delete(transaction_id)
