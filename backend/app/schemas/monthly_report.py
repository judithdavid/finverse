from pydantic import BaseModel


class MonthlyReport(BaseModel):
    month: str
    income: float
    expense: float
