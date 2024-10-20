from _ex.ex_oop.e08 import Antipasto, Primo, Secondo, Dolce, calcola_conto, stampa_menu  # type: ignore


def test_antipasto():
    antipasto = Antipasto(
        "Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola"
    )
    assert antipasto.get_nome() == "Bruschetta"
    assert antipasto.get_prezzo() == 5.0
    assert antipasto.get_ingredienti() == ["Pane", "Pomodoro", "Basilico"]
    assert antipasto.get_porzione() == "Piccola"

    antipasto.ordina()
    assert not antipasto.is_disponibile()

    antipasto.disponi()
    assert antipasto.is_disponibile()


def test_primo():
    primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
    assert primo.get_nome() == "Spaghetti alla Carbonara"
    assert primo.get_prezzo() == 12.0
    assert primo.get_tipo_pasta() == "Spaghetti"
    assert primo.get_sugo() == "Carbonara"

    primo.ordina()
    assert not primo.is_disponibile()

    primo.disponi()
    assert primo.is_disponibile()


def test_secondo():
    secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
    assert secondo.get_nome() == "Bistecca alla Fiorentina"
    assert secondo.get_prezzo() == 25.0
    assert secondo.get_tipo_carne() == "Manzo"
    assert secondo.get_cottura() == "Media"

    secondo.ordina()
    assert not secondo.is_disponibile()

    secondo.disponi()
    assert secondo.is_disponibile()


def test_dolce():
    dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)
    assert dolce.get_nome() == "Tiramisù"
    assert dolce.get_prezzo() == 6.0
    assert dolce.get_tipo_dolce() == "Tiramisù"
    assert dolce.get_calorie() == 450

    dolce.ordina()
    assert not dolce.is_disponibile()

    dolce.disponi()
    assert dolce.is_disponibile()


def test_calcola_conto():
    antipasto = Antipasto(
        "Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola"
    )
    primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
    secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
    dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

    piatti_ordinati = [antipasto, primo, secondo, dolce]
    conto_totale = calcola_conto(piatti_ordinati)
    assert conto_totale == 48.0


def test_stampa_menu(capfd):
    antipasto = Antipasto(
        "Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola"
    )
    primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
    secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
    dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

    piatti = [antipasto, primo, secondo, dolce]
    stampa_menu(piatti)
    captured = capfd.readouterr()
    assert "Bruschetta - 5.0€ - Disponibile" in captured.out
    assert "Spaghetti alla Carbonara - 12.0€ - Disponibile" in captured.out
    assert "Bistecca alla Fiorentina - 25.0€ - Disponibile" in captured.out
    assert "Tiramisù - 6.0€ - Disponibile" in captured.out
