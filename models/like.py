from ..db import db
from sqlalchemy import ForeignKey


class Like(db.Model):
    __table_name__ = "like"

    user_id = db.Column(db.Integer, ForeignKey("user.id"), primary_key=True)
    post_id = db.Column(db.Integer, ForeignKey("post.id"), primary_key=True)
