from pydantic import BaseModel, Field, EmailStr


class AuthorBase(BaseModel):
    name: str
    age: int = Field(ge=18)  # age more than 18 years
    email: EmailStr | None = Field(default=None)


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorCreate):
    pass


class Author(AuthorBase):
    author_id: int

    class Config:
        from_attributes = True
