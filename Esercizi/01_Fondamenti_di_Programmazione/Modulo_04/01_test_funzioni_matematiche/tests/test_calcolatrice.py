"""
Esercizio 01: Test di Funzioni Matematiche Semplici

Obiettivo:
Prendere confidenza con la struttura di un progetto di test, l'import
di funzioni da testare e la scrittura di semplici 'assert'.

Istruzioni:
1.  Assicurati di aver creato la struttura di cartelle `src/` e `tests/`.
2.  Crea un ambiente virtuale, attivalo e installa `pytest` (`pip install pytest`).
3.  Completa il test per la funzione 'somma' (test_somma).
4.  Scrivi da zero un nuovo test per la funzione 'sottrazione' (chiamalo test_sottrazione).
    Testa che 10 - 5 sia uguale a 5.
5.  Scrivi un test per la funzione 'moltiplicazione' (test_moltiplicazione).
    Testa che 3 * 4 sia uguale a 12.
6.  Esegui `pytest` dal terminale nella cartella principale del progetto.
7.  Osserva il risultato: due test passeranno (SUCCESS) e uno fallirà (FAIL).
8.  Analizza il messaggio di errore del test fallito per capire il problema.
9.  Correggi il bug nel file `src/calcolatrice.py` e riesegui i test fino a
    quando non passano tutti.
"""

# Importa le funzioni da testare dal modulo 'calcolatrice'
from src.calcolatrice import somma, sottrazione, moltiplicazione


def test_somma():
    """Verifica il corretto funzionamento della funzione somma."""
    # ### INIZIO DEL TUO CODICE ###
    assert somma(2, 3) == 5
    assert somma(-1, 1) == 0
    # Aggiungi un altro assert a tua scelta

    # ### FINE DEL TUO CODICE ###


# ### INIZIO DEL TUO CODICE ###

# Scrivi qui la funzione test_sottrazione


# Scrivi qui la funzione test_moltiplicazione


# ### FINE DEL TUO CODICE ###
