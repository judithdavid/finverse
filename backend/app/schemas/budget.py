from pydantic import BaseModel


class BudgetBase(BaseModel):
    amount: float


class BudgetCreate(BudgetBase):
    category_id: int
    user_id: int


class BudgetResponse(BudgetBase):
    id: int
    category_id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }
