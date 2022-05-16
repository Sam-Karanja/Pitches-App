from tokenize import String
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from impotlib_metadata import email
from wtforms import stringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators= [DaraRequired(),Email])
    username = StringField('Enter your username', validators = [DataRequired()])
    password = PasswordField('Password', validators[DateRequired(), EqualTo('password_confirm', message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm password', validators= [DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is an account with that email")

    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("That username is already taken")

class LoginForm(FlaskForm):
    email = stringField('Your Email Address', validators= [DataRequired(),Email])
    password = PasswordField('password', validators = [DataRequired])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign in')







d