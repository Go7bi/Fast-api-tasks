from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import status,HTTPException,Depends
from typing import Annotated
from .import JWTtokken

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token:str= Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    

    return JWTtokken.verify_tokken(token,credentials_exception)