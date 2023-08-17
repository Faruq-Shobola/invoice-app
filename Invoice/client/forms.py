from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email


class ClientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    number = StringField('Phone Number', validators=[DataRequired()])
    website = StringField('Website')
    client_type = SelectField('Type')
    address = TextAreaField('Address', validators=[DataRequired()])
    logo = FileField('Logo', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Add Client')