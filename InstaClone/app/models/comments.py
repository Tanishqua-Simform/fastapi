from uuid import uuid4, UUID
from typing import List
from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from config.database import Base

class Comment(Base):
    __tablename__ = 'comments'

    uid: Mapped[UUID] = mapped_column(primary_key=True, index=True, default=uuid4)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    post_id: Mapped[UUID] = mapped_column(ForeignKey("posts.uid", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.uid", ondelete="CASCADE"), nullable=False)

    comment_liked_by: Mapped[List["User"]] = relationship(back_populates="comment_liked")

    commented_by: Mapped["User"] = relationship(back_populates="comments")
    commented_on: Mapped["Post"] = relationship(back_populates="comments")