from .db import db
from datetime import datetime


class Song(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    artist = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    album = db.Column(db.String(255), nullable=False)
    written_by = db.Column(db.String(1000))
    label = db.Column(db.String(255))
    song_bio = db.Column(db.Text)
    lyrics = db.Column(db.Text, nullable=False)
    song_url = db.Column(db.Text, nullable=False)
    media_url = db.Column(db.Text)
    song_icon = db.Column(db.Text)
    song_background_image = db.Column(db.Text)
    release_date = db.Column(db.Date)
    user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    annotations = db.relationship('Annotation', backref='song', lazy=True)
    comments = db.relationship('Comment', backref='song', lazy=True)
    votes = db.relationship('Vote', backref='song', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "artist": self.artist,
            "title": self.title,
            "album": self.album,
            "written_by": self.written_by,
            "label": self.label,
            "song_bio": self.song_bio,
            "lyrics": self.lyrics,
            "song_url": self.song_url,
            "media_url": self.media_url,
            "song_icon": self.song_icon,
            "song_background_image": self.song_background_image,
            "release_date": self.release_date,
            "user_Id": self.user_Id,
            "created": self.created,
            "updated": self.updated
        }
