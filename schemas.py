from pydantic import BaseModel, ConfigDict, Field

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    date_posted: str