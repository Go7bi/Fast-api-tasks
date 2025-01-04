from fastapi import HTTPException,status
from .. import schema,models
from sqlalchemy.orm import Session
from ..hashing import Hash


def create(request:schema.User,db:Session):
    user_db = models.user(name = request.name,email = request.email,password = Hash.bcrpt(request.password))
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

def showall(db:Session):
    showall = db.query(models.user).all()
    return showall

def showone(id:int,db:Session):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={f'The given id of {id} is no found'})
    return user

def destroy(id:int,db:Session):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={f'The given id of {id} is no found'})
    db.delete(user)
    db.commit()
    return 'done'