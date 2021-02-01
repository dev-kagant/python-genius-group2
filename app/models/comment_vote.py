from .db import db
from datetime import datetime


class Comment_Vote(db.Model):
    __tablename__ = "comment_votes"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    votes = db.Column(db.Integer, nullable=False)
    user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comment_Id = db.Column(db.Integer, db.ForeignKey('comments.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "created": self.created,
            "updated": self.updated,
            "votes": self.votes,
            "user_Id": self.user_Id,
            "comment_Id": self.comment_Id,
        }
