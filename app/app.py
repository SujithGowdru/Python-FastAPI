from fastapi import FastAPI
from app.schemas import PostCreate


app = FastAPI()

text_posts = {1 : {"title":"First Post", "content": "text post content"}, 
              2 : {"title":"Second Post", "content": "more text post content"},
              3 : {"title":"Third Post", "content": "even more text post content"},
              4 : {"title":"Fourth Post", "content": "additional text post content"},
              5 : {"title":"Fifth Post", "content": "final text post content"},
              6 : {"title":"Sixth Post", "content": "extra text post content"},
              7 : {"title":"Seventh Post", "content": "supplementary text post content"},
              8 : {"title":"Eighth Post", "content": "ancillary text post content"},
              9 : {"title":"Ninth Post", "content": "auxiliary text post content"},
              10 : {"title":"Tenth Post", "content": "ultimate text post content"}
              }

@app.get("/posts")
def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{id}")
def get_post(id:int):
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate):
    new_post = {"title": post.title,"content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post