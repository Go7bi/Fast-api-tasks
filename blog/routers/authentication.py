from fastapi import APIRouter,Depends,HTTPException,status
from .. import schema,models
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
import blog.JWTtokken as JWTtokken

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request :OAuth2PasswordRequestForm=Depends(),db:Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credential')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect password')
    

    access_token = JWTtokken.create_access_token(
        data={"sub": user.email}
    )
    return {'access_token':access_token, 'token_type':"bearer"}