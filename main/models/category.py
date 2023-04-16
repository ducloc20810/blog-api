from main.db import db
from sqlalchemy.orm import Relationship


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    posts = Relationship("Post", back_populates="category")
