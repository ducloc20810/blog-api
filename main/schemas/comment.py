from typing import List
from .user import UserResponseSchema
from .base import BaseSchema


class CommentRequestSchema(BaseSchema):
    content: str


class CommentResponseSchema(BaseSchema):
    id: int
    content: str
    user: UserResponseSchema
    parent_id: int | None


class CommentResponseSchemaWithReplies(CommentResponseSchema):
    replies: List[CommentResponseSchema]
