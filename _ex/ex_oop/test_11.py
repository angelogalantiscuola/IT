from _ex.ex_oop.e11 import ( # type: ignore
    Ricetta,
    Primo,
    Secondo,
    Dolce,
    verifica_ingredienti,
    stampa_ricette,
)  # type: ignore


def test_ricetta_str():
    ricetta = Ricetta("Generica", 10, ["Ingrediente1"], "Facile")
    assert str(ricetta) == "Generica - 10 min - Difficoltà: Facile"


def test_primo_attributes():
    primo = Primo(
        "Spaghetti alla Carbonara",
        20,
        ["Spaghetti", "Uova", "Pancetta"],
        "Media",
        "Spaghetti",
        "Carbonara",
    )
    assert primo.tipo_pasta == "Spaghetti"
    assert primo.sugo == "Carbonara"


def test_secondo_attributes():
    secondo = Secondo(
        "Bistecca alla Fiorentina",
        30,
        ["Bistecca", "Sale", "Pepe"],
        "Alta",
        "Manzo",
        "Media",
    )
    assert secondo.tipo_carne == "Manzo"
    assert secondo.cottura == "Media"


def test_dolce_attributes():
    dolce = Dolce(
        "Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert"
    )
    assert dolce.zucchero == 200
    assert dolce.tipo_dolce == "Dessert"


def test_aggiungi_ingrediente():
    ricetta = Ricetta("Generica", 10, ["Ingrediente1"], "Facile")
    ricetta.aggiungi_ingrediente("Ingrediente2")
    assert "Ingrediente2" in ricetta.ingredienti


def test_verifica_ingredienti():
    primo = Primo(
        "Spaghetti alla Carbonara",
        20,
        ["Spaghetti", "Uova", "Pancetta"],
        "Media",
        "Spaghetti",
        "Carbonara",
    )
    secondo = Secondo(
        "Bistecca alla Fiorentina",
        30,
        ["Bistecca", "Sale", "Pepe"],
        "Alta",
        "Manzo",
        "Media",
    )
    dolce = Dolce(
        "Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert"
    )
    ricette = [primo, secondo, dolce]
    disponibili = [
        "Spaghetti",
        "Uova",
        "Pancetta",
        "Bistecca",
        "Sale",
        "Pepe",
        "Mascarpone",
        "Caffè",
        "Savoiardi",
    ]
    ricette_possibili = verifica_ingredienti(ricette, disponibili)
    assert len(ricette_possibili) == 3


def test_stampa_ricette(capfd):
    primo = Primo(
        "Spaghetti alla Carbonara",
        20,
        ["Spaghetti", "Uova", "Pancetta"],
        "Media",
        "Spaghetti",
        "Carbonara",
    )
    secondo = Secondo(
        "Bistecca alla Fiorentina",
        30,
        ["Bistecca", "Sale", "Pepe"],
        "Alta",
        "Manzo",
        "Media",
    )
    dolce = Dolce(
        "Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert"
    )
    ricette = [primo, secondo, dolce]
    stampa_ricette(ricette)
    captured = capfd.readouterr()
    assert "Spaghetti alla Carbonara - 20 min - Difficoltà: Media" in captured.out
    assert "Bistecca alla Fiorentina - 30 min - Difficoltà: Alta" in captured.out
    assert "Tiramisù - 30 min - Difficoltà: Media" in captured.out
