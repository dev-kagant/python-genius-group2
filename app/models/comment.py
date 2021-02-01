from .db import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    user_comment = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)
    user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    song_Id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
    votes = db.relationship('Comment_Vote', backref='comments', lazy=True)


    def to_dict(self):
        return {
            "id": self.id,
            "created": self.created,
            "updated": self.updated,
            "user_comment": self.user_comment,
            "username": self.username,
            "user_Id": self.user_Id,
            "song_Id": self.song_Id,
            "votes": [vote.to_dict().user_Id for vote in self.votes]
        }
