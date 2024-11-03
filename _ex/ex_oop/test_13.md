import pytest
from casa_stanza import Casa, Stanza # Assicurati che il percorso sia corretto

def test_casa_attributes():
casa = Casa("Via delle Rose 15", "Maria Rossi")
assert casa.indirizzo == "Via delle Rose 15"
assert casa.proprietario == "Maria Rossi"
assert casa.stanze == []

def test_stanza_attributes():
stanza = Stanza("Soggiorno", 30)
assert stanza.nome == "Soggiorno"
assert stanza.superficie == 30

def test_aggiungi_stanza():
casa = Casa("Via delle Rose 15", "Maria Rossi")
stanza = Stanza("Soggiorno", 30)
casa.aggiungi_stanza(stanza)
assert stanza in casa.stanze

def test_multi_aggiungi_stanza():
casa = Casa("Via delle Rose 15", "Maria Rossi")
stanza1 = Stanza("Soggiorno", 30)
stanza2 = Stanza("Cucina", 15)
stanza3 = Stanza("Camera da Letto", 20)
casa.aggiungi_stanza(stanza1)
casa.aggiungi_stanza(stanza2)
casa.aggiungi_stanza(stanza3)
assert len(casa.stanze) == 3
assert stanza1 in casa.stanze
assert stanza2 in casa.stanze
assert stanza3 in casa.stanze

def test_stampa_stanze(capfd):
casa = Casa("Via delle Rose 15", "Maria Rossi")
stanza1 = Stanza("Soggiorno", 30)
stanza2 = Stanza("Cucina", 15)
casa.aggiungi_stanza(stanza1)
casa.aggiungi_stanza(stanza2)

    casa.stampa_stanze()
    captured = capfd.readouterr()
    assert "Soggiorno (30 mq)" in captured.out
    assert "Cucina (15 mq)" in captured.out
