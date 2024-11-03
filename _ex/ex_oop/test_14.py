import pytest
from studente_corso import Studente, Corso  # Assicurati che il percorso sia corretto


def test_studente_attributes():
    studente = Studente("Alice Rossi", "MAT123")
    assert studente.nome == "Alice Rossi"
    assert studente.matricola == "MAT123"
    assert studente.corsi == []


def test_corso_attributes():
    corso = Corso("Programmazione Python", "PY101")
    assert corso.titolo == "Programmazione Python"
    assert corso.codice == "PY101"
    assert corso.studenti == []


def test_aggiungi_corso_a_studente():
    studente = Studente("Alice Rossi", "MAT123")
    corso = Corso("Programmazione Python", "PY101")

    studente.aggiungi_corso(corso)

    assert corso in studente.corsi
    assert studente in corso.studenti


def test_aggiungi_studente_a_corso():
    studente = Studente("Marco Bianchi", "MAT456")
    corso = Corso("Database Relazionali", "DB201")

    corso.aggiungi_studente(studente)

    assert studente in corso.studenti
    assert corso in studente.corsi


def test_associazione_multiplie():
    studente1 = Studente("Alice Rossi", "MAT123")
    studente2 = Studente("Marco Bianchi", "MAT456")
    corso1 = Corso("Programmazione Python", "PY101")
    corso2 = Corso("Database Relazionali", "DB201")
    corso3 = Corso("Sistemi Operativi", "SO301")

    studente1.aggiungi_corso(corso1)
    studente1.aggiungi_corso(corso2)
    studente2.aggiungi_corso(corso2)
    studente2.aggiungi_corso(corso3)

    # Verifica associazioni per studente1
    assert corso1 in studente1.corsi
    assert corso2 in studente1.corsi
    assert studente1 in corso1.studenti
    assert studente1 in corso2.studenti

    # Verifica associazioni per studente2
    assert corso2 in studente2.corsi
    assert corso3 in studente2.corsi
    assert studente2 in corso2.studenti
    assert studente2 in corso3.studenti


def test_no_duplicate_association():
    studente = Studente("Alice Rossi", "MAT123")
    corso = Corso("Programmazione Python", "PY101")

    studente.aggiungi_corso(corso)
    studente.aggiungi_corso(corso)  # Tentativo di aggiungere di nuovo lo stesso corso

    assert len(studente.corsi) == 1
    assert len(corso.studenti) == 1


def test_stampa_associazioni(capfd):
    studente1 = Studente("Alice Rossi", "MAT123")
    studente2 = Studente("Marco Bianchi", "MAT456")
    corso1 = Corso("Programmazione Python", "PY101")
    corso2 = Corso("Database Relazionali", "DB201")

    studente1.aggiungi_corso(corso1)
    studente1.aggiungi_corso(corso2)
    studente2.aggiungi_corso(corso2)

    # Funzione per stampare le associazioni
    print(f"{studente1.nome} è iscritto ai seguenti corsi:")
    for corso in studente1.corsi:
        print(f"- {corso.titolo} ({corso.codice})")

    print(f"\n{corso2.titolo} ha i seguenti studenti iscritti:")
    for studente in corso2.studenti:
        print(f"- {studente.nome} ({studente.matricola})")

    captured = capfd.readouterr()

    assert "Alice Rossi è iscritto ai seguenti corsi:" in captured.out
    assert "- Programmazione Python (PY101)" in captured.out
    assert "- Database Relazionali (DB201)" in captured.out
    assert "Database Relazionali ha i seguenti studenti iscritti:" in captured.out
    assert "- Alice Rossi (MAT123)" in captured.out
    assert "- Marco Bianchi (MAT456)" in captured.out
