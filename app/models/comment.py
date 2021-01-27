from .db import db

class Comment(db.Model):
  __tablename__ = "comments"

  id = db.Column(db.Integer, primary_key = True)
  user_comment = db.Column(db.Text, nullable=False)
  user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  song_Id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
