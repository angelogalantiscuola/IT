# ruff: noqa: F841

import pytest
from _ex.ex_oop.e03 import Veicolo  # type: ignore


@pytest.fixture(autouse=True)
def reset_numero_veicoli():
    Veicolo.numero_veicoli = 0


def test_numero_veicoli_initial():
    assert Veicolo.get_numero_veicoli() == 0


def test_creazione_veicolo():
    auto1 = Veicolo("Auto", "Toyota")
    assert Veicolo.get_numero_veicoli() == 1


def test_creazione_due_veicoli():
    auto1 = Veicolo("Auto", "Toyota")
    moto1 = Veicolo("Moto", "Honda")
    assert Veicolo.get_numero_veicoli() == 2


def test_creazione_tre_veicoli():
    auto1 = Veicolo("Auto", "Toyota")
    moto1 = Veicolo("Moto", "Honda")
    bici1 = Veicolo("Bici", "Bianchi")
    assert Veicolo.get_numero_veicoli() == 3
