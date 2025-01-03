from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'gobi'}}

@app.get('/blog')
def about(limit=15, published:bool=True, sort:Optional[str]=None):
    if published:
        return {'data' f'{limit} published blog from db'}
    return {'data' f'{limit} blog from db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':{'all unpublished blogs'}}

@app.get('/blog/{id}')
def show(id : int):
    return{'id':id}

@app.get('/blog/{id}/comments')
def comments(id):
    return{'data':{'1':'2'}}

class blog(BaseModel):
    title : str
    body : str
    optional : bool

@app.post('/blog')
def create(blog : blog):
    return {'blog is create by title of' f'{blog.title} and {blog.body}'}

