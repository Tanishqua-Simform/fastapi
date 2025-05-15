from pydantic import BaseModel, UUID4

class PostIn(BaseModel):
    file_url: str
    caption: str
    user_id: UUID4