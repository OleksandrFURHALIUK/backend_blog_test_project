from typing import List


from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse

from . import schemas
from . import service


router = APIRouter(prefix='/authors', tags=['Authors'])


@router.get('', response_model=List[schemas.Author], description='Return all authors ', summary='Get all')
def get_authors():
    return service.get_all()


@router.get("/{author_id}", response_model=schemas.Author, description='Return author by id', summary='Get')
def get_author_by_id(author_id: int):
    author = service.get_by_id(author_id)
    if author:
        return author
    else:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={})


@router.post("", response_model=schemas.Author, description='Create author', summary='Create')
def get_author_by_id(author: schemas.AuthorCreate):
    return service.create(author)


@router.put("/{author_id}", response_model=schemas.Author, description='Update author', summary="Update")
def update_author(author_id: int, author: schemas.AuthorUpdate):
    return service.update(author_id, author)


@router.delete("/{author_id}", description='Delete author', summary="Delete")
def delete_author_by_id(author_id: int):
    service.delete(author_id)
    return {'message': "deleted"}
