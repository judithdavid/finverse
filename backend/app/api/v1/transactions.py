from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.transaction_repository import TransactionRepository
from backend.app.schemas.transaction import (
    TransactionCreate,
    TransactionResponse,
)
from backend.app.services.transaction_service import TransactionService

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.post("/", response_model=TransactionResponse, status_code=201)
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
):
    repository = TransactionRepository(db)
    service = TransactionService(repository)

    return service.create_transaction(transaction)


@router.get("/", response_model=list[TransactionResponse])
def get_transactions(
    db: Session = Depends(get_db),
):
    repository = TransactionRepository(db)
    service = TransactionService(repository)

    return service.get_transactions()


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
):
    repository = TransactionRepository(db)
    service = TransactionService(repository)

    transaction = service.get_transaction(transaction_id)

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found",
        )

    return transaction


@router.delete("/{transaction_id}")
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
):
    repository = TransactionRepository(db)
    service = TransactionService(repository)

    transaction = service.delete_transaction(transaction_id)

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found",
        )

    return {"message": "Transaction deleted successfully"}
