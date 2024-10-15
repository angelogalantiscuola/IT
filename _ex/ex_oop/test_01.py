# pylint: disable=redefined-outer-name
import pytest
from _ex.ex_oop.e01 import Persona


# The @pytest.fixture decorator in pytest is used to define a fixture function.
# Fixtures are a way to provide a fixed baseline upon which tests can reliably and repeatedly execute.
# They are used to set up some context (like creating objects, connecting to databases, etc.)
# before running tests and to clean up afterward.
@pytest.fixture
def persona():
    return Persona("Mario", 30, "Roma")


def test_saluta(persona):
    assert persona.saluta() == "Ciao, mi chiamo Mario."


def test_descrizione(persona):
    assert persona.descrizione() == "Ho 30 anni e vivo a Roma."
