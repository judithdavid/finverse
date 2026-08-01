from sqlalchemy import ForeignKey, String , Numeric
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database.base import Base


class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    # balance: Mapped[float] = mapped_column(Numeric(12, 2), default=0)
    balance: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user = relationship("User")
