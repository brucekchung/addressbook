from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ContactForm(FlaskForm):
  name = StringField(
    'Name',
    validators=[DataRequired(), Length(min=1, max=30)]
  )
  street = StringField(
    'Street',
    validators=[DataRequired(), Length(min=1, max=30)]
  )
  city = StringField(
    'City',
    validators=[DataRequired(), Length(min=1, max=30)]
  )
  state = StringField(
    'State',
    validators=[DataRequired(), Length(min=1, max=30)]
  )
  zipcode = StringField(
    'Zipcode',
    validators=[DataRequired(), Length(min=1, max=30)]
  )

