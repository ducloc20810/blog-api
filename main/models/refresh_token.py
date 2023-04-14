from ..db import db

class RefreshToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)