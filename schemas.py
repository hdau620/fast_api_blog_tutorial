from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime

class UserBase(BaseModel):
    pass
    username: str = Field(min_length=1, max_length=100)
    email: EmailStr  = Field(max_length=200)

# What we expected form uer
class UserCreate(UserBase):
    pass

# what we respond back to user
class UserResponse(UserBase):
    pass
    # This allows pydantic to read from sqlalchemy model
    model_config = ConfigDict(from_attributes=True)

    id:int
    image_file: str|None
    image_path: str

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=100)

class PostCreate(PostBase):
    user_id: int

class PostUpdate(BaseModel):
    title: str| None = Field(default=None, min_length = 1, max_length=100)
    content: str| None = Field(default=None, min_length=1, max_length=100)

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    date_posted: datetime
    # Why is it working? sending nested json back to user
    author: UserResponse