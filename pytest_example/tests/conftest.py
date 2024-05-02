# tests/conftest.py

# When a test function requests a fixture (by including the fixture's name as a parameter),
# pytest will automatically call the corresponding fixture function
# and pass its return value to the test function.
import pytest

from pytest_example.app.app import app

# This conftest.py file is used by pytest to define setup code that is shared among multiple test files.


# The @pytest.fixture decorator is used to mark functions that return these shared resources,
# which are called "fixtures".
@pytest.fixture
# This fixture simply returns the Flask application instance app
def flask_app():
    # The yield keyword is part of Python's generator syntax. In the context of pytest fixtures,
    # it's used to separate setup code (before the yield) from cleanup code (after the yield).
    # In this conftest.py file, there's no cleanup code, so yield is essentially acting like return.
    yield app


@pytest.fixture
# This fixture depends on the app fixture (you can see app is a parameter of the client function).
# It returns a test client instance created by calling app.test_client().
# This test client allows you to make requests to the app without running the server.
def client(flask_app):
    return flask_app.test_client()
