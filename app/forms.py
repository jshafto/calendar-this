from flask_wtf import FlaskForm
from wtforms import (
  StringField, DateField, TimeField, TextAreaField, BooleanField, SubmitField
)
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets.html5 import DateInput, TimeInput
from datetime import datetime

class AppointmentForm(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  start_date =  DateField('Start Date', validators=[DataRequired()], widget=DateInput())
  start_time = TimeField('Start Time', validators=[DataRequired()], widget=TimeInput())
  end_date = DateField('End Date', validators=[DataRequired()], widget=DateInput())
  end_time = TimeField('End Time', validators=[DataRequired()], widget=TimeInput())
  description = TextAreaField('Description', validators=[DataRequired()])
  private = BooleanField('Private')
  submit = SubmitField('Submit')
  def validate_end_date(self, field):
    start = datetime.combine(self.start_date.data, self.start_time.data),
    end = datetime.combine(field.data, self.end_time.data),
    if start >= end:
      raise ValidationError("End date/time must come after start date/time")
    if not self.start_date.data == field.data:
      raise ValidationError("End date must the be the same as start date")
