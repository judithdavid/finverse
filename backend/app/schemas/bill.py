from pydantic import BaseModel


class BillBase(BaseModel):
    name: str
    amount: float
    due_date: str
    is_paid: bool = False


class BillCreate(BillBase):
    user_id: int


class BillResponse(BillBase):
    id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }
