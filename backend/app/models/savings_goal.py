from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from backend.app.database.base import Base


class SavingsGoal(Base):
    __tablename__ = "savings_goals"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    # target_amount: Mapped[float] = mapped_column(Numeric(12, 2))
    # current_amount: Mapped[float] = mapped_column(
    #     Numeric(12, 2),
    #     default=0,
    # )
    target_amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    current_amount: Mapped[Decimal] = mapped_column(
    Numeric(12, 2),
    default=0,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    user = relationship("User")