
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.user_repository import UserRepository
from backend.app.services.user_service import UserService
from backend.app.schemas.user import (
    UserCreate,
    UserResponse,
    UserUpdate,
)


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)

    try:
        return service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)

    return service.get_all_users()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)

    user = service.get_user(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)

    try:
        service.delete_user(user_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db),
):
    repository = UserRepository(db)
    service = UserService(repository)

    try:
        return service.update_user(user_id, user)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
