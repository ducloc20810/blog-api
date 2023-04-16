from pydantic import BaseModel
from .user import UserResponseSchema
from main.models.category import Category


class PostSchema(BaseModel):
    title: str
    content: str


class PostResponseSchema(PostSchema):
    id: int
    title: str
    content: str
    author: UserResponseSchema
    tags: str


class CreatePostSchema(BaseModel):
    title: str
    content: str
    category: Category
