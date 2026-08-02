
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.user_repository import UserRepository
from backend.app.services.user_service import UserService
from backend.app.core.security import create_access_token
from backend.app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
    UserUpdate,
    Token,
)

from backend.app.api.dependencies import get_current_user
from backend.app.models.user import User
from fastapi import Request

from backend.app.core.rate_limit import limiter


router = APIRouter(prefix="/users", tags=["Users"])



@router.post("/", response_model=UserResponse, status_code=201)
# @limiter.limit("10/minute")
def create_user( request: Request, user: UserCreate, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)

    try:
        return service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.post("/login", response_model=Token)
@limiter.limit("10/minute")
def login(user: UserLogin, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)

    authenticated_user = service.authenticate_user(
        user.email,
        user.password,
    )

    if authenticated_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {"sub": authenticated_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }

@router.get("/me", response_model=UserResponse)
def get_current_logged_in_user(
    current_user: User = Depends(get_current_user),
):
    return current_user

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


