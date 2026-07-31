from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from backend.app.database.base import Base

class Bill(Base):
    __tablename__ = "bills"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    amount: Mapped[float]
    due_date: Mapped[str]
    is_paid: Mapped[bool] = mapped_column(default=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
