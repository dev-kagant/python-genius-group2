from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, URL, Optional
from app.models import User

class EditUserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[Optional()])
    bio = StringField('bio')
    avatar = StringField('avatar', validators=[URL(), Optional()])
    background = StringField('background', validators=[URL(), Optional()])