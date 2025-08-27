# Il Tuo Primo Unit Test con Pytest

Abbiamo visto *perché* è importante testare. Ora vediamo *come* farlo. Useremo `pytest`, la libreria di testing più popolare e potente nell'ecosistema Python.

### 1. Cos'è `pytest`?

`pytest` è un framework di testing che rende la scrittura di test semplice e leggibile. Richiede pochissima "cerimonia" (codice standard ripetitivo) e si basa su convenzioni intelligenti per trovare ed eseguire i test automaticamente.

### 2. Preparazione del Progetto

Un progetto ben organizzato separa il codice dell'applicazione dal codice di test. La struttura standard è la seguente:

```
progetto_calcolatrice/
├── src/                      <-- Cartella per il codice sorgente
│   └── calcolatrice.py
└── tests/                    <-- Cartella per i test
    └── test_calcolatrice.py
```

1.  **Crea le cartelle:** Crea una cartella per il progetto e, al suo interno, le sottocartelle `src` e `tests`.
2.  **Crea l'ambiente virtuale e installa pytest:**
    ```bash
    # Dalla cartella principale del progetto
    python -m venv .venv
    source .venv/Scripts/activate  # o .venv/bin/activate
    pip install pytest
    ```

### 3. Il Codice da Testare

Creiamo una funzione molto semplice nel file `src/calcolatrice.py`.

```python
# File: src/calcolatrice.py

def somma(a: int, b: int) -> int:
    """Restituisce la somma di due numeri interi."""
    return a + b
```

### 4. Scrivere il Primo Test

Ora scriviamo il codice che verificherà la nostra funzione `somma`. `pytest` si basa su due semplici convenzioni:
1.  I file di test devono iniziare con `test_` (es. `test_calcolatrice.py`).
2.  Le funzioni di test al loro interno devono iniziare con `test_` (es. `test_somma`).

Ecco il contenuto del file `tests/test_calcolatrice.py`:

```python
# File: tests/test_calcolatrice.py

# 1. Importa la funzione che vuoi testare
from src.calcolatrice import somma

# 2. Definisci la funzione di test
def test_somma_due_numeri_positivi():
    # 3. Prepara gli input e l'output atteso
    input1 = 5
    input2 = 3
    risultato_atteso = 8
    
    # 4. Chiama la funzione e verifica il risultato con 'assert'
    assert somma(input1, input2) == risultato_atteso

def test_somma_un_positivo_e_un_negativo():
    """Un test può essere anche più conciso."""
    assert somma(10, -5) == 5
```

### 5. L'Istruzione `assert`: il Cuore del Test

`assert` è una parola chiave di Python che controlla se una condizione è `True`.
*   Se `condizione` è `True`, l'istruzione non fa nulla e il test prosegue.
*   Se `condizione` è `False`, l'istruzione solleva un errore (`AssertionError`) e il test **fallisce**.

`pytest` usa `assert` per verificare le nostre aspettative. La riga `assert somma(5, 3) == 8` si legge come: "Affermo che il risultato di `somma(5, 3)` deve essere uguale a `8`".

### 6. Eseguire i Test

Con l'ambiente virtuale attivo, posizionati nella cartella principale del progetto (`progetto_calcolatrice/`) e lancia questo semplice comando:

```bash
pytest
```

`pytest` troverà automaticamente la cartella `tests`, i file `test_*.py` e le funzioni `test_*()` al loro interno, e li eseguirà.

**Output in caso di successo:**
Se tutto va bene, vedrai un output simile a questo, con dei puntini verdi che indicano i test passati.
```
============================= test session starts ==============================
...
collected 2 items

tests/test_calcolatrice.py ..                                            [100%]

============================== 2 passed in 0.01s ===============================
```

**Output in caso di fallimento:**
Proviamo a rovinare la nostra funzione `somma` in `src/calcolatrice.py`:
```python
def somma(a: int, b: int) -> int:
    return a * b # Errore intenzionale!
```
Ora, rieseguiamo `pytest`:
```
============================= test session starts ==============================
...
collected 2 items

tests/test_calcolatrice.py FF                                            [100%]

=================================== FAILURES ===================================
______________________ test_somma_due_numeri_positivi ______________________

    def test_somma_due_numeri_positivi():
        input1 = 5
        input2 = 3
        risultato_atteso = 8
    
>       assert somma(input1, input2) == risultato_atteso
E       assert 15 == 8
E        +  where 15 = somma(5, 3)

tests/test_calcolatrice.py:11: AssertionError
...
=========================== 2 failed in 0.03s ============================
```
`pytest` non solo ci dice che i test sono falliti (`FF`), ma ci mostra esattamente *perché*: si aspettava `8` ma ha ricevuto `15`. Questo feedback immediato e preciso è ciò che rende il testing automatico così potente.