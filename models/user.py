from ..db import db
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    posts = relationship("Post", back_populates="posts")
    favorites = relationship(
        "Post", secondary="favorite", back_populates="favorite_users"
    )
    likes = relationship("Post", secondary="like", back_populates="liked_users")
    reads = relationship("Post", secondary="read", back_populates="read_users")
    comments = relationship("Post", secondary="comment", back_populates="comments")


like = db.Table(
    "like",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
)

favorite = db.Table(
    "favorite",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
)

read = db.Table(
    "read",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
)
