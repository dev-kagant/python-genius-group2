from flask import Blueprint, jsonify
from app.models import Song

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
    form = AddSong()                #need actual form name
    if form.validate_on_submit():
        song = Song()
        form.populate_obj(song)
        Song.add(song)
        Song.commit()
        return song.id          #need to render the song page
    return "Bad Data"      #need to be changed to validator response


@song_routes.route("/edit/<int:id>", methods=['GET', 'POST'])
def get_song():
    song = Song.query.get(id)
    return AddSong(song)                       #need to test this route

def edit_song():
    form = AddSong()       #need actual form name may be a different form than add
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
    return "Bad Data"      #need to be changed to validator response


@song_routes.route("/delete/<int:id>", methods=['DELETE'])
def delete_song():
    song = Song.query.get(id)
    Song.delete(song)
    Song.commit()
    return redirect("/songs")
