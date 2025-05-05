from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    name: str
    age: int
    gender: str
    bio: str


class UserLogin(BaseModel):
    username: str
    password: str

class UserProfileIn(BaseModel):
    name: str
    age: int
    gender: str
    bio: str

class UserProfileOut(UserProfileIn):
    username: str