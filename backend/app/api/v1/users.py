
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.session import get_db
from backend.app.repositories.user_repository import UserRepository
from backend.app.schemas.user import UserCreate, UserResponse
from backend.app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)

    try:
        return service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    repository = UserRepository(db)
    service = UserService(repository)

    user = service.get_user(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user
