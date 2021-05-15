from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Log In')

class NoteForm(FlaskForm):
  note = TextField('Note', validators=[DataRequired()])
  submit = SubmitField('Record')