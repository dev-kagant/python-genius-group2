from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(40), nullable = False, unique = True)
  email = db.Column(db.String(255), nullable = False, unique = True)
  hashed_password = db.Column(db.String(255), nullable = False)
  user_bio = db.Column(db.Text)
  user_avatar = db.Column(db.Text)
  user_background = db.Column(db.Text)
  songs = db.relationship('Song', backref='user', lazy=True)
  annotations = db.relationship('Annotation', backref='user', lazy=True)
  comments = db.relationship('Comment', backref='user', lazy=True)
  votes = db.relationship('Vote', backref='user', lazy=True)


  @property
  def password(self):
    return self.hashed_password


  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)


  def check_password(self, password):
    return check_password_hash(self.password, password)


  def to_dict(self):
    return {
      "id": self.id,
      "username": self.username,
      "email": self.email
    }


class Song(db.Model):
  __tablename__ = "songs"

  id = db.Column(db.Integer, primary_key = True)
  artist = db.Column(db.String(255), nullable=False)
  title = db.Column(db.String(255), nullable=False)
  album = db.Column(db.String(255), nullable=False)
  written_by = db.Column(db.String(1000))
  label = db.Column(db.String(255))
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
      "lyrics": self.lyrics,
      "song_url": self.song_url,
      "media_url": self.media_url,
      "song_icon": self.song_icon,
      "song_background_image": self.song_background_image,
      "release_date": self.release_date
    }


class Annotation(db.Model):
  __tablename__ = "annotations"

  id = db.Column(db.Integer, primary_key = True)
  song_facts = db.Column(db.Text, nullable=False)
  user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  song_Id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)


class Comment(db.Model):
  __tablename__ = "comments"

  id = db.Column(db.Integer, primary_key = True)
  user_comment = db.Column(db.Text, nullable=False)
  user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  song_Id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)


class Vote(db.Model):
  __tablename__ = "votes"

  id = db.Column(db.Integer, primary_key = True)
  votes = db.Column(db.Integer, nullable=False)
  user_Id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  song_Id = db.Column(db.Integer, db.ForeignKey('songs.id'), nullable=False)
