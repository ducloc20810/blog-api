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
