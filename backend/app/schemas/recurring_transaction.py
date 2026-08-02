from pydantic import BaseModel


class RecurringTransactionBase(BaseModel):
    description: str
    amount: float
    transaction_type: str
    frequency: str


class RecurringTransactionCreate(RecurringTransactionBase):
    wallet_id: int
    category_id: int


class RecurringTransactionResponse(RecurringTransactionBase):
    id: int
    wallet_id: int
    category_id: int

    model_config = {
        "from_attributes": True
    }
