import pytest

from engie.main import create_application


@pytest.fixture()
def application():
    application = create_application()
    yield application


@pytest.fixture()
def client(application):
    return application.test_client()
