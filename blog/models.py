from .database import Base
from sqlalchemy import Column,String,Integer,Float,ForeignKey
from sqlalchemy.orm import relationship

class blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    user_id = Column(Integer,ForeignKey('user.id'))
    creater = relationship('user',back_populates='blogs')

class user(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('blog',back_populates='creater')