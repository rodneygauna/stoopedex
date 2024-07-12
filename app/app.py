"""Flask app for the web interface of the project."""
# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig


# Flask app configuration
app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


# Importing models after db is defined
from models.user_models import *
from models.event_models import *


# Flask-Login configuration
from login_config import login_manager
login_manager.init_app(app)
login_manager.login_view = 'users.login'


# Flask Blueprints - Imports
from views.user_views import users_bp
from views.event_views import event_bp
from views.core_view import core_bp

# Flask Blueprints - Register
app.register_blueprint(users_bp)
app.register_blueprint(event_bp)
app.register_blueprint(core_bp)


# Main run script
if __name__ == '__main__':
    app.run(debug=True)
