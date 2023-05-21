from main.db import db
from sqlalchemy.orm import relationship, Mapped
from .base import TimestampMixin


class Role(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    users = relationship("User", secondary="user_role", back_populates="roles")
