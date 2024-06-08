import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from core.database import Base


class Post(Base):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    title = Column(String)
    content = Column(String)
    author = relationship('Author')
    #category = relationship()
    #tags = relationship()


    #pos = relationship("Item", back_populates="owner")
