from .db import db
from datetime import datetime


class Annotation(db.Model):
    __tablename__ = "annotations"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    annotation = db.Column(db.Text, nullable=False),
    start = db.Column(db.Integer, nullable=False),
    end = db.Column(db.Integer, nullable=False),
    user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    song_Id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "created": self.created,
            "updated": self.updated,
            "annotation": self.annotation,
            "start": self.start,
            "end": self.end,
            "user_Id": self.user_Id,
            "song_Id": self.song_Id
        }
