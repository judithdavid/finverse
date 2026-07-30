from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database.base import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    category_type: Mapped[str] = mapped_column(String(20))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user = relationship("User")
