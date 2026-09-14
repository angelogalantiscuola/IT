# Unit Testing con Pytest: Collaudo Automatico in Pratica

Ora che sappiamo costruire la matrice dei casi di prova, vediamo come automatizzare il collaudo in Python usando **`pytest`**, il framework di testing standard nell'industria.

---

## 1. Struttura del Progetto

Un progetto ordinato tiene separato il codice dell'applicazione dai file di collaudo:

```text
calcolatore_sconti/
├── .venv/                    <-- Ambiente virtuale attivo
├── src/                      <-- Cartella del codice da testare
│   └── sconti.py
└── tests/                    <-- Cartella dei test
    └── test_sconti.py
```

---

## 2. Preparazione: Installare Pytest

Con l'ambiente virtuale attivo nel terminale:

```bash
pip install pytest
```

---

## 3. Il Codice da Testare (`src/sconti.py`)

Scriviamo una funzione pura nel file `src/sconti.py`:

```python
# src/sconti.py


def calcola_prezzo_scontato(prezzo: float, sconto_percentuale: float) -> float:
    """Calcola il prezzo finale dopo lo sconto."""
    if prezzo < 0 or sconto_percentuale < 0 or sconto_percentuale > 100:
        return -1.0  # Codice di errore per input non valido

    taglio = (prezzo * sconto_percentuale) / 100.0
    return prezzo - taglio
```

---

## 4. Scrivere i Test con `assert` (`tests/test_sconti.py`)

Le convenzioni di Pytest sono semplicissime:
1. I file di test devono iniziare con `test_` (es. `test_sconti.py`).
2. Le funzioni di test al loro interno devono iniziare con `test_` (es. `test_calcolo_normale()`).

```python
# tests/test_sconti.py
from src.sconti import calcola_prezzo_scontato


def test_sconto_normale():
    # Affermo che con 100€ e sconto 20% il risultato DEVE essere 80.0
    assert calcola_prezzo_scontato(100.0, 20.0) == 80.0


def test_sconto_zero():
    # Caso limite: nessuno sconto
    assert calcola_prezzo_scontato(50.0, 0.0) == 50.0


def test_sconto_totale():
    # Caso limite: 100% di sconto (gratis)
    assert calcola_prezzo_scontato(75.0, 100.0) == 0.0


def test_sconto_valore_negativo():
    # Caso anomalo: sconto negativo non ammesso
    assert calcola_prezzo_scontato(100.0, -10.0) == -1.0
```

### Come funziona l'istruzione `assert`?
* Se la condizione è `True`, l'istruzione non fa nulla e il test prosegue silenziosamente.
* Se la condizione è `False`, l'istruzione solleva un errore (`AssertionError`) e Pytest segnala il fallimento.

---

## 5. Eseguire i Test da Terminale

Posizionati nella cartella principale del progetto e lancia semplicemente:

```bash
pytest
```

Pytest troverà automaticamente la cartella `tests`, eseguirà tutte le funzioni `test_*()` e mostrerà il risultato.

### Output in caso di successo (100% Verde):
```text
============================= test session starts ==============================
collected 4 items

tests/test_sconti.py ....                                                [100%]

============================== 4 passed in 0.02s ===============================
```

---

## 6. Come Leggere un Errore (Il Debug Rapido)

Cosa succede se la funzione contiene un bug sui decimali o sui valori limite?

Pytest non dice solo "è fallito", ma **mostra esattamente la differenza tra ciò che ti aspettavi e ciò che la funzione ha restituito**:

```text
______________________________ test_sconto_normale ______________________________
    def test_sconto_normale():
>       assert calcola_prezzo_scontato(100.0, 20.0) == 80.0
E       assert 85.0 == 80.0
E        +  where 85.0 = calcola_prezzo_scontato(100.0, 20.0)

tests/test_sconti.py:5: AssertionError
=========================== 1 failed, 3 passed in 0.04s ===========================
```

Leggendo `assert 85.0 == 80.0`, sai all'istante che la tua funzione ha restituito `85.0` invece del valore atteso `80.0`. Trovare il bug richiede pochi secondi.