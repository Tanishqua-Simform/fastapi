from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session, Query
from . import schemas, models, tokens
from .database import Base, engine
from .hashing import Hash

app = FastAPI()

Base.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

@app.get("/users/", tags=['Database Integration', 'Password Hashing'])
def all_user(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No user found!')
    return users

@app.post("/register/", tags=['Auth'])
def register(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        name=request.name,
        age=request.age,
        gender=request.gender,
        bio=request.bio
        )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User already exists!')

@app.post("/login/", tags=['Auth'])
def login(request: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User Not Found!')
    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Incorrect password!')
    return "Login Successful"

@app.post('/jwt-login/', tags=['Auth'])
def jwt_login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username==request.username).first()
    if not user or not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect Credentials!')
    access_token = tokens.create_access_token(data={'sub':user.username})
    return {'access_token': access_token, 'token_type': "bearer"}

def get_user(token_user: Annotated[str, Depends(tokens.get_token_user)], db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username==token_user)
    return user

@app.get('/profile/', response_model=schemas.UserProfileOut, tags=['Profile'])
def profile(user: Annotated[Query[models.User], Depends(get_user)]):
    return user.first()

@app.put('/profile/', response_model=schemas.UserProfileOut, tags=['Profile'])
def profile(request: schemas.UserProfileIn, user: Annotated[Query[models.User], Depends(get_user)], db: Session = Depends(get_db)):
    user.update(request.model_dump()) 
    user = user.first()
    db.commit()
    db.refresh(user)
    return user

def is_admin(user:Annotated[Query[models.User], Depends(get_user)]):
    user = user.first()
    if user.username != 'admin':
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='You are not admin.')
    return user

@app.get('/admin/', tags=['Role Based'])
def admin(user: models.User = Depends(is_admin)):
    return {'message': f'Welcome, {user.name}!'}