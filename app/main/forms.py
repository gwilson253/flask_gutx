from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class TestEmailForm(Form):
    email = StringField('Test Email', validators=[Required(), Length(1, 64), 
                                             Email()])
    username = StringField('Username')
    password = StringField('Password')
    submit = SubmitField('Run Test')
