"""Views - Events"""
import os
from datetime import datetime, timezone

from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

from forms.event_forms import EventForm, EventSignupForm
from models.event_models import Event, EventAttendee
from controllers.event_controls import (
    event_info, event_attendee_info, all_events
)
from app import db


# Blueprint configuration
event_bp = Blueprint('events', __name__)


# Google Maps API Key
GOOGLE_MAPS_API_KEY = os.environ['GOOGLE_MAPS_API_KEY']


# Create Events
@event_bp.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
    """Creates a new event"""

    form = EventForm()
    if form.validate_on_submit():
        new_event = Event()
        form.populate_obj(new_event)
        new_event.event_leader_id = current_user.id
        new_event.created_by = current_user.id
        db.session.add(new_event)
        db.session.commit()
        flash('Event created successfully', 'success')
        return redirect(url_for('events.view_events'))
    return render_template('events/create_event.html',
                           title='Stoopedex - Create Stoop Sale', form=form)


# Edit Event
@event_bp.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    """Edit an existing event"""

    edit_event_obj = Event.query.get_or_404(event_id)
    form = EventForm(obj=edit_event_obj)
    if form.validate_on_submit():
        form.populate_obj(edit_event_obj)
        edit_event_obj.updated_at = datetime.now(timezone.utc)
        edit_event_obj.updated_by = current_user.id
        db.session.commit()
        flash('Event updated successfully.', 'success')
        return redirect(url_for('events.view_events'))
    return render_template('events/create_event.html',
                           title='Stoopedex - Edit Stoop Sale', form=form)


# View (single) event
@event_bp.route('/event/<int:event_id>')
@login_required
def event(event_id):
    """View a (single) event"""

    event = Event.query.get_or_404(event_id)
    event_details = event_info(event_id)
    event_roster = event_attendee_info(event_id)

    is_current_user_in_roster = False
    is_current_user_canceled = False
    is_current_user_event_leader = False

    if event.event_leader_id == current_user.id:
        is_current_user_event_leader = True
    for attendee in event_attendee_info(event_id):
        if attendee.attendee_id == current_user.id:
            is_current_user_in_roster = True
            if attendee.attendee_status == 'canceled':
                is_current_user_canceled = True

    return render_template(
        'events/event.html', title='Stoopedex - View Event',
        event=event, event_details=event_details,
        event_roster=event_roster,
        is_current_user_canceled=is_current_user_canceled,
        is_current_user_in_roster=is_current_user_in_roster,
        is_current_user_event_leader=is_current_user_event_leader,
        GOOGLE_MAPS_API_KEY=GOOGLE_MAPS_API_KEY
    )


# View ALL events
@event_bp.route('/view_events')
def view_events():
    """View all events"""

    all_event_info = all_events()

    return render_template('events/view_events.html',
                           title='Stoopedex - All Events',
                           all_event_info=all_event_info,
                           GOOGLE_MAPS_API_KEY=GOOGLE_MAPS_API_KEY)


# Sign up for event
@event_bp.route('/sign_up/<int:event_id>', methods=['GET', 'POST'])
@login_required
def event_signup(event_id):
    """Enable the user to sign up for an existing event"""

    form = EventSignupForm()
    event = Event.query.get_or_404(event_id)
    if event.event_leader_id == current_user.id:
        flash('You are the leader of this event, you do not have sign up',
              'info')
    if event.event_status != 'active':
        flash('The event is no longer open for signups.', 'danger')
        return redirect(url_for('events.event', event_id=event_id))
    if form.validate_on_submit():
        event_signup_data = EventAttendee(
            event_id=event_id,
            attendee_id=current_user.id,
            attendee_status='interested',
            comments=form.comments.data,
            created_by=current_user.id,
            created_at=datetime.now(timezone.utc)
        )
        db.session.add(event_signup_data)
        db.session.commit()
        flash('You have successfully signed up for the event.', 'success')
        return redirect(url_for('events.event', event_id=event_id))
    return render_template('events/event_signup.html',
                           title='Stoopedex - Event Signup', event=event,
                           form=form)


# Cancel Sign up for event
@event_bp.route("/cancel_event_signup/<int:event_id>",
                methods=["GET", "POST"])
@login_required
def cancel_event_signup(event_id):
    """Changes event status to canceled"""

    event = Event.query.get_or_404(event_id)
    if event.event_status != 'open':
        flash('This event is not open for signups.', 'danger')
    if event.event_leader_id == current_user.id:
        flash("You are the leader of this event.", "danger")
    event_signup = EventAttendee.query.filter_by(
        event_id=event_id, attendee_id=current_user.id).first()
    if event_signup:
        event_signup.attendee_status = "canceled"
        event_signup.updated_date = datetime.now(timezone.utc)
        event_signup.updated_by = current_user.id
        db.session.commit()
        flash("You have removed yourself from the event.", "success")
    else:
        flash("You are not signed up for this event.", "danger")
    return redirect(url_for("events.event", event_id=event_id))
