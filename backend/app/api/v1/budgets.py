from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.budget_repository import BudgetRepository
from backend.app.schemas.budget import (
    BudgetCreate,
    BudgetResponse,
)
from backend.app.services.budget_service import BudgetService

router = APIRouter(
    prefix="/budgets",
    tags=["Budgets"],
)


@router.post("/", response_model=BudgetResponse, status_code=201)
def create_budget(
    budget: BudgetCreate,
    db: Session = Depends(get_db),
):
    repository = BudgetRepository(db)
    service = BudgetService(repository)

    return service.create_budget(budget)


@router.get("/", response_model=list[BudgetResponse])
def get_budgets(
    db: Session = Depends(get_db),
):
    repository = BudgetRepository(db)
    service = BudgetService(repository)

    return service.get_budgets()


@router.get("/{budget_id}", response_model=BudgetResponse)
def get_budget(
    budget_id: int,
    db: Session = Depends(get_db),
):
    repository = BudgetRepository(db)
    service = BudgetService(repository)

    budget = service.get_budget(budget_id)

    if budget is None:
        raise HTTPException(
            status_code=404,
            detail="Budget not found",
        )

    return budget


@router.delete("/{budget_id}")
def delete_budget(
    budget_id: int,
    db: Session = Depends(get_db),
):
    repository = BudgetRepository(db)
    service = BudgetService(repository)

    budget = service.delete_budget(budget_id)

    if budget is None:
        raise HTTPException(
            status_code=404,
            detail="Budget not found",
        )

    return {"message": "Budget deleted successfully"}