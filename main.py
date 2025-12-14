from typing import Optional
from random import randrange
from fastapi import FastAPI, Body,Response,status
from pydantic import BaseModel
app = FastAPI()


class Post(BaseModel):
    title:str
    content : str
    published:bool = True
    rating:Optional[int]=None


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
@app.get("/")
def root():
    return {"message": "Hello Welcome to fast API"}

#order matters if have same route
@app.get("/post")
def get_posts():
    return {"data":my_posts}

@app.post("/create_posts")
def create_posts(post:Post):
    print(post.rating)
    post_dict = post.dict()
    post_dict['id']=randrange(0,100000)
    my_posts.append(post_dict)
    return {"data":post_dict['id']}

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
