from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.loan_repository import LoanRepository
from backend.app.schemas.loan import LoanCreate, LoanResponse
from backend.app.services.loan_service import LoanService

router = APIRouter(
    prefix="/loans",
    tags=["Loans"],
)


@router.post("/", response_model=LoanResponse, status_code=201)
def create_loan(
    loan: LoanCreate,
    db: Session = Depends(get_db),
):
    repository = LoanRepository(db)
    service = LoanService(repository)

    return service.create_loan(loan)


@router.get("/", response_model=list[LoanResponse])
def get_loans(
    db: Session = Depends(get_db),
):
    repository = LoanRepository(db)
    service = LoanService(repository)

    return service.get_loans()


@router.get("/{loan_id}", response_model=LoanResponse)
def get_loan(
    loan_id: int,
    db: Session = Depends(get_db),
):
    repository = LoanRepository(db)
    service = LoanService(repository)

    loan = service.get_loan(loan_id)

    if loan is None:
        raise HTTPException(
            status_code=404,
            detail="Loan not found",
        )

    return loan


@router.delete("/{loan_id}")
def delete_loan(
    loan_id: int,
    db: Session = Depends(get_db),
):
    repository = LoanRepository(db)
    service = LoanService(repository)

    loan = service.delete_loan(loan_id)

    if loan is None:
        raise HTTPException(
            status_code=404,
            detail="Loan not found",
        )

    return {"message": "Loan deleted successfully"}
