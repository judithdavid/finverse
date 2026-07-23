from backend.app.repositories.user_repository import UserRepository
from backend.app.schemas.user import UserCreate, UserUpdate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: UserCreate):
        existing_user = self.repository.get_by_email(user.email)

        if existing_user:
            raise ValueError("Email already registered")

        return self.repository.create(user)
    
    def update_user(self, user_id: int, user_data: UserUpdate):
        user = self.repository.get_by_id(user_id)

        if user is None:
            raise ValueError("User not found")

        return self.repository.update(user, user_data)

    def get_user(self, user_id: int):
        return self.repository.get_by_id(user_id)

    def get_all_users(self):
        return self.repository.get_all()

    def delete_user(self, user_id: int):
        user = self.repository.get_by_id(user_id)

        if user is None:
            raise ValueError("User not found")

        self.repository.delete(user)

