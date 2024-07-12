"""Util to populate the DB with fake date"""
import random

from faker import Faker
from flask import Blueprint
from werkzeug.security import generate_password_hash

from models.user_models import User
from models.event_models import Event, EventAttendee
from utils.timezone_dictionary import TIMEZONES
from utils.us_states_dictionary import STATE
from app import db


faker = Faker()

# Blueprint configuration
faker_bp = Blueprint('commands', __name__)


@faker_bp.cli.command('seed_users')
def seed_users():
    """Seeds the database with fake user data"""

    user_data = []

    # Users
    for i in range(1, 100+1):
        user_data.append(User(
            email=faker.email(),
            firstname=faker.first_name(),
            lastname=faker.last_name(),
            phone=random.randint(1000000000, 9999999999),
            password_hash=generate_password_hash('password')
        ))

    for entry in user_data:
        db.session.add(entry)
    db.session.commit()


@faker_bp.cli.command('seed_events')
def seed_events():
    """Seeds the database with fake events data"""

    user_ids = [user.id for user in User.query.all()]

    events_data = []

    # Events
    for i in range(1, 100+1):
        events_data.append(Event(
            event_leader_id=random.choice(user_ids),
            title=faker.text(max_nb_chars=50),
            subtitle=faker.text(max_nb_chars=100),
            description=faker.sentence(nb_words=20),
            item_description=faker.sentence(nb_words=30),
            start_date=faker.future_date(),
            start_time=faker.time(pattern='%H:%M:%S'),
            start_timezone=random.choice([item[0] for item in TIMEZONES]),
            address1=faker.street_address(),
            address2=faker.building_number(),
            city=faker.city(),
            state=random.choice([item[0] for item in STATE]),
            zipcode=faker.postcode(),
            created_by=random.choice(user_ids)
        ))

    for entry in events_data:
        db.session.add(entry)
    db.session.commit()


@faker_bp.cli.command('seed_attendees')
def seed_attendees():
    """Seeds the database with fake attendee data"""

    user_ids = [user.id for user in User.query.all()]
    event_ids = [event.id for event in Event.query.all()]

    attendee_data = []

    # Event Attendees
    for i in range(1, 400+1):
        attendee_data.append(EventAttendee(
            event_id=random.choice(event_ids),
            attendee_id=random.choice(user_ids),
            attendee_status=random.choice(['interested', 'canceled']),
            comments=faker.paragraph(),
            created_by=random.choice(user_ids)
        ))

    for entry in attendee_data:
        db.session.add(entry)
    db.session.commit()
