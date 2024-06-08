from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from core.database import SessionLocal
from . import models, schemas


def create(author: schemas.AuthorCreate) -> models.Author:
    session = SessionLocal()
    db_author = models.Author(**author.dict())
    session.add(db_author)
    session.commit()
    session.refresh(db_author)
    return db_author


def get_by_id(author_id: int) -> models.Author:
    session = SessionLocal()
    db_author = session.query(models.Author).filter(models.Author.author_id == author_id).one_or_none()
    if not db_author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Author not found in db"}])
    return db_author


def get_all() -> List[schemas.Author]:
    session = SessionLocal()
    db_authors = session.query(models.Author).all()
    return db_authors


def update(author_id: int, author: schemas.AuthorUpdate) -> models.Author:
    session = SessionLocal()
    db_author = session.query(models.Author).filter(models.Author.author_id == author_id).one_or_none()
    if db_author:
        db_author.name = author.name
        db_author.email = author.email
        db_author.age = author.age

        session.commit()
        session.refresh(db_author)
        return db_author
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Author not found in db"}])


def delete(author_id: int):
    session = SessionLocal()
    db_author = session.query(models.Author).filter(models.Author.author_id == author_id).one_or_none()
    if db_author:
        session.delete(db_author)
        session.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Author not found in db"}])
