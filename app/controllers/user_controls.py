"""User - Controls"""
from datetime import datetime, timezone

from flask import request

from app import db
from models.user_models import LoginHistory


def log_user_login(user_id, user_email, status, comments):
    """Logs a user's login attempt"""

    ip_address = request.access_route[0] if request.access_route else request.remote_addr
    log_login = LoginHistory(
        user_id=user_id,
        user_email=user_email,
        login_status=status,
        login_comments=comments,
        login_date=datetime.now(timezone.utc),
        ip_address=ip_address
    )
    db.session.add(log_login)
    db.session.commit()
