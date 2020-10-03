from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import SubmitField


class FileForm(FlaskForm):
    file = FileField('File', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'mp4', 'webp', 'jpeg', 'webm'], 'File not allowed!')])
    submit = SubmitField('Submit')
