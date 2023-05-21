from main.db import db
from sqlalchemy.orm import relationship, Mapped
from .post import Post
from .base import TimestampMixin
from .role import Role


class User(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    middle_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    roles: Mapped[list[Role]] = relationship(
        "Role", secondary="user_role", back_populates="users"
    )
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="author")
    favorites = relationship(
        "Post", secondary="favorite", back_populates="favorite_users"
    )
    likes = relationship("Post", secondary="like", back_populates="liked_users")
    reads = relationship("Post", secondary="read", back_populates="read_users")
    comments = relationship("Comment", back_populates="user")

    _table_args__ = (db.UniqueConstraint("email"),)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


like = db.Table(
    "like",
    db.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
)

favorite = db.Table(
    "favorite",
    db.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
)

read = db.Table(
    "read",
    db.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("post_id", db.Integer, db.ForeignKey("post.id"), primary_key=True),
)

user_role = db.Table(
    "user_role",
    db.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id"), primary_key=True),
)
