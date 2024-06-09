from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from core.database import SessionLocal
from . import models, schemas


def create(post: schemas.PostCreate) -> models.Post:
    session = SessionLocal()
    db_post = models.Post(**post.dict())
    session.add(db_post)
    session.commit()
    session.refresh(db_post)
    return db_post


def get_by_id(p_id: int) -> models.Post:
    session = SessionLocal()
    db_post = session.query(models.Post).filter(models.Post.p_id == p_id).one_or_none()

    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Post not found in db"}])
    return db_post



def get_all() -> List[schemas.Post]:
    session = SessionLocal()
    posts = session.query(models.Post).all()
    return posts


def update(p_id: int, post_update: schemas.PostUpdate) -> schemas.Post:
    session = SessionLocal()
    post = session.query(models.Post).filter(models.Post.p_id == p_id).one_or_none()
    update_data = post_update.dict()
    if post:
        for field in update_data:
            setattr(post, field, update_data[field])
        session.commit()
        session.refresh(post)
        return post
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Post not found in db"}])


def delete(p_id: int):
    session = SessionLocal()
    post = session.query(models.Post).filter(models.Post.p_id == p_id).one_or_none()

    if post:
        session.delete(post)
        session.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=[{"msg": "Post not found in db"}])



