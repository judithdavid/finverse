from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.investment_repository import (
    InvestmentRepository,
)
from backend.app.schemas.investment import (
    InvestmentCreate,
    InvestmentResponse,
)
from backend.app.services.investment_service import (
    InvestmentService,
)

router = APIRouter(
    prefix="/investments",
    tags=["Investments"],
)


@router.post("/", response_model=InvestmentResponse, status_code=201)
def create_investment(
    investment: InvestmentCreate,
    db: Session = Depends(get_db),
):
    repository = InvestmentRepository(db)
    service = InvestmentService(repository)

    return service.create_investment(investment)


@router.get("/", response_model=list[InvestmentResponse])
def get_investments(
    db: Session = Depends(get_db),
):
    repository = InvestmentRepository(db)
    service = InvestmentService(repository)

    return service.get_investments()


@router.get("/{investment_id}", response_model=InvestmentResponse)
def get_investment(
    investment_id: int,
    db: Session = Depends(get_db),
):
    repository = InvestmentRepository(db)
    service = InvestmentService(repository)

    investment = service.get_investment(investment_id)

    if investment is None:
        raise HTTPException(
            status_code=404,
            detail="Investment not found",
        )

    return investment


@router.delete("/{investment_id}")
def delete_investment(
    investment_id: int,
    db: Session = Depends(get_db),
):
    repository = InvestmentRepository(db)
    service = InvestmentService(repository)

    investment = service.delete_investment(investment_id)

    if investment is None:
        raise HTTPException(
            status_code=404,
            detail="Investment not found",
        )

    return {"message": "Investment deleted successfully"}
