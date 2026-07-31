from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.savings_goal_repository import (
    SavingsGoalRepository,
)
from backend.app.schemas.savings_goal import (
    SavingsGoalCreate,
    SavingsGoalResponse,
)
from backend.app.services.savings_goal_service import (
    SavingsGoalService,
)

router = APIRouter(
    prefix="/savings-goals",
    tags=["Savings Goals"],
)


@router.post("/", response_model=SavingsGoalResponse, status_code=201)
def create_savings_goal(
    savings_goal: SavingsGoalCreate,
    db: Session = Depends(get_db),
):
    repository = SavingsGoalRepository(db)
    service = SavingsGoalService(repository)

    return service.create_savings_goal(savings_goal)


@router.get("/", response_model=list[SavingsGoalResponse])
def get_savings_goals(
    db: Session = Depends(get_db),
):
    repository = SavingsGoalRepository(db)
    service = SavingsGoalService(repository)

    return service.get_savings_goals()


@router.get("/{savings_goal_id}", response_model=SavingsGoalResponse)
def get_savings_goal(
    savings_goal_id: int,
    db: Session = Depends(get_db),
):
    repository = SavingsGoalRepository(db)
    service = SavingsGoalService(repository)

    savings_goal = service.get_savings_goal(savings_goal_id)

    if savings_goal is None:
        raise HTTPException(
            status_code=404,
            detail="Savings goal not found",
        )

    return savings_goal


@router.delete("/{savings_goal_id}")
def delete_savings_goal(
    savings_goal_id: int,
    db: Session = Depends(get_db),
):
    repository = SavingsGoalRepository(db)
    service = SavingsGoalService(repository)

    savings_goal = service.delete_savings_goal(savings_goal_id)

    if savings_goal is None:
        raise HTTPException(
            status_code=404,
            detail="Savings goal not found",
        )

    return {"message": "Savings goal deleted successfully"}
