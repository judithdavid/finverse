
from datetime import date

from pydantic import BaseModel


class TransactionFilter(BaseModel):
    start_date: date | None = None
    end_date: date | None = None
    category_id: int | None = None
    wallet_id: int | None = None
    transaction_type: str | None = None
