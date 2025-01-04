from fastapi import APIRouter,Depends,HTTPException,status
from typing import List
from .. import database,schema,models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import user

router = APIRouter(
    prefix='/users',
    tags=['User']
)
get_db = database.get_db



@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request : schema.User,db: Session = Depends(get_db)):
    return user.create(request,db)

@router.get('/',response_model=List[schema.Showuser])
def showalluser(db: Session = Depends(get_db)):
    return user.showall(db)

@router.get('/{id}',response_model=schema.Showuser)
def showbyid(id : int,db : Session = Depends(get_db)):
    return user.showone(id,db)

@router.delete('/user/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id : int,db : Session = Depends(get_db)):
    return user.destroy(id,db)
