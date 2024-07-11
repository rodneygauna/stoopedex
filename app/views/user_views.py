"""Views - Users"""
from datetime import datetime, timezone
from random import randint
from flask import (
    Blueprint, abort, render_template, request, flash, redirect, url_for, session
)
from werkzeug.security import generate_password_hash
from flask_login import (
    login_user, login_required, logout_user, current_user
)
from controllers.user_controls import log_user_login
from forms.user_forms import (
    RegisterUserForm, EditProfileForm, LoginForm, ChangePasswordForm, ShortCodeForm
)
from models.user_models import (
    User, LoginHistory
)
from app import db


# Blueprint configuration
users_bp = Blueprint('users', __name__)


# Register User
@users_bp.route('/register', methods=['GET', 'POST'])
def register_user():
    """Register a new user"""

    form = RegisterUserForm()
    # TODO: Do I need to create a support route? If so, add check if first user
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('This email is already registered', 'warning')
            return redirect(url_for('users.register_user'))
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data),
            created_at=datetime.now(timezone=utc)
        )
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!', 'success')
        return redirect(url_for('users.login'))
    return render_template('users/register.html',
                           title='Stoopedex - Register',
                           form=form)


# Log in
@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Logs in a user"""

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            log_user_login(user.id if user else None, form.email.data,
                           'failed', 'Invalid email or password')
            flash('Login failed. Please check your email and password.', 'warning')
            return redirect(url_for('users.login'))
        elif user.status == 'INACTIVE':
            log_user_login(user.id, user.email, 'failed', 'Account is inactive')
            flash('Your account is inactive. Please contact an administrator.', 'warning')
            return redirect(url_for('users.login'))

        session['user_id'] = user.id
        return redirect(url_for('user.complete_login'))
    return render_template('users/login.html', title='Stoopdex - Login', form=form)


# Route - Complete Login
@users_bp.route('/complete_login')
def complete_login():
    """Completes the login process if the short code (2FA) is correct"""
    
    user = User.query.get_or_404(session.get('user_id'))
    login_user(user, remember=True)
    session.pop('short_code', None)
    next_page = request.args.get('next', url_for('core.index'))
    flash('Login successful.', 'success')
    return redirect(next_page)


# Logout user
@users_bp.route('/logout')
@login_required
def logout():
    """Logs out a user"""
   
    logout_user()
    return redirect(url_for('core.index'))
