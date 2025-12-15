from random import randrange
from fastapi import FastAPI, Body,Response,status,Depends
import schemas
import models
from sqlalchemy.orm import Session
from database import engine, SessionLocal, get_db

#Create tables
models.Base.metadata.create_all(bind=engine)


app = FastAPI()





my_posts=[
    {
    "title": "title of post 1",
    "content": "content of post 1",
    "rating":4,
    "id":1
    },
{
    "title": "title of post 2",
    "content": "content of post 2",
    "rating":3,
    "id":2
    }
]


def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p
    return None

def find_index_post(id):
    for index,post in enumerate(my_posts):
        if id==post['id']:
            return index
    return None
@app.get("/")
def root():
    return {"message": "Hello Welcome to fast API"}

#order matters if have same route
@app.get("/post")
def get_posts():
    return {"data":my_posts}

@app.post("/create_posts")
def create_posts(request:schemas.Post,db:Session=Depends(get_db)):
   new_post = models.Posts(title=request.title,description=request.content)
   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return new_post

@app.get("/posts/{id}")
def get_post(id:int,response:Response):
    print(id)
    post = find_post(id)
    if not post:
        response.status_code=status.HTTP_404_NOT_FOUND
        return {"msg":f"Post with {id} was not found"}
    return {
        "post_detail" : post
    }

@app.delete("/posts/{id}")
def delete_post(id:int):
    index = find_index_post(id)
    if index == None:
        return Response(status_code=status.HTTP_404_NOT_FOUND,content=f"Post with id : {id} not found")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_200_OK,content=f"Post with id : {id} deleted successfully !")