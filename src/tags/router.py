from typing import List

from fastapi import APIRouter

from . import service, schemas, models

router = APIRouter(prefix='/tags', tags=['Tags'])


@router.get('', response_model=List[schemas.Tag])
def get_all_tags() -> List[schemas.Tag]:
    return service.get_all()


@router.get('/{t_id}', response_model=schemas.Tag)
def get_tag(t_id: int) -> schemas.Tag:
    tag = service.get_by_id(t_id=t_id)
    return tag


@router.post('/', response_model=schemas.Tag)
def create(tag: schemas.TagCreate) -> schemas.Tag:
    tag = service.create(tag)
    return tag


@router.put('/{id}', response_model=schemas.Tag)
def update(t_id: int, tag_update: schemas.TagUpdate):
    tag = service.update(t_id=t_id, tag_update=tag_update)
    return tag


@router.delete('/{id}')
def delete(t_id: int):
    service.delete(t_id)
    return {'msg': 'deleted'}
