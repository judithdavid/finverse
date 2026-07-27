from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from backend.app.core.security import verify_access_token
from backend.app.database.session import get_db
from backend.app.repositories.user_repository import UserRepository

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    email = verify_access_token(credentials.credentials)

    repository = UserRepository(db)

    user = repository.get_by_email(email)

    return user
