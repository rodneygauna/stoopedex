"""Core - Views"""
from flask import render_template, Blueprint


# Blueprint configuration
core_bp = Blueprint('core', __name__)


# Home page
@core_bp.route('/')
def index():
    """Home page"""

    return render_template('core/index.html', title='Stoopedex')
