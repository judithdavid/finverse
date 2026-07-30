from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database.base import Base


class Budget(Base):
    __tablename__ = "budgets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    amount: Mapped[float] = mapped_column(Numeric(12, 2))

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    category = relationship("Category")
    user = relationship("User")
