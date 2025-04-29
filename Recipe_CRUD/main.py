from fastapi import FastAPI, Depends
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create operation on Database
@app.post('/recipe')
def create_recipe(recipe: schemas.Recipe, db: Session = Depends(get_db)):
    new_recipe = models.Recipe(ingredients=recipe.ingredients, instructions=recipe.instructions, serving=recipe.serving)
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe