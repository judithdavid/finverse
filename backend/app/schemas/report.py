from pydantic import BaseModel


class ReportResponse(BaseModel):
    total_income: float
    total_expense: float
    total_balance: float
    total_budget: float
    total_savings: float
    total_investments: float
    total_loans: float
