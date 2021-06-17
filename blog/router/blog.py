from blog.oauth2 import get_current_user
from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(req: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):

    return blog.create(req, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(id, db)

@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
def put_blog(id, req: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id, req, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_by_id(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_by_id(id, db)