from pydantic import BaseModel

class blog(BaseModel):
    name: str
    description: str
    price: float


class Showblog(blog):
    name: str
    description: str
    price: float

    class config():
        orm_model = True

class User(BaseModel):
    name : str
    email : str
    password : str
