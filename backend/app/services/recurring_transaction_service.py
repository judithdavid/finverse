from backend.app.repositories.recurring_transaction_repository import (
    RecurringTransactionRepository,
)
from backend.app.schemas.recurring_transaction import (
    RecurringTransactionCreate,
)


class RecurringTransactionService:
    def __init__(
        self,
        repository: RecurringTransactionRepository,
    ):
        self.repository = repository

    def create_recurring_transaction(
        self,
        recurring_transaction: RecurringTransactionCreate,
    ):
        return self.repository.create(recurring_transaction)

    def get_recurring_transaction(
        self,
        recurring_transaction_id: int,
    ):
        return self.repository.get_by_id(recurring_transaction_id)

    def get_recurring_transactions(self):
        return self.repository.get_all()

    def delete_recurring_transaction(
        self,
        recurring_transaction_id: int,
    ):
        return self.repository.delete(recurring_transaction_id)
