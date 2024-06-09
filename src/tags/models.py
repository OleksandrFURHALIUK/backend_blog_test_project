import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, backref

from core.database import Base, engine


class Tag(Base):

    __tablename__ = "tags"

    t_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    posts = relationship('Post',  back_populates='tag')

    # author = relationship("Author", back_populates="authors")
Base.metadata.create_all(bind=engine)