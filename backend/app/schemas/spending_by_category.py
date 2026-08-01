from pydantic import BaseModel


class CategorySpending(BaseModel):
    category: str
    total_amount: float
