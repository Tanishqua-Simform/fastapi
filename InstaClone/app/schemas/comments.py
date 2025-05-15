from pydantic import BaseModel, UUID4

class CommentIn(BaseModel):
    text: str
    post_id: UUID4
    user_id: UUID4