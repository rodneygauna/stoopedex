"""Event Model"""
# Imports
from datetime import datetime, timezone

from app import db


# Model - Event
class Event(db.Model):
    """Event model"""

    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    event_leader_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.Text, nullable=False)
    subtitle = db.Column(db.Text)
    description = db.Column(db.Text)
    item_description = db.Column(db.Text)
    event_status = db.Column(db.String(255), default="active")
    start_date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    start_timezone = db.Column(db.Text, nullable=False)
    address1 = db.Column(db.Text)
    address2 = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    zip = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_by = db.Column(db.Integer, db.ForeignKey('user.id'))


# Model - Event Attendee
class EventAttendee(db.Model):
    """Event Attendee model"""

    __tablename__ = "event_attendees"

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    attendee_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    attendee_status = db.Column(db.String(255), nullable=False,
                                default='interested')
    comments = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    created_by = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'))
