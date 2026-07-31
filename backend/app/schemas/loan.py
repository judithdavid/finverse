from pydantic import BaseModel


class LoanBase(BaseModel):
    lender: str
    amount: float
    remaining_amount: float
    interest_rate: float


class LoanCreate(LoanBase):
    user_id: int


class LoanResponse(LoanBase):
    id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }
