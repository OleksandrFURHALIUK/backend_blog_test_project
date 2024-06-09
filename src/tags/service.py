from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from core.database import SessionLocal
from . import models, schemas


def create(tag: schemas.TagCreate) -> models.Tag:
    session = SessionLocal()
    db_tag = models.Tag(**tag.dict())
    session.add(db_tag)
    session.commit()
    session.refresh(db_tag)
    return db_tag


def get_by_id(t_id: int) -> models.Tag:
    session = SessionLocal()
    tag = session.query(models.Tag).filter(models.Tag.t_id == t_id).one_or_none()

    if not tag:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Tag not found in db"}])
    return tag


def get_all() -> List[schemas.Tag]:
    session = SessionLocal()
    tags = session.query(models.Tag).all()
    return tags


def update(t_id: int, tag_update: schemas.TagUpdate) -> schemas.Tag:
    session = SessionLocal()
    tag = session.query(models.Tag).filter(models.Tag.t_id == t_id).one_or_none()
    update_data = tag_update.dict()
    if tag:
        for field in update_data:
            setattr(tag, field, update_data[field])
        session.commit()
        session.refresh(tag)
        return tag
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Tag not found in db"}])


def delete(t_id: int):
    session = SessionLocal()
    tag = session.query(models.Tag).filter(models.Tag.t_id == t_id).one_or_none()

    if tag:
        session.delete(tag)
        session.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Tag not found in db"}])
