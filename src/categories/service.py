from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from core.database import SessionLocal
from . import models, schemas


def create(category: schemas.CategoryCreate) -> models.Category:
    session = SessionLocal()
    db_category = models.Category(**category.dict())
    session.add(db_category)
    session.commit()
    session.refresh(db_category)
    return db_category


def get_by_id(c_id: int) -> models.Category:
    session = SessionLocal()
    db_category = session.query(models.Category).filter(models.Category.c_id == c_id).one_or_none()

    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Category not found in db"}])
    return db_category


def get_all() -> List[schemas.Category]:
    session = SessionLocal()
    db_categories = session.query(models.Category).all()
    return db_categories


def update(c_id: int, category: schemas.CategoryUpdate) -> models.Category:
    session = SessionLocal()
    db_category= session.query(models.Category).filter(models.Category.c_id == c_id).one_or_none()
    if db_category:
        db_category.name = category.name
        db_category.description = category.description
        session.commit()
        session.refresh(db_category)
        return db_category
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Category not found in db"}])


def delete(c_id: int):
    session = SessionLocal()
    db_category= session.query(models.Category).filter(models.Category.c_id == c_id).one_or_none()
    if db_category:
        session.delete(db_category)
        session.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Category not found in db"}])
