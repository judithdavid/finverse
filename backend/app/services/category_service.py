from backend.app.repositories.category_repository import CategoryRepository
from backend.app.schemas.category import CategoryCreate


class CategoryService:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def create_category(self, category: CategoryCreate):
        return self.repository.create(category)

    def get_category(self, category_id: int):
        return self.repository.get_by_id(category_id)

    def get_categories(self):
        return self.repository.get_all()

    def delete_category(self, category_id: int):
        return self.repository.delete(category_id)
