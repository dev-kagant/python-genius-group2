from flask import Blueprint, request
from flask_login import current_user
from app.models import db, Song

song_routes = Blueprint("songs", __name__)


@song_routes.route("/<int:id>")
def song(id):
    song = Song.query.get(id)
    return song.to_dict()


@song_routes.route("/", methods=['GET'])
def songs():
    songs = Song.query.all()
    return {"songs": [song.to_dict() for song in songs]}


@song_routes.route("/new_song", methods=['POST'])
def add_song():
    song = Song(user_Id=current_user.id, **request.json)
    db.session.add(song)
    db.session.commit()
    return song.to_dict()



@song_routes.route("/edit/<int:id>", methods=['GET', 'POST'])
def get_song():
    song = Song.query.get(id)
    return AddSong(song)                       #need to test this route

def edit_song():
    song = Song.query.get(id)
    if form.validate_on_submit():
        song_update = Song()
        form.populate_obj(song_update)
        song.artist = song_update.artist
        song.title = song_update.title
        song.album = song_update.album
        song.written_by = song_update.written_by
        song.label = song_update.label
        song.song_bio = song_update.song_bio
        song.lyrics = song_update.lyrics
        song.song_url = song_update.song_url
        song.media_url = song_update.media_url
        song.song_icon = song_update.song_icon
        song.song_background_image = song_update.song_background_image
        song.release_date = song_update.release_date
        Song.commit()
        return song.id          #need to render the song page
    # return "Bad Data"      #need to be changed to validator response


@song_routes.route("/delete", methods=['DELETE'])
def delete_song():
    songId = request.json["song"]
    song = Song.query.get(int(songId))
    db.session.delete(song)
    db.session.commit()
