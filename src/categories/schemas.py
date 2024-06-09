from pydantic import BaseModel, Field, EmailStr


class CategoryBase(BaseModel):
    name: str
    description: str

class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Category(CategoryBase):
    c_id: int

    class Config:
        from_attributes = True