from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, PasswordField, FileField, HiddenField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf.file import FileRequired, FileAllowed, FileField

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(max=50)])
    email = EmailField("Email", validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=32)])
    password2 = PasswordField("Confirm password", validators=[DataRequired(), Length(min=8, max=32)])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=32)])
    submit = SubmitField("Login")


class ImageForm(FlaskForm):
    file = FileField("Select file to upload", validators=[FileRequired(), FileAllowed(ALLOWED_EXTENSIONS)])
    description = TextAreaField("Description", validators=[Length(max=150)])
    submit = SubmitField("Upload")

class GalleryForm(FlaskForm):
    title = StringField("Gallery Title", validators=[DataRequired(), Length(min=1, max=50)])
    description = TextAreaField("Description", validators=[Length(max=150)])
    submit = SubmitField("Create Gallery")