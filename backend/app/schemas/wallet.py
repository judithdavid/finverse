from pydantic import BaseModel


class WalletBase(BaseModel):
    name: str
    balance: float


class WalletCreate(WalletBase):
    user_id: int


class WalletResponse(WalletBase):
    id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }
