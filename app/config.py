"""
Basic configuration file for the application.
Variables are read from the environment variables from docker-compose.yml
"""
import os


class BaseConfig(object):
    """Base configuration for the application."""
    # Database configuration
    DB_NAME = os.environ['POSTGRES_DB']
    DB_USER = os.environ['POSTGRES_USER']
    DB_PASS = os.environ['POSTGRES_PASSWORD']
    DB_PORT = os.environ['DATABASE_PORT']
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{DB_USER}:{DB_PASS}@postgres:{DB_PORT}/{DB_NAME}'
    )
    # Encryption key
    SECRET_KEY = os.environ['SECRET_KEY']
