from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get('/')
def home():
    return {'data':'blog list'}

@app.get('/blog/{id}')
def show(id: int):  
    #fetch blog with id = id
    return{'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    is_published: Optional[bool]

@app.post('/createblog')
def create_blog(body: Blog):
    return body
