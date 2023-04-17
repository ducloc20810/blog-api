from main.db import db
from sqlalchemy.orm import Relationship
from .base import TimestampMixin


class Category(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    posts = Relationship("Post", back_populates="category")
