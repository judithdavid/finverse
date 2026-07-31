from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base

class Investment(Base):
    __tablename__ = "investments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    investment_type: Mapped[str]
    amount: Mapped[float]
    current_value: Mapped[float]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
