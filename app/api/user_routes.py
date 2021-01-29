from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash
from app.models import db, User, Song, Annotation
from app.forms import EditUserForm


user_routes = Blueprint('users', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {"users": [user.to_dict() for user in users]}


@user_routes.route('/<int:id>')
def user(id):
    user = User.query.get(id)
    if user:
        return user.to_dict()
    return {'errors': ['User Not Found']}, 404


@user_routes.route("/update", methods=["PATCH"])
def update_user():
    """
    Update user information
    """
    form = EditUserForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User.query.get(current_user.id)
        try:
            user.username = form.data['username'],
            user.email = form.data['email'],
            if form.data['password']:
                user.hashed_password = generate_password_hash(form.data['password']),
            user.user_avatar = form.data['avatar'],
            user.user_background = form.data['background'],
            user.user_bio = form.data['bio']
        except Exception as err:
            print(f'{err.__class__.__name__}: {err}')
            return {'errors': ['Sorry, cannot process your request']}, 400
        else:
            db.session.add(user)
            db.session.commit()
            return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400
