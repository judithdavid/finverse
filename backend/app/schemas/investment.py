from pydantic import BaseModel


class InvestmentBase(BaseModel):
    name: str
    investment_type: str
    amount: float
    current_value: float


class InvestmentCreate(InvestmentBase):
    user_id: int


class InvestmentResponse(InvestmentBase):
    id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }
