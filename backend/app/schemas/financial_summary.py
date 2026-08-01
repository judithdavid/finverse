from pydantic import BaseModel


class FinancialSummaryResponse(BaseModel):
    total_assets: float
    total_liabilities: float
    net_worth: float
    savings_rate: float