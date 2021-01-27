from .db import db

class Vote(db.Model):
  __tablename__ = "votes"

  id = db.Column(db.Integer, primary_key = True)
  votes = db.Column(db.Integer, nullable=False)
  user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  song_Id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
