from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.recurring_transaction_repository import (
    RecurringTransactionRepository,
)
from backend.app.schemas.recurring_transaction import (
    RecurringTransactionCreate,
    RecurringTransactionResponse,
)
from backend.app.services.recurring_transaction_service import (
    RecurringTransactionService,
)

router = APIRouter(
    prefix="/recurring-transactions",
    tags=["Recurring Transactions"],
)


@router.post("/", response_model=RecurringTransactionResponse, status_code=201)
def create_recurring_transaction(
    recurring_transaction: RecurringTransactionCreate,
    db: Session = Depends(get_db),
):
    repository = RecurringTransactionRepository(db)
    service = RecurringTransactionService(repository)

    return service.create_recurring_transaction(recurring_transaction)


@router.get("/", response_model=list[RecurringTransactionResponse])
def get_recurring_transactions(
    db: Session = Depends(get_db),
):
    repository = RecurringTransactionRepository(db)
    service = RecurringTransactionService(repository)

    return service.get_recurring_transactions()


@router.get("/{recurring_transaction_id}", response_model=RecurringTransactionResponse)
def get_recurring_transaction(
    recurring_transaction_id: int,
    db: Session = Depends(get_db),
):
    repository = RecurringTransactionRepository(db)
    service = RecurringTransactionService(repository)

    recurring_transaction = service.get_recurring_transaction(
        recurring_transaction_id
    )

    if recurring_transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Recurring transaction not found",
        )

    return recurring_transaction


@router.delete("/{recurring_transaction_id}")
def delete_recurring_transaction(
    recurring_transaction_id: int,
    db: Session = Depends(get_db),
):
    repository = RecurringTransactionRepository(db)
    service = RecurringTransactionService(repository)

    recurring_transaction = service.delete_recurring_transaction(
        recurring_transaction_id
    )

    if recurring_transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Recurring transaction not found",
        )

    return {
        "message": "Recurring transaction deleted successfully"
    }
