"""Event - Forms"""
from flask_wtf import FlaskForm
from wtforms import (SubmitField, SelectField, TextAreaField,
                     DateField, TimeField, StringField)
from wtforms.validators import DataRequired
from utils.event_status_dictionary import EVENT_STATUS
from utils.timezone_dictionary import TIMEZONES


# Form - Create Event
class EventForm(FlaskForm):
    """Create an event form"""

    title = TextAreaField("Title", validators=[DataRequired()])
    subtitle = TextAreaField("Subtitle")
    description = TextAreaField("Description")
    item_description = TextAreaField("Item Description")
    event_status = SelectField("Event Status", choices=EVENT_STATUS)
    start_date = DateField("Start Date", format='%Y-%m-%d',
                           validators=[DataRequired()])
    start_time = TimeField("Start Time", format='%H:%M',
                           validators=[DataRequired()])
    start_timezone = SelectField("Timezone", choices=TIMEZONES,
                                 validators=[DataRequired()])
    address1 = StringField("Address", validators=[DataRequired()])
    address2 = StringField("Address 2", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    state = StringField("State", validators=[DataRequired()])
    zipcode = StringField("Zipcode", validators=[DataRequired()])
    submit = SubmitField("Save Event")


# Form - Event Signup
class EventSignupForm(FlaskForm):
    """Event signup form"""

    comments = TextAreaField("Comments")
    submit = SubmitField("Sign Up")
