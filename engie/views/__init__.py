from .example import example_routes


def register_views(application):
    application.register_blueprint(example_routes)
