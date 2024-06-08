from typing import List


from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from . import schemas
from . import service


router = APIRouter(prefix='/categories', tags=['Categories'])


@router.get('', response_model=List[schemas.Category], description='Return all categories ', summary='Get all')
def get_categories():
    return service.get_all()


@router.get("/{c_id}", response_model=schemas.Category, description='Return category by id', summary='Get')
def get_category_by_id(c_id: int):
    category = service.get_by_id(c_id)
    return category


@router.post("", response_model=schemas.Category, description='Create category', summary='Create')
def create_category(category: schemas.CategoryCreate):
    return service.create(category)


@router.put("/{c_id}", response_model=schemas.Category, description='Update category', summary="Update")
def update_category(c_id: int, category: schemas.CategoryUpdate):
    return service.update(c_id, category)


@router.delete("/{c_id}", description='Delete category', summary="Delete")
def delete_category_by_id(c_id: int):
    service.delete(c_id)
    return {'message': "deleted"}
