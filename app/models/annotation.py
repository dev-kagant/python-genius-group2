from .db import db

class Annotation(db.Model):
  __tablename__ = "annotations"

  id = db.Column(db.Integer, primary_key = True)
  song_facts = db.Column(db.Text, nullable=False)
  user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  song_Id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
