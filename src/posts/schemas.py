import datetime

from pydantic import BaseModel, Field

from authors.schemas import Author
from categories.schemas import Category


class PostBase(BaseModel):
    title: str
    created_at: datetime.datetime = Field(default=datetime.datetime.now())
    content: str
    author_id: int
    category_id: int


class PostUpdate(PostBase):
    pass


class PostCreate(PostBase):
    pass


class Post(PostBase):
    p_id: int

    class Config:
        from_attributes = True
