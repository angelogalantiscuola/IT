from _ex.ex_oop.e07 import MaterialeBiblioteca, Libro, Rivista, DVD  # type: ignore


def test_materiale_biblioteca():
    materiale = MaterialeBiblioteca("Materiale Generico", 2020)
    assert materiale.get_titolo() == "Materiale Generico"
    assert materiale.get_anno_pubblicazione() == 2020
    assert materiale.is_disponibile()

    materiale.prestito()
    assert not materiale.is_disponibile()

    materiale.restituzione()
    assert materiale.is_disponibile()


def test_libro():
    libro = Libro("Il Signore degli Anelli", 1954, "J.R.R. Tolkien", 1178)
    assert libro.get_titolo() == "Il Signore degli Anelli"
    assert libro.get_anno_pubblicazione() == 1954
    assert libro.get_autore() == "J.R.R. Tolkien"
    assert libro.get_numero_pagine() == 1178

    libro.prestito()
    assert not libro.is_disponibile()

    libro.restituzione()
    assert libro.is_disponibile()


def test_rivista():
    rivista = Rivista("National Geographic", 2023, 5, "Maggio")
    assert rivista.get_titolo() == "National Geographic"
    assert rivista.get_anno_pubblicazione() == 2023
    assert rivista.get_numero_edizione() == 5
    assert rivista.get_mese_pubblicazione() == "Maggio"

    rivista.prestito()
    assert not rivista.is_disponibile()

    rivista.restituzione()
    assert rivista.is_disponibile()


def test_dvd():
    dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
    assert dvd.get_titolo() == "Inception"
    assert dvd.get_anno_pubblicazione() == 2010
    assert dvd.get_regista() == "Christopher Nolan"
    assert dvd.get_durata() == 148

    dvd.prestito()
    assert not dvd.is_disponibile()

    dvd.restituzione()
    assert dvd.is_disponibile()


def test_ricerca():
    libro = Libro("Il Signore degli Anelli", 1954, "J.R.R. Tolkien", 1178)
    rivista = Rivista("National Geographic", 2023, 5, "Maggio")
    dvd = DVD("Inception", 2010, "Christopher Nolan", 148)

    materiali = [libro, rivista, dvd]
    risultato = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
    assert risultato.get_titolo() == "Inception"
