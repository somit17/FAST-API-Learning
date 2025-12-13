from fastapi import FastAPI, Body
from pydantic import BaseModel
app = FastAPI()


class Post(BaseModel):
    title:str
    content : str

@app.get("/")
def root():
    return {"message": "Hello Welcome to fast API"}

#order matters if have same route
@app.get("/post")
def get_posts():
    return {"data":"This is your posts "}

@app.post("/create_posts")
def create_posts(new_post:Post):
    print(new_post.title)
    return {"data":"new post"}


