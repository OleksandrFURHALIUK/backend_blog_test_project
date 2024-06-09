from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base, engine


class Category(Base):

    __tablename__ = "categories"

    c_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    posts = relationship("Post", back_populates='category')

