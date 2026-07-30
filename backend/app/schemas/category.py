from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    category_type: str


class CategoryCreate(CategoryBase):
    user_id: int


class CategoryResponse(CategoryBase):
    id: int
    user_id: int

    model_config = {
        "from_attributes": True
    }
