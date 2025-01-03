from pydantic import BaseModel
from typing import List

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
    creater : Showuser

    class config():
        orm_model = True