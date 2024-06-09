from pydantic import BaseModel, Field, EmailStr


class TagBase(BaseModel):
    name: str
    description: str


class TagCreate(TagBase):
    pass


class TagUpdate(TagBase):
    pass


class Tag(TagBase):
    t_id: int

    class Config:
        from_attributes = True

