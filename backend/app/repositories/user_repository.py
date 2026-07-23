from sqlalchemy.orm import Session

from backend.app.models.user import User
from backend.app.schemas.user import UserCreate, UserUpdate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: UserCreate) -> User:
        db_user = User(
            email=user.email,
            full_name=user.full_name,
            password_hash=user.password,
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user

    def update(self, user: User, user_data: UserUpdate):
        user.full_name = user_data.full_name

        self.db.commit()
        self.db.refresh(user)

        return user


    def get_by_email(self, email: str):
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def get_by_id(self, user_id: int):
        return (
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )
    
    def get_all(self):
        return self.db.query(User).all()

    def delete(self, user: User):
        self.db.delete(user)
        self.db.commit()

