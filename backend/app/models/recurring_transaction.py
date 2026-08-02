from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.database.base import Base


class RecurringTransaction(Base):
    __tablename__ = "recurring_transactions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    description: Mapped[str] = mapped_column(String(255))
    amount: Mapped[float] = mapped_column(Numeric(12, 2))
    transaction_type: Mapped[str] = mapped_column(String(20))
    frequency: Mapped[str] = mapped_column(String(20))

    wallet_id: Mapped[int] = mapped_column(
        ForeignKey("wallets.id")
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )

    wallet = relationship("Wallet")
    category = relationship("Category")
