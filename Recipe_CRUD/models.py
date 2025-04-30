from sqlalchemy import Column, Integer, String
from database import Base

class Recipe(Base):
    __tablename__ = 'recipes'
    
    id = Column(Integer, primary_key=True, index=True)
    ingredients = Column(String)
    instructions = Column(String)
    serving = Column(Integer)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)