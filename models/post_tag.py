from ..db import db
from sqlalchemy import ForeignKey


class PostTag(db.Model):
    __table_name__ = "post-tag"

    post_id = db.Column(db.Integer, ForeignKey("post.id"), primary_key=True)
    tag_id = db.Column(db.Integer, ForeignKey("tag.id"), primary_key=True)
