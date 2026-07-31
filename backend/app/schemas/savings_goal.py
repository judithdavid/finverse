
from pydantic import BaseModel


class SavingsGoalBase(BaseModel):
    name: str
    target_amount: float
    current_amount: float = 0


class SavingsGoalCreate(SavingsGoalBase):
    user_id: int


class SavingsGoalResponse(SavingsGoalBase):
    id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }
