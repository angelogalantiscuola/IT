from _ex.ex_oop.e09 import Libro  # type: ignore


def test_libro_getter_setter():
    libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
    assert libro.titolo == "Il Signore degli Anelli"
    assert libro.autore == "J.R.R. Tolkien"
    assert libro.pagine == 1200

    libro.titolo = "Lo Hobbit"
    assert libro.titolo == "Lo Hobbit"

    libro.autore = "J.R.R. Tolkien"
    assert libro.autore == "J.R.R. Tolkien"

    libro.pagine = 310
    assert libro.pagine == 310


def test_libro_invalid_titolo():
    libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
    try:
        libro.titolo = ""
    except ValueError as e:
        assert str(e) == "Il titolo non può essere una stringa vuota."


def test_libro_invalid_autore():
    libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
    try:
        libro.autore = ""
    except ValueError as e:
        assert str(e) == "L'autore non può essere una stringa vuota."


def test_libro_invalid_pagine():
    libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
    try:
        libro.pagine = -1
    except ValueError as e:
        assert str(e) == "Il numero di pagine deve essere un numero positivo."
