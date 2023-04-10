from ..db import db
from sqlalchemy.orm import relationship


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    posts = relationship("Post", secondary="post_tag", back_populates="tags")
