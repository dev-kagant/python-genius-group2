from flask import Blueprint, request
from flask_login import current_user
from app.models import db, Song

song_routes = Blueprint("songs", __name__)

#GET A SINGLE SONG
@song_routes.route("/<int:id>")
def song(id):
    song = Song.query.get(id)
    return song.to_dict()


# GET ALL SONGS IN DATABASE
@song_routes.route("", methods=['GET'])
def songs():
    songs = Song.query.all()
    return {"songs": [song.to_dict() for song in songs]}


# ADD A NEW SONG
@song_routes.route("/new_song", methods=['POST'])
def add_song():
    song = Song(user_Id=current_user.id, **request.json)
    db.session.add(song)
    db.session.commit()
    return song.to_dict()


# EDIT SONG FACTS
@song_routes.route("/edit", methods=['PATCH'])
def edit_song():
    song = Song.query.get(request.json['id'])
    song.artist = request.json['artist']
    song.title = request.json['title']
    song.album = request.json['album']
    song.written_by = request.json['written_by']
    song.label = request.json['label']
    song.song_url = request.json['song_url']
    song.media_url = request.json['media_url']
    song.song_icon = request.json['song_icon']
    song.song_background_image = request.json['song_background_image']
    song.release_date = request.json['release_date']
    db.session.commit()
    return song.to_dict()

#EDIT SONG LYRICS
@song_routes.route("/edit-lyrics", methods=['PATCH'])
def edit_lyrics():
    song = Song.query.get(request.json['songId'])
    song.lyrics = request.json['lyrics']
    db.session.commit()
    return song.to_dict()

#EDIT SONG BIO
@song_routes.route("/edit-bio", methods=['PATCH'])
def edit_bio():
    song = Song.query.get(request.json['songId'])
    song.song_bio = request.json['song_bio']
    db.session.commit()
    return song.to_dict()


# DELETE A SONG
@song_routes.route("/delete", methods=['DELETE'])
def delete_song():
    songId = request.json["song"]
    song = Song.query.get(int(songId))
    db.session.delete(song)
    db.session.commit()
