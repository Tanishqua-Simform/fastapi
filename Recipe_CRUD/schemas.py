from pydantic import BaseModel

## Pydantic Schema
class Recipe(BaseModel):
    ingredients: str
    instructions: str
    serving: int

class ShowRecipe(Recipe):

    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True