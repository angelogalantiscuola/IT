import pytest
from _ex.ex_oop.e04 import Calcolatrice  # type: ignore


def test_addizione():
    assert Calcolatrice.addizione(10, 5) == 15
    assert Calcolatrice.addizione(-1, 1) == 0
    assert Calcolatrice.addizione(0, 0) == 0


def test_sottrazione():
    assert Calcolatrice.sottrazione(10, 5) == 5
    assert Calcolatrice.sottrazione(-1, 1) == -2
    assert Calcolatrice.sottrazione(0, 0) == 0


def test_moltiplicazione():
    assert Calcolatrice.moltiplicazione(10, 5) == 50
    assert Calcolatrice.moltiplicazione(-1, 1) == -1
    assert Calcolatrice.moltiplicazione(0, 5) == 0


def test_divisione():
    assert Calcolatrice.divisione(10, 5) == 2.0
    assert Calcolatrice.divisione(-10, 5) == -2.0
    assert Calcolatrice.divisione(0, 5) == 0.0
    with pytest.raises(ZeroDivisionError):
        Calcolatrice.divisione(10, 0)
