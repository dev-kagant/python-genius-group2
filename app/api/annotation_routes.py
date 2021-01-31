from flask import Blueprint, request
from flask_login import current_user
from app.models import db, Annotation

annotation_routes = Blueprint("annotation", __name__)


# ADD NEW ANNOTATION
@annotation_routes.route("/create", methods=["POST"])
def addAnnotation():
    annotation = Annotation(user_Id=current_user.id, **request.json)
    try:
        db.session.add(annotation)
        db.session.commit()
        return annotation.to_dict()
    except Exception as err:
        print(f'{err.__class__.__name__}: {err}')
        return {'errors': ['Sorry, cannot process your request']}, 400


# GET ANNOTATION FOR SONG PAGE
@annotation_routes.route("/get/songs/<int:id>", methods=["GET"])
def getAnnotationForSong(id):
    print(id)
    annotations = Annotation.query \
                            .filter_by(song_Id=id) \
                            .order_by(Annotation.start) \
                            .all()
    return {"annotations": [annotation.to_dict() for annotation in annotations]}
