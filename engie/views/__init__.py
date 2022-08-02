from .ascii import ascii_routes


def register_views(application):
    application.register_blueprint(ascii_routes)
