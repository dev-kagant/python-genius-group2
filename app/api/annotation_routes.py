from flask import Blueprint, request
from flask_login import current_user, login_required
from app.models import db, Annotation

annotation_routes = Blueprint("annotation", __name__)


# ADD NEW ANNOTATION
@annotation_routes.route("/create", methods=["POST"])
@login_required
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
    annotations = Annotation.query \
                            .filter_by(song_Id=id) \
                            .order_by(Annotation.start) \
                            .all()
    return {"annotations": [annotation.to_dict() for annotation in annotations]}


# GET ANNOTATION BY ID
@annotation_routes.route("/get/<int:id>", methods=["GET"])
def getAnnotationById(id):
    annotation = Annotation.query.get(id)
    return annotation.to_dict()


# UPDATE ANNOTATION
@annotation_routes.route("/patch/<int:id>", methods=["PATCH"])
@login_required
def updateAnnotation(id):
    print(id)
    try:
        annotation = Annotation.query.get(id)
        annotation.annotation = request.json["annotation"]
        print(annotation)
    except Exception as err:
            print(f'{err.__class__.__name__}: {err}')
            return {'errors': ['Sorry, cannot process your request']}, 400
    else:
        db.session.commit()
        return annotation.to_dict()


# DELETE ANNOTATION
@annotation_routes.route("/delete/<int:id>", methods=["DELETE"])
@login_required
def deleteAnnotation(id):
    annotation = Annotation.query.get(id)
    db.session.delete(annotation)
    db.session.commit()
    return {'message': 'Annotation Deleted.'}
