from flask import Flask

from .views import register_views


def create_application():
    # Create flask application.
    application = Flask(__name__)

    # Register views.
    register_views(application)

    return application
