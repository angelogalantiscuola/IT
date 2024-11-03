import pytest
from auto_motore import Auto, Motore  # Assicurati che il percorso sia corretto


def test_auto_attributes():
    auto = Auto("Fiat", "500")
    assert auto.marca == "Fiat"
    assert auto.modello == "500"
    assert auto.motore is None


def test_motore_attributes():
    motore = Motore("ENG123456", "Benzina")
    assert motore.numero_seriale == "ENG123456"
    assert motore.tipo == "Benzina"
    assert motore.auto is None


def test_associazione_auto_motore():
    auto = Auto("Fiat", "500")
    motore = Motore("ENG123456", "Benzina")

    auto.associa_motore(motore)

    assert auto.motore == motore
    assert motore.auto == auto


def test_associazione_uno_a_uno():
    auto1 = Auto("Fiat", "500")
    motore1 = Motore("ENG123456", "Benzina")
    auto2 = Auto("Toyota", "Corolla")
    motore2 = Motore("ENG654321", "Diesel")

    auto1.associa_motore(motore1)
    auto2.associa_motore(motore2)

    assert auto1.motore == motore1
    assert motore1.auto == auto1
    assert auto2.motore == motore2
    assert motore2.auto == auto2


def test_sovrascrittura_associazione():
    auto = Auto("Fiat", "500")
    motore1 = Motore("ENG123456", "Benzina")
    motore2 = Motore("ENG654321", "Diesel")

    auto.associa_motore(motore1)
    assert auto.motore == motore1
    assert motore1.auto == auto

    auto.associa_motore(motore2)
    assert auto.motore == motore2
    assert motore2.auto == auto
    assert motore1.auto is None
