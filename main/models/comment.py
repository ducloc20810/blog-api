from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from main.db import db
from .base import TimestampMixin


class Comment(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey("post.id"))
    user_id = db.Column(db.Integer, ForeignKey("user.id"))
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    parent_id = db.Column(db.Integer, ForeignKey("comment.id"), default=None)

    # Define relationship with Post
    post = relationship("Post", back_populates="comments")

    # Define relationship with User
    user = relationship("User", back_populates="comments")

    # Define relationship with parent comment
    parent_comment = relationship("Comment", remote_side=[id], back_populates="replies")

    # Define relationship with replies to comment
    replies = relationship("Comment", back_populates="parent_comment")
