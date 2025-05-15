from enum import Enum
from regex import regex
from uuid import uuid4, UUID
from datetime import datetime
from typing import List
from sqlalchemy import event, types
from sqlalchemy.orm import validates, relationship, Mapped, mapped_column
from config.database import Base

class GenderEnum(Enum):
    MALE = 'male'
    FEMALE = 'female'
    TRANSGENDER = 'transgender'

class RoleEnum(Enum):
    ADMIN = 'admin'
    USER = 'user'

class User(Base):
    __tablename__ = "users"

    uid: Mapped[UUID] = mapped_column(types.Uuid, primary_key=True, index=True, default=uuid4)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str]
    last_name: Mapped[str]
    age: Mapped[int]
    gender: Mapped[GenderEnum] = mapped_column(nullable=False)
    bio: Mapped[str]
    deleted: Mapped[bool] = mapped_column(default=False)
    role: Mapped[RoleEnum] = mapped_column(default=RoleEnum.USER, nullable=False)
    pg_16: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now)

    posts: Mapped[List["Post"]] = relationship(back_populates='posted_by')
    comments: Mapped[List["Comment"]] = relationship(back_populates='commented_by')
    post_liked: Mapped[List["Post"]] = relationship(back_populates="post_liked_by")
    comment_liked: Mapped[List["Comment"]] = relationship(back_populates="comment_liked_by")

    @validates('email')
    def validate_email(self, key, value):
        expression = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"
        if not regex.match(expression, value):
            raise ValueError('Invalid Email ID entered.')
        return value
    
@event.listens_for(User, 'before_insert')
def validate(mapper, connection, target):
    if target.age > 16:
        target.pg_16 = False