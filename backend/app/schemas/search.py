from pydantic import BaseModel


class TransactionSearchResponse(BaseModel):
    id: int
    description: str
    amount: float
    transaction_type: str

    model_config = {
        "from_attributes": True
    }