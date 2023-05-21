from typing import List
from .user import UserResponseSchema
from .base import BaseSchema


class CommentRequestSchema(BaseSchema):
    content: str


class CommentResponseSchema(BaseSchema):
    id: int
    content: str
    user: UserResponseSchema


class ReplyResponseSchema(CommentResponseSchema):
    parent_id: int


class CommentResponseSchemaWithReplies(CommentResponseSchema):
    parent_id: None
    replies: List[ReplyResponseSchema]
