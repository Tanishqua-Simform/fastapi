from typing import List
from uuid import uuid4, UUID
from sqlalchemy import ForeignKey, types
from sqlalchemy.orm import relationship, Mapped, mapped_column
from config.database import Base

class Post(Base):
    __tablename__ = 'posts'

    uid: Mapped[UUID] = mapped_column(types.Uuid, primary_key=True, index=True, default=uuid4)
    file_url: Mapped[str] = mapped_column(nullable=False)
    caption: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.uid", ondelete="CASCADE"), nullable=False)

    post_liked_by: Mapped[List["User"]] = relationship(back_populates="post_liked")
    comments: Mapped[List["Comment"]] = relationship(back_populates="commented_on")

    posted_by: Mapped["User"] = relationship(back_populates="posts")