from pydantic import BaseModel

class PostIn(BaseModel):
    image: str
    caption: str
    owner: int
