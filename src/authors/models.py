from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base, engine


class Author(Base):

    __tablename__ = "authors"

    author_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String, index=True)

    posts = relationship("Post", back_populates='author')
    #pos = relationship("Item", back_populates="owner")


#Base.metadata.create_all(bind=engine)