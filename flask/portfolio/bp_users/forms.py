from flask_wtf import FlaskForm
from portfolio.bp_users.models import User
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)] )
    password = PasswordField('Password',
                            validators=[DataRequired()] )
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')] )
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken')
    

class LoginForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=2, max=20)] )
    password = PasswordField('Password',
                            validators=[DataRequired()] )
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')
