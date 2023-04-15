from main.db import db
from .base import TimestampMixin


class RefreshToken(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
