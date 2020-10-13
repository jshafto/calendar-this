from flask_wtf import FlaskForm
from wtforms import (
  StringField, DateField, TimeField, TextAreaField, BooleanField, SubmitField
)
from wtforms.validators import DataRequired
from wtforms.widgets.html5 import DateInput, TimeInput

class AppointmentForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  start_date =  DateField('Start Date', validators=[DataRequired()], widget=DateInput())
  start_time = TimeField('Start Time', validators=[DataRequired()], widget=TimeInput())
  end_date = DateField('End Date', validators=[DataRequired()], widget=DateInput())
  end_time = TimeField('End Time', validators=[DataRequired()], widget=TimeInput())
  description = TextAreaField('Description', validators=[DataRequired()])
  private = BooleanField('Private')
  submit = SubmitField('Submit')
