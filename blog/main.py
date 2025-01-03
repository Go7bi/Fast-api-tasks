from fastapi import FastAPI,Depends,status,Response,HTTPException
from typing import List
from .import schema,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from .hashing import Hash

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blog'])
def create(request : schema.blog,db : Session= Depends(get_db)):
    new_db = models.blog(name = request.name,description = request.description,price =request.price,user_id = 1)
    db.add(new_db)
    db.commit()
    db.refresh(new_db)
    return new_db

@app.get('/blog',response_model=List[schema.Showblog],tags=['blog'])
def all(db : Session= Depends(get_db)):
    blogs = db.query(models.blog).all()
    return blogs

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=['blog'])
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.blog).filter(models.blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No blog with id {id} found'
        )
    db.delete(blog)
    db.commit()
    return 'done'


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=['blog'])
def update(id, request: schema.blog, db: Session = Depends(get_db)):
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

@app.get('/blogs/{id}',response_model=schema.Showblog,tags=['blog'])
def show(id,db : Session= Depends(get_db)):
    blogs = db.query(models.blog).filter(models.blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'The given id of {id} id not found')
    return blogs

@app.post('/user',status_code=status.HTTP_201_CREATED,tags=['post'])
def user(request : schema.User,db: Session = Depends(get_db)):
    user_db = models.user(name = request.name,email = request.email,password = Hash.bcrpt(request.password))
    db.add(user_db)
    db.commit()
    db.refresh(user_db)
    return user_db

@app.get('/user',response_model=List[schema.Showuser],tags=['post'])
def showalluser(db: Session = Depends(get_db)):
    showall = db.query(models.user).all()
    return showall

@app.get('/user/{id}',response_model=schema.Showuser,tags=['post'])
def showbyid(id : int,db : Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={f'The given id of {id} is no found'})
    return user

@app.delete('/user/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['post'])
def delete(id : int,db : Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail={f'The given id of {id} is no found'})
    db.delete(user)
    db.commit()
    return 'done'