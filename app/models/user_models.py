"""User Model"""
# Imports
from datetime import datetime, timezone

from flask import redirect, url_for
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from login_config import login_manager

from app import db


# Login Manager - User Loader
@login_manager.user_loader
def load_user(user_id):
    """Loads the user from the database"""
    return User.query.get(int(user_id))


# Login Manager - Unauthorized Handler
@login_manager.unauthorized_handler
def unauthorized():
    """Redirects unauthorized users to the login page"""
    return redirect(url_for("users.login")), 401


# Model - User
class User(db.Model, UserMixin):
    """User model"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, index=True)
    phone = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(255))
    role = db.Column(db.String(255), default="user")
    status = db.Column(db.String(255), default="active")
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def check_password(self, password):
        """Checks if the password is correct"""
        return check_password_hash(self.password_hash, password)

    def is_superuser_admin(self):
        """Checks if the user is a superuser"""
        return self.role in ["super user", "admin"]


# Model - Login History
class LoginHistory(db.Model):
    """Login history model"""

    __tablename__ = "login_history"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    user_email = db.Column(db.String(255))
    login_date = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    login_status = db.Column(db.String(255), nullable=False)
    login_comments = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"))
