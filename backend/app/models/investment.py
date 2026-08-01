from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from decimal import Decimal
from backend.app.database.base import Base

class Investment(Base):
    __tablename__ = "investments"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    investment_type: Mapped[str]
    # amount: Mapped[float]
    # current_value: Mapped[float]
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    current_value: Mapped[Decimal] = mapped_column(Numeric(12, 2))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


