from ..db import db
from sqlalchemy import ForeignKey


class Read(db.Model):
    __table_name__ = "read"

    user_id = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey("post.id"), primary_key=True)
