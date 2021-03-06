from flask import Blueprint, request
from flask_login import current_user
from app.models import db, Song, Comment

comment_routes = Blueprint("comments", __name__)

#GET ALL SONG COMMENTS
@comment_routes.route("/new_comment", methods=['POST'])
def get_comments():
    comment = Comment(**request.json)
    db.session.add(comment)
    db.session.commit()
    return comment.to_dict()


@comment_routes.route("/<int:songId>", methods=['GET'])
def get_all_comments(songId):
    song = Song.query.get(songId)
    return song.to_dict()


@comment_routes.route("/delete/<int:commentId>", methods=['DELETE'])
def delete_comment(commentId):
    comment = Comment.query.get(int(commentId))
    print("THIS IS COMMENT", comment)
    db.session.delete(comment)
    db.session.commit()
    return 'OK'
