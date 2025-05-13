from uuid import uuid4
from sqlalchemy import Column, String, Integer, UUID
from config.database import Base

class Post(Base):
    __tablename__ = 'posts'

    uid = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    image = Column(String, nullable=False)
    caption = Column(String)
    owner = Column(Integer, nullable=False)