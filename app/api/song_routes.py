from flask import Blueprint
from app.models.user.py import Song

song_routes = Blueprint("songs", __name__)


@song_routes.route("/<int:id>")
def song(id):
    song = Song.query.get(id)
    return song.to_dict()