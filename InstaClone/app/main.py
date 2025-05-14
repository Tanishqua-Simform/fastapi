from fastapi import FastAPI, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from schemas.posts import PostIn
from models.posts import Post
from config.database import get_db
from config.minio import upload

app = FastAPI()

@app.post('/create')
def create(post: PostIn, session: Session = Depends(get_db)):
    new_post = Post(**post.model_dump())
    session.add(new_post)
    session.commit()
    session.refresh(new_post)
    return new_post

@app.post('/image')
async def upload_image(uploaded_file: UploadFile = File(...)):
    if uploaded_file.content_type.split('/')[0] not in ['image', 'video']:
        raise HTTPException(status_code=400, detail="Unsupported File uploaded. Please upload image or video file!")
    directory = 'static'
    file = uploaded_file.filename
    file_location = f'{directory}/{file}'
    with open(file_location, 'wb') as f:
        f.write(await uploaded_file.read())
    url = upload(directory, file)
    return {'msg': 'image uploaded successfully with FastApi', 'url': url}