import pytest
from _ex.ex_oop.e01 import Persona

# FILE: _ex/ex_oop/test_01.py


def test_saluta():
    persona = Persona("Mario", 30, "Roma")
    assert persona.saluta() == "Ciao, mi chiamo Mario."


def test_descrizione():
    persona = Persona("Mario", 30, "Roma")
    assert persona.descrizione() == "Ho 30 anni e vivo a Roma."
