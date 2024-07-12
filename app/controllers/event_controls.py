"""Event - Controls"""
from datetime import datetime

from flask import request

from models.user_models import User
from models.event_models import Event, EventAttendee
from app import db


# Query DB for Event information
def event_info(event_id):
    """Queries the DB for information about an event"""

    event_details = db.session.query(
        Event.id,
        Event.title,
        Event.subtitle,
        Event.description,
        Event.item_description,
        Event.start_date,
        Event.start_time,
        Event.start_timezone,
        Event.address1,
        Event.address2,
        Event.city,
        Event.state,
        Event.zipcode,
        Event.status,
        User.firstname,
        User.lastname
        # Need to filter out inactive status events
    )\
        .join(User, Event.event_leader_id == User.id)\
        .filter(Event.id == event_id).first()

    return event_details


# Query DB for Event Attendee information
def event_attendee_info(event_id):
    """Query the DB for information about
    the attendees interested in the event"""

    event_attendee_details = db.session.query(
        EventAttendee.id,
        EventAttendee.attendee_id,
        EventAttendee.attendee_status,
        EventAttendee.comments,
        User.firstname,
        User.lastname,
    )\
        .join(User, EventAttendee.attendee_id == User.id)\
        .filter(EventAttendee.event_id == event_id)\
        .order_by(EventAttendee.updated_date.asc()).all()

    return event_attendee_details


# Query DB for all events
def all_events():
    """Query the DB for all active events
    and return an attendee count as well"""

    today = datetime.now().date()
    page = request.args.get('page', 1, type=int)
    events_info = db.session.query(
        Event.id,
        Event.start_date,
        Event.start_time,
        Event.start_timezone,
        Event.title,
        Event.description,
        Event.event_status,
        Event.updated_at,
        db.func.count(EventAttendee.attendee_id).label("attendee_count"),
    )\
        .join(User, Event.event_leader_id == User.id)\
        .outerjoin(EventAttendee, db.and_(
            Event.id == EventAttendee.event_id,
            EventAttendee.attendee_status == 'interested'))\
        .filter(Event.start_date >= today, Event.event_status == "open")\
        .group_by(Event.id)\
        .order_by(Event.start_date.asc(), Event.start_time.asc())\
        .paginate(page=page, per_page=5)

    return events_info
