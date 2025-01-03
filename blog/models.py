from .database import Base
from sqlalchemy import Column,String,Integer,Float

class blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)

class user(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)