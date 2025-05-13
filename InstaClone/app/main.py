from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schemas.posts import PostIn
from models.posts import Post
from config.database import get_db

app = FastAPI()

@app.post('/create')
def create(post: PostIn, session: Session = Depends(get_db)):
    new_post = Post(**post.model_dump())
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post