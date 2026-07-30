from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_balance: float
    total_income: float
    total_expense: float
    total_budget: float
