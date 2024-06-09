from typing import List

from fastapi import APIRouter

from . import service, schemas, models

router = APIRouter(prefix='/posts', tags=['Posts'])


@router.get('', response_model=List[schemas.Post])
def get_all_posts() -> List[schemas.Post]:
    return service.get_all()


@router.get('/{p_id}', response_model=schemas.Post)
def get_post(p_id: int) -> schemas.Post:
    post = service.get_by_id(p_id=p_id)
    return post


@router.post('/', response_model=schemas.Post)
def create(post: schemas.PostCreate) -> schemas.Post:
    post = service.create(post)
    return post


@router.put('/{id}', response_model=schemas.Post)
def update(p_id: int, post_update: schemas.PostUpdate):
    post = service.update(p_id=p_id, post_update=post_update)
    return post


@router.delete('/{id}')
def delete(p_id: int):
    service.delete(p_id)
    return {'msg': 'deleted'}
