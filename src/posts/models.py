import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, backref

from core.database import Base, engine


class Post(Base):

    __tablename__ = "posts"

    p_id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    title = Column(String)
    content = Column(String)

    category_id = Column(Integer, ForeignKey('categories.c_id'))
    category = relationship("Category", back_populates='posts')

    author_id = Column(Integer, ForeignKey('authors.author_id'))
    author = relationship("Author", back_populates='posts')

    tag_id = Column(Integer, ForeignKey('tags.t_id'))
    tag = relationship("Tag", back_populates='posts')

    # author = relationship("Author", back_populates="authors")
#Base.metadata.create_all(bind=engine)