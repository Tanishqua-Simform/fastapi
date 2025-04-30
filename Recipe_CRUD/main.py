from typing import List
from fastapi import FastAPI, Depends, Response, status, HTTPException
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from hashing import Hash

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create operation on Database
@app.post('/recipe', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowRecipe, tags=['Recipes'])
def create_recipe(recipe: schemas.Recipe, db: Session = Depends(get_db)):
    new_recipe = models.Recipe(ingredients=recipe.ingredients, instructions=recipe.instructions, serving=recipe.serving)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

# Read All operation on Database
@app.get('/recipe', status_code=status.HTTP_200_OK, response_model=List[schemas.ShowRecipe], tags=['Recipes'])
def all_recipe(response: Response, db: Session = Depends(get_db)):
    recipes = db.query(models.Recipe).all()
    if not recipes:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': 'No recipes found'} # Alternatively, raise an exception (in below code)
    return recipes

# Read One operation on Database
@app.get('/recipe/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowRecipe, tags=['Recipes'])
def get_recipe_detail(id, db: Session = Depends(get_db)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id==id).first()
    if not recipe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Recipe with id {id} not found.') # Alternatively, return response with status_code 404
    return recipe

# Update operation on Database
@app.put('/recipe/{id}', status_code=status.HTTP_201_CREATED, tags=['Recipes'])
def update_recipe(id, request: schemas.Recipe, db: Session = Depends(get_db)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id==id)
    if not recipe.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Recipe with id {id} not found.')
    recipe.update(request.model_dump())
    db.commit()
    return f'Recipe with id {id} updated successfully.'

# Delete operation on Database
@app.delete('/recipe/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Recipes'])
def delete_recipe(id, db: Session = Depends(get_db)):
    recipe = db.query(models.Recipe).filter(models.Recipe.id==id)
    if not recipe.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Recipe with id {id} not found.')
    recipe.delete()
    db.commit()
    return f'Recipe with id {id} deleted successfully.'

# Create User
@app.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['Users'])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get specific user
@app.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=['Users'])
def get_user(id, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found!')
    return user