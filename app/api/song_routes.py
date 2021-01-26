from flask import Blueprint, jsonify
from app.models import Song

song_routes = Blueprint("songs", __name__)


@song_routes.route("/<int:id>")
def song(id):
    song = Song.query.get(id)
    return song.to_dict()