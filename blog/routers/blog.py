from fastapi import HTTPException,status,APIRouter,Depends
from .. import schema,models
from sqlalchemy.orm import Session
from ..repository import blog
from ..database import get_db
from typing import List

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request : schema.blog,db : Session= Depends(get_db)):
    return blog.create(request,db)

@router.get('/',response_model=List[schema.Showblog])
def all(db : Session= Depends(get_db)):
    return blog.get_all(db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return blog.delete(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schema.blog, db: Session = Depends(get_db)):
    return blog.change(id,request,db)

@router.get('/{id}',response_model=schema.Showblog)
def show(id,db : Session= Depends(get_db)):
    return blog.show_one(id,db)
