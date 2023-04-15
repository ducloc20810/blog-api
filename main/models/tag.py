from main.db import db
from sqlalchemy.orm import relationship
from .base import TimestampMixin


class Tag(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    posts = relationship("Post", secondary="post_tag", back_populates="tags")
