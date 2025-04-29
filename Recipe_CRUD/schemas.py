from pydantic import BaseModel

## Pydantic Schema
class Recipe(BaseModel):
    ingredients: str
    instructions: str
    serving: int