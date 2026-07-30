from sqlalchemy.orm import Session

from backend.app.models.category import Category
from backend.app.schemas.category import CategoryCreate


class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, category: CategoryCreate) -> Category:
        db_category = Category(
            name=category.name,
            category_type=category.category_type,
            user_id=category.user_id,
        )

        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)

        return db_category

    def get_by_id(self, category_id: int):
        return (
            self.db.query(Category)
            .filter(Category.id == category_id)
            .first()
        )

    def get_all(self):
        return self.db.query(Category).all()

    def delete(self, category_id: int):
        category = self.get_by_id(category_id)

        if category:
            self.db.delete(category)
            self.db.commit()

        return category
