from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.database.base import Base


class Loan(Base):
    __tablename__ = "loans"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    lender: Mapped[str]
    amount: Mapped[float]
    remaining_amount: Mapped[float]
    interest_rate: Mapped[float]

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
