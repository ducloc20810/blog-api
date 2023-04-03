from ..db import db
from sqlalchemy.orm import relationship


class Tag(db.Model):
    __table_name__ = "tag"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    posts = relationship("Post", secondary="post-tag", back_populates="tags")
