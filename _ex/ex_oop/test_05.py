from _ex.ex_oop.e05 import Dipendente, Manager, Sviluppatore  # type: ignore


def test_dipendente():
    dipendente = Dipendente("Mario", 30000)
    assert dipendente.get_nome() == "Mario"
    assert dipendente.get_stipendio() == 30000

    dipendente.set_nome("Luigi")
    dipendente.set_stipendio(35000)
    assert dipendente.get_nome() == "Luigi"
    assert dipendente.get_stipendio() == 35000


def test_manager():
    manager = Manager("Alice", 50000, 3)
    assert manager.get_nome() == "Alice"
    assert manager.get_stipendio() == 50000
    assert manager.get_numero_di_team() == 3

    manager.set_nome("Eve")
    manager.set_stipendio(55000)
    manager.set_numero_di_team(4)
    assert manager.get_nome() == "Eve"
    assert manager.get_stipendio() == 55000
    assert manager.get_numero_di_team() == 4


def test_sviluppatore():
    sviluppatore = Sviluppatore("Bob", 40000, "Python")
    assert sviluppatore.get_nome() == "Bob"
    assert sviluppatore.get_stipendio() == 40000
    assert sviluppatore.get_linguaggio_di_programmazione() == "Python"

    sviluppatore.set_nome("Charlie")
    sviluppatore.set_stipendio(45000)
    sviluppatore.set_linguaggio_di_programmazione("Java")
    assert sviluppatore.get_nome() == "Charlie"
    assert sviluppatore.get_stipendio() == 45000
    assert sviluppatore.get_linguaggio_di_programmazione() == "Java"
