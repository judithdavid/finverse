from pydantic import BaseModel


class CashFlowResponse(BaseModel):
    total_income: float
    total_expense: float
    net_cash_flow: float
