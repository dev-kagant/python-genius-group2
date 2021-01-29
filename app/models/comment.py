from .db import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    user_comment = db.Column(db.Text, nullable=False)
    user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    song_Id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
