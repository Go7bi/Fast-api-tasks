from fastapi import FastAPI,Depends,status,Response,HTTPException,APIRouter
from typing import List
from ..import schema,models
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..routers import blog
from ..database import get_db

def create(request:schema.blog,db:Session):
    new_db = models.blog(name = request.name,description = request.description,price =request.price,user_id = 1)
    db.add(new_db)
    db.commit()
    db.refresh(new_db)
    return new_db

def get_all(db:Session):
    blogs = db.query(models.blog).all()
    return blogs

def delete(id : int,db : Session):
    blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No blog with id {id} found'
        )
    db.delete(blog)
    db.commit()
    return 'done'

def change(id:int,request:schema.blog,db:Session):
    blogs = db.query(models.blog).filter(models.blog.id == id)
    blog = blogs.first()  

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No blog with id {id} found')

    blog.name = request.name
    blog.description = request.description
    blog.price = request.price

    db.commit()
    db.refresh(blog)

    return {"message": "Blog updated successfully", "blog": blog}

def show_one(id:int,db:Session):
    blogs = db.query(models.blog).filter(models.blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'The given id of {id} id not found')
    return blogs


