
from datetime import datetime

from pydantic import BaseModel


class TransactionBase(BaseModel):
    amount: float
    description: str
    transaction_type: str


class TransactionCreate(TransactionBase):
    wallet_id: int


class TransactionResponse(TransactionBase):
    id: int
    wallet_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
