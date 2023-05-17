from typing import List
from .user import UserResponseSchema
from .category import CategoryResponseSchema
from .base import BaseSchema
from .tag import TagSchema


class PostSchema(BaseSchema):
    title: str
    content: str


class PostResponseSchema(PostSchema):
    id: int
    title: str
    content: str
    author: UserResponseSchema
    category: CategoryResponseSchema | None
    tags: List[TagSchema] | None
    liked_users: List[UserResponseSchema]


class CreatePostSchema(BaseSchema):
    title: str
    content: str
    category_id: int


class UpdatePostSchema(BaseSchema):
    title: str | None
    content: str | None
    category_id: int | None
