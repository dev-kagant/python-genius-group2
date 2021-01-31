from flask import Blueprint, request
from app.models import Song

search_routes = Blueprint("search", __name__)

@search_routes.route("")
def search():
    term = request.args.get('term')
    print(term)
    try:
        song_titles = Song.query.filter(Song.title.ilike(f'%{term}%'))
        song_artists = Song.query.filter(Song.artist.ilike(f'%{term}%'))
        song_lyrics = Song.query.filter(Song.lyrics.ilike(f'%{term}%'))
    except Exception as e:
        print(f'An error ocurred that reads {e}. Check the console for more details.')


    return {
        "song_artist": [song_artist.to_dict() for song_artist in song_artists],
        "search_song": [song_title.to_dict() for song_title in song_titles],
        "song_lyric": [song_lyric.to_dict() for song_lyric in song_lyrics]}
