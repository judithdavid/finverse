from pydantic import BaseModel


class NotificationBase(BaseModel):
    title: str
    message: str
    is_read: bool = False


class NotificationCreate(NotificationBase):
    user_id: int


class NotificationResponse(NotificationBase):
    id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }
