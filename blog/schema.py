from pydantic import BaseModel
from typing import List,Optional
class blog(BaseModel):
    name: str
    description: str
    price: float




class User(BaseModel):
    name : str
    email : str
    password : str

class Showuser(User):
    name : str
    email : str
    blogs : List[blog] = []

    class config():
        orm_model = True

class Showblog(blog):
    name: str
    description: str
    price: float
    creater : User

    class config():
        orm_model = True

class Login(BaseModel):
    username :str
    password : str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None