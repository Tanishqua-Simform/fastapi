from pydantic import BaseModel

class UserIn(BaseModel):
    email: str
    username: str
    password: str
    first_name: str
    last_name: str
    age: int
    gender: str
    bio: str