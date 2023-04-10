from ..db import db
from sqlalchemy import Table
from sqlalchemy.orm import relationship, Mapped
from .tag import Tag
from .comment import Comment


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = relationship("User", back_populates="posts")
    tags: Mapped[list["Tag"]] = relationship(
        "Tag", secondary="post_tag", back_populates="posts"
    )
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="post")
    liked_users = relationship("User", secondary="like", back_populates="likes")
    read_users = relationship("User", secondary="read", back_populates="reads")
    favorite_users = relationship(
        "User", secondary="favorite", back_populates="favorites"
    )


post_tag = Table(
    "post_tag",
    db.Model.metadata,
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"), primary_key=True),
)
