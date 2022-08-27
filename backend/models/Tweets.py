from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash

from backend.configuration.database import db


class Tweets(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    file = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __init__(self,query,user_id,file):
        self.query = query
        self.user_id = user_id
        self.file = file